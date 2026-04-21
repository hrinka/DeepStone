---
description: Research a question across the wiki and file the answer back
allowed-tools: Read, Write, Bash, Glob, Grep
---

# Wiki Query

Read CLAUDE.md for project conventions.

The question to research: $ARGUMENTS

1. Read `wiki/index.md` to understand available content
2. Identify which wiki pages are relevant to the question
3. Read those pages
4. Synthesise a thorough answer with `[[wikilink]]` citations to specific wiki pages
5. Save the answer as `wiki/outputs/{question-slug}.md` with proper YAML frontmatter
6. Update `wiki/index.md` with the new output entry
7. Append to `wiki/log.md`

Always file the answer back — this is the compounding loop.
