# Working without a browser

You have the Ubikron tools but can't browse. You can't add new pages to the case, but there's a lot you can still do with what's been captured.

## What you can do

- **Read the case**: `understand-project` for the pages, graph, clippings and notes in one go; `get-project-memory`; `get-user-report` for the user's own report.
- **Search what was captured**: `search-history-full-text` and `search-history-urls` over every page and screenshot OCR text; `fetch-history-text` to read a page in full.
- **Work the graph**: add pivot points you find in captured pages, link them, fix types.
- **Enrich with Mimic**: `list-mimic-services`, `execute-mimic-service`, `fetch-mimic-results`. Check `fetch-all-mimic-results` first, so you don't pay for an answer the case already has.
- **Write the report**: the checks and templates are in `report.md`.

## The uniqueness gate without a browser

You can't run the Google search the gate needs. So before running any enrichment on a value:

- Look for a captured search for it in the case (`search-history-urls` for the value). If one shows it's unique, note that in memory with the page it came from, and go ahead.
- If there isn't one, ask the user to search it in quotes with Ubikron recording, or to confirm it's unique. Don't enrich until they have.

## When the case needs browsing

Say so. List the pages or searches you'd want, in order, in project memory under "Needs browsing", and tell the user. They can browse them, or pick the case up later with an agent that has a browser.
