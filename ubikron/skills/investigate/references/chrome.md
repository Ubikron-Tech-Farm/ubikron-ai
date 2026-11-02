# Browsing in the analyst's Chrome

You browse in the analyst's own Chrome through the Claude in Chrome tools (`mcp__claude-in-chrome__*` in Claude Code). Ubikron runs as an extension in the same Chrome and records every page that loads there into its active project. WebFetch and WebSearch go round it, and what they read never reaches the case.

## Tabs and pages

- Start each session with `tabs_context_mcp` to see your tab group. Work in tabs you open yourself (`tabs_create_mcp`, then `navigate`). The analyst's other tabs are theirs.
- After opening a page, wait two seconds (`computer`, action `wait`) before reading or acting on it, so the page and the Ubikron widget have loaded and the capture has registered.
- Read a page with `get_page_text`. That's cheaper than a screenshot; use screenshots when layout matters or text won't do (images, maps, street view). If text fails, read the DOM; screenshots last.
- To act on an element, get its ref with `find` or `read_page`, then act on it with `computer`. Use `javascript_tool` to pull structured data, such as result links, out of a page. `browser_batch` runs several of these in one call.
- If you can't get to the right part of the screen, ask the analyst to scroll it into view.

## Search results

Open results by their real `href`, extracted with `javascript_tool`, and navigate to each. Don't click them, and don't copy URLs from snippet text: snippets are often truncated or differ from the real page, which gives you 404s.

## Captures

- Call `switch-project` before you browse. The extension follows the switch, so captures land in the project you're working in. If captures turn up in the wrong project, ask the analyst to check which project Ubikron shows.
- Captures take about 30 seconds to appear in Ubikron. Read the page in the browser while you're on it; use the history tools when you come back to it later.

## It's the analyst's real browser

- It's signed in to their real accounts (LinkedIn, Facebook, Instagram and so on). Always try the page and let it tell you whether you're signed in.
- **Your visits count as the analyst's own.** Before opening a profile on a site that shows its owner who viewed it (LinkedIn does), ask the analyst whether to go ahead.
- Claude in Chrome has its own site permissions, and some sites it won't visit. If a site is refused, tell the analyst and move on; don't go round it.

## The Ubikron widget

To clip evidence or save a page in full, read `widget.md`.
