---
description: Process new raw sources into the wiki
allowed-tools: Read, Write, Bash, Glob, Grep
---

# Wiki Ingest

Read CLAUDE.md for project conventions.

1. Glob `raw/**/*.md` to list all source files
2. Glob `wiki/sources/**/*.md` to list already-processed sources
3. Compare — find files in raw/ with no matching summary in wiki/sources/
4. For each new source:
   a. Create source summary in `wiki/sources/` (200-500 words, frontmatter required)
   b. Identify key concepts and entities
   c. Create new pages in `wiki/concepts/` or `wiki/entities/` if needed
   d. Append new info to existing pages (never rewrite from scratch)
   e. Add `[[wikilinks]]` connecting new content to existing pages
5. Update `wiki/index.md` and append to `wiki/log.md`
6. Report: sources processed, pages created, pages updated
