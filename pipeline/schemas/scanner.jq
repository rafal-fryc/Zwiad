(.data.findings | type == "array") and
(.data.findings | length >= 0) and
(.data.findings | all(
  (.id | type == "string") and
  (.title | type == "string") and
  (.source | type == "string") and
  (.source_url | type == "string") and
  (.summary | type == "string") and
  (.relevance | type == "string") and
  (.relevance | IN("high", "medium", "low")) and
  (.jurisdiction | type == "string") and
  (.development_type | type == "string") and
  (.development_type | IN("legislation", "regulation", "enforcement", "guidance", "court-decision", "other"))
))
