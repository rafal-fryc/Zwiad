(.data.reports | type == "array") and
(.data.reports | all(
  (.finding_id | type == "string") and
  (.report_path | type == "string") and
  (.format | type == "string") and
  (.format | IN("client-alert", "research-memo")) and
  (.jurisdiction_tags | type == "array") and
  (.confidence_summary | type == "object") and
  (.confidence_summary.high | type == "number") and
  (.confidence_summary.medium | type == "number") and
  (.confidence_summary.low | type == "number")
))
