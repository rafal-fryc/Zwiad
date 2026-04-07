(.finding_id | type == "string") and
(.report_path | type == "string") and
(.round | type == "number") and
(.round >= 1) and
(.round <= 3) and
(.claims_checked | type == "number") and
(.claims_checked >= 0) and
(.issues | type == "array") and
(.issues | all(
  (.claim | type == "string") and
  (.section | type == "string") and
  (.source_url | type == "string") and
  (.issue | type == "string") and
  (.severity | type == "string") and
  (.severity | IN("critical", "major", "minor")) and
  (.suggested_fix | type == "string") and
  (.status | type == "string") and
  (.status | IN("open", "fixed", "disputed", "upheld", "withdrawn"))
)) and
(.resolution_status | type == "string") and
(.resolution_status | IN("issues-found", "resolved", "escalate", "error"))
