(.data.reviews | type == "array") and
(.data.reviews | all(
  (.finding_id | type == "string") and
  (.report_path | type == "string") and
  (.status | type == "string") and
  (.status | IN("verified", "disputed", "needs-human-review")) and
  (.iteration_count | type == "number") and
  (.iteration_count >= 1) and
  (.iteration_count <= 3) and
  (.claims_checked | type == "number") and
  (.issues_found | type == "array") and
  (.issues_found | all(
    (.claim | type == "string") and
    (.issue | type == "string") and
    (.severity | type == "string") and
    (.severity | IN("critical", "major", "minor"))
  ))
))
