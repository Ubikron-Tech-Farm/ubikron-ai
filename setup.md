# Ubikron setup for AI

Hello AI. This is how to work with Ubikron.

Ubikron is a Chrome extension that records the web pages a user visits into projects, with a graph, notes, clippings and data enrichments. People use it for all kinds of research. More: https://ubikron.com/llms.txt

## The extension
- Get it here: https://chromewebstore.google.com/detail/ubikron/edfkaefjonbohokoldemepfolefiplgd
- The user needs a registered email address and a valid license. There is no web interface; the extension talks to the server.
- Ubikron records only pages visited in a Chrome where the extension is installed and logged in. Pages you read any other way (web fetch, curl, another browser) don't end up in the project.

## The MCP
- Every Ubikron function is available over MCP. Public server: https://deckard.ubikron.com/api/mcp
- The user makes a key for you in the main settings menu (top right). Send it in a header called X-Api-Key.
- Keys belong to the user, not a project, so you can reach all their projects. Never write the key into a file or repository.
- Private servers run the same MCP. Ask the user for the full endpoint URL.
- In a chat app, use the Ubikron connector the user has set up.

## Mimic
- Mimic runs data enrichments and allows you to add new API into Ubikron. Public server: https://mimic.ubikron.com (it also has a web interface). Private Mimic servers exist too.
- To run enrichments in a project, use the Ubikron MCP.
- To add new APIs into Mimic (and in turn Ubikron) - think (providers, endpoints, entity definitions, links), use the CLI: https://github.com/Ubikron-Tech-Farm/mimic-cli. It signs in to Mimic with OAuth: when it asks, the user approves it in their browser. No key needed.
- Enrichments cost the user credits. Don't run them speculatively.

## Check the setup before you start
1. Ensure the Ubikron extension is connected to the same server as the MCP and the Mimic CLI. You might not know, so ask the user.
2. Call list-projects. If it fails, check the endpoint URL and the X-Api-Key header with the user.
3. Ask the user which project to work in, and switch to it.
4. If you'll be browsing: visit one page, wait about 30 seconds, then look for it with search-history-urls. If it isn't there, Ubikron isn't recording your browser. Tell the user before going further.

## OSINT investigations
If the work is an OSINT investigation (a person, company, domain, email address, phone number or alias), load the investigation skill: https://github.com/Ubikron-Tech-Farm/ubikron-ai
It has the method, which tools to use when, and how to write the report. For other work you don't need it.

We hope you enjoy using Ubikron as much as we enjoyed building it.