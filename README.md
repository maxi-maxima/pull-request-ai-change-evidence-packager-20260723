# Pull Request AI Change Evidence Packager

Reviewers need concise proof of what an AI-assisted PR changed and where the evidence lives, without reading huge transcripts.

## Why now

AI code review and agentic engineering are trending, but teams still lack lightweight handoff artifacts for human reviewers.

## Install and run

```bash
python -m pull_request_ai_change_evidence_packager_20260723 --help
python -m pull_request_ai_change_evidence_packager_20260723 examples/pr
python -m pull_request_ai_change_evidence_packager_20260723 examples/pr --format markdown
```

## Example

```bash
JSON lists files, short hashes and evidence line numbers for PR comments.
```

## Self-check

```bash
python -m unittest discover -s tests
```

## Roadmap

- Git diff input
- GitHub Action wrapper

## License

MIT
