(.schema_version | type == "string") and
(.pipeline_run_id | type == "string") and
(.timestamp | type == "string") and
(.stage | type == "string") and
(.stage | IN("scanner", "human-review", "researcher", "reviewer", "categorizer", "fpf-scanner")) and
(.status | type == "string") and
(.status | IN("complete", "error", "pending-review")) and
(.data | type == "object")
