use serde_json::Value;
use std::{fs,path::Path,process};
fn validate(doc:&Value)->Result<Vec<String>,String>{
    if doc.get("schema_version").and_then(Value::as_u64)!=Some(1){return Err("unsupported schema version".into())}
    if doc.pointer("/policy/allow_mutable_refs").and_then(Value::as_bool)!=Some(false){return Err("mutable refs must be disabled".into())}
    let sources=doc.get("sources").and_then(Value::as_array).filter(|v|!v.is_empty()).ok_or("at least one source is required")?;
    let mut pins=Vec::new();
    for source in sources {
        let repo=source.get("repository").and_then(Value::as_str).unwrap_or("");
        let commit=source.get("commit").and_then(Value::as_str).unwrap_or("");
        let parts:Vec<&str>=repo.split('/').collect();
        if parts.len()!=2||parts.iter().any(|s|s.is_empty()||s.chars().any(char::is_whitespace)){return Err(format!("invalid repository: {repo:?}"))}
        if commit.len()!=40||!commit.bytes().all(|b|b.is_ascii_digit()||(b'a'..=b'f').contains(&b)){return Err(format!("{repo} is not pinned to a 40-hex commit"))}
        pins.push(format!("pin-policy: exact {repo}@{commit}"));
    }
    Ok(pins)
}
fn main(){
    let root=Path::new(env!("CARGO_MANIFEST_DIR")).join("../..");
    let path=root.join("source-pins.json");
    let result=fs::read_to_string(&path).map_err(|e|e.to_string())
       .and_then(|s|serde_json::from_str::<Value>(&s).map_err(|e|e.to_string()))
       .and_then(|v|validate(&v));
    match result{
        Ok(pins)=>for pin in pins{println!("{pin}")},
        Err(e)=>{eprintln!("pin-policy: {e}");process::exit(1)}
    }
}
#[cfg(test)]mod tests{
    use super::*;
    #[test]fn valid_pins(){
        let doc=serde_json::json!({"schema_version":1,"policy":{"allow_mutable_refs":false},"sources":[{"repository":"acme/demo","commit":"abcdef0123456789abcdef0123456789abcdef01"}]});
        assert_eq!(validate(&doc).unwrap().len(),1);
    }
    #[test]fn refuse_mutable_or_nonhex(){
        let doc=serde_json::json!({"schema_version":1,"policy":{"allow_mutable_refs":true},"sources":[{"repository":"acme/demo","commit":"x"}]});
        assert!(validate(&doc).is_err());
        let doc=serde_json::json!({"schema_version":1,"policy":{"allow_mutable_refs":false},"sources":[{"repository":"acme/demo","commit":"not-a-sha"}]});
        assert!(validate(&doc).is_err());
    }
    #[test]fn reject_missing_and_ambiguous_repo(){
        let doc=serde_json::json!({"schema_version":1,"policy":{"allow_mutable_refs":false},"sources":[]});
        assert!(validate(&doc).is_err());
        let doc=serde_json::json!({"schema_version":1,"policy":{"allow_mutable_refs":false},"sources":[{"repository":"a/b/c","commit":"abcdef0123456789abcdef0123456789abcdef01"}]});
        assert!(validate(&doc).is_err());
    }
}
