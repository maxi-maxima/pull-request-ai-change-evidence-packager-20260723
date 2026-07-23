# Pull Request AI Change Evidence Packager

## 解决的痛点

Reviewers need concise proof of what an AI-assisted PR changed and where the evidence lives, without reading huge transcripts.

## 为什么现在值得做

AI code review and agentic engineering are trending, but teams still lack lightweight handoff artifacts for human reviewers.

## 安装与运行

```bash
python -m pull_request_ai_change_evidence_packager_20260723 examples/pr
```

## 示例

```bash
JSON lists files, short hashes and evidence line numbers for PR comments.
```

## 自检

```bash
python -m unittest discover -s tests
```

## 路线图

- Git diff input
- Markdown PR comment output
- GitHub Action wrapper

## 许可证

MIT
