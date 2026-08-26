# Runtime check for fpf-scanner output (mirrors fpf-scanner.schema.json's
# load-bearing fields; keep the two in sync).
(.data.email_files_processed | type == "array") and
(.data.bills | type == "array") and
(.data.bills | all(
  (.id | type == "string") and
  (.bill_identifier | type == "string") and
  (.state | type == "string") and
  (.state_abbrev | type == "string") and
  (.session | type == "string") and
  (.title | type == "string") and
  (.summary | type == "string") and
  (.status | type == "string") and
  (.status | IN("introduced", "in-committee", "passed-committee", "passed-first-chamber",
                "passed-second-chamber", "enrolled", "signed", "vetoed", "dead", "tabled", "amended")) and
  (.category | type == "array")
))
