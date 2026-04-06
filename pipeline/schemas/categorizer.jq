(.data.filed_reports | type == "array") and
(.data.filed_reports | all(
  (.finding_id | type == "string") and
  (.source_path | type == "string") and
  (.destination_path | type == "string") and
  (.topic | type == "string") and
  (.topic | IN("privacy", "cybersecurity", "ai-law")) and
  (.subcategory | type == "string")
))
