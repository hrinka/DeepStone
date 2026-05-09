---
description: Health check — find gaps, broken links, contradictions
allowed-tools: Read, Write, Bash, Glob, Grep
---

# Wiki Lint

Read CLAUDE.md for project conventions.

Perform a full health check of the wiki:

1. **Contradictions** — claims in one page that conflict with another. Flag with ⚠️
2. **Orphan pages** — pages with no inbound `[[wikilinks]]`. Suggest where to add links.
3. **Broken links** — `[[wikilinks]]` pointing to non-existent pages. Create stubs for top 5.
4. **Missing frontmatter** — pages missing required YAML fields. Fix them.
5. **Gaps** — concepts frequently referenced but with no own page. Create stubs.
6. **Suggested questions** — 3-5 research questions worth exploring next.

Fix everything you can automatically.
Write a report to `wiki/outputs/lint-report-{today's date}.md`.
Append to `wiki/log.md`.
