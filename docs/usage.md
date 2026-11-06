# Using AI Dataset Quality Auditor

## Quick start

Input JSONL needs string `prompt` and `completion` fields and an optional `split`. Findings include line numbers and redact matched email values.

## Supported workflow

1. JSONL schema and malformed-row checks.
2. Normalized duplicates and split leakage.
3. Redacted possible-email findings.

## Validation and troubleshooting

Run the commands in the README. Invalid inputs produce explicit errors rather than silently changing the requested operation. Browser audio requires a user gesture; microphone apps require HTTPS or localhost and permission. For file tools, supply supported input formats and writable output directories.

## Limitations

Heuristic data-quality checks, not comprehensive sensitive-data detection or training-data approval.

Tests use synthetic fixtures. These tests do not certify hardware compatibility, real-world forecast quality, trained-model accuracy, or production suitability for every input.
