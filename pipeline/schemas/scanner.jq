# Key allowlist mirrors scanner.schema.json (scanner-authored fields plus the
# annotations topic_keys.py and dedup-findings.sh add later) — keep in sync.
(.data.findings | type == "array") and
(.data.findings | length >= 0) and
(.data.findings | all(
  keys - ["id", "title", "source", "source_url", "summary", "date",
          "relevance", "jurisdiction", "development_type", "category",
          "topic_key", "topic_type", "topic_key_confidence",
          "is_update", "previous_topic_key", "previous_report_path",
          "diff_signal", "status_before", "status_after", "operation"]
  == []
)) and
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
  (.development_type | IN("legislation", "regulation", "enforcement", "guidance", "court-decision", "other")) and
  (.category | type == "string") and
  (.category | IN("privacy", "cybersecurity", "ai-law"))
))
