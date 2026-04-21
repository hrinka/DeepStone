# claude-obsidian — Claude + Obsidian Wiki Vault (DeepStone)

This vault uses the claude-obsidian pattern: a persistent, compounding knowledge base.

**Skills:** `/wiki`, `/wiki-ingest`, `/wiki-query`, `/wiki-lint`, `/save`, `/autoresearch`, `/canvas`

## What This Vault Is For

Rinka's second brain. Topics: music & DJ culture, coding, UK working holiday, make money, culture, general.

## Vault Structure

```
.raw/           source documents — immutable, Claude reads but never modifies
raw/            legacy source folder (subfolders: music, coding, culture, money, uk-whv)
wiki/           Claude-generated knowledge base
_templates/     Obsidian Templater templates
_attachments/   images and PDFs
```

## How to Use

- Drop a source into `.raw/`, then say: `ingest [filename]`
- Ask any question — Claude reads index first, then drills into relevant pages
- `/save` after a useful conversation to file it into the wiki
- `/autoresearch [topic]` to do autonomous web research
- `/wiki` to check status or scaffold anything missing

## Reading Order (efficient context)

1. Read `wiki/hot.md` first (~500 words of recent context)
2. If not enough, read `wiki/index.md`
3. Then read relevant section indexes (`wiki/concepts/_index.md`, etc.)
4. Only then read individual pages

## Wiki Structure

```
wiki/
├── hot.md          recent context cache (update after every session)
├── index.md        one-line summary of every page
├── log.md          operation history
├── overview.md     vault summary
├── concepts/       frameworks, patterns, ideas
├── entities/       people, tools, organisations
├── sources/        ingested document summaries
├── questions/      saved queries and answers
├── comparisons/    side-by-side analyses
├── canvases/       visual knowledge maps
└── meta/           vault metadata
```

## Cross-Project Access

To reference this vault from another Claude Code project, add to that project's CLAUDE.md:

```
Wiki: ~/Desktop/DeepStone
Read wiki/hot.md → wiki/index.md → specific pages as needed.
```
