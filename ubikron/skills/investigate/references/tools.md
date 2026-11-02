# Ubikron MCP tools

Most tools take an optional `projectId`. Leave it out and the active project is used.

## Project
| Tool | What it does |
|---|---|
| `list-projects`, `switch-project` | List the analyst's projects, then switch to one with `switch-project projectId=<id>`. Later calls without `projectId` use it, and the analyst's extension switches too, so new captures land there |
| `create-new-project` | Create a project |
| `understand-project` | One large overview: project note, visited URLs, graph, and every clipping with its annotation, AI description and OCR text. Use it to get your bearings at the start of a session, not over and over |

## Captured pages
| Tool | What it does |
|---|---|
| `fetch-all-navigation-history-entries` | Every page captured in the project |
| `search-history-urls` | Full-text search over captured pages, returning only the URLs |
| `search-history-full-text` | Full-text search over captured page content |
| `fetch-history-text` | The full captured text of one page, by URL |
| `fetch-all-history-urls-with-mhtml` | Pages that have a stored archive |
| `fetch-all-tagged-history-urls` | Pages that carry tags |

## Clippings
| Tool | What it does |
|---|---|
| `fetch-all-clippings` | Every clipping, with the page it came from and the analyst's annotation. AI descriptions and OCR text are left out |
| `get-clipping-details` | One clipping's AI description, OCR text and annotation, by its `entityReference` |
| `fetch-clipping-details-bundle-by-url` | The same for every clipping on one page, by URL |
| `edit-clipping-annotation` | Replace a clipping's annotation, by `entityReference`. It replaces the whole text, so carry over what's already there |

## Graph
| Tool | What it does |
|---|---|
| `list-available-types` | The entity types in the catalog, each with its main property and supported properties. The catalog changes, so call this before adding nodes rather than guessing a type |
| `get-graph` | What's on the graph and how it connects: node ids, types, labels, entityIds and edges. No properties or styling |
| `get-graph-details` | Properties, href, size, position, colour and attachments, only for the node and edge ids you name |
| `add-graph-node` | Add an entity node (`value` is the type's main property; everything else you know goes in `properties`) or a page node (`type=ubikron.history` with the URL) |
| `link-graph-nodes`, `remove-graph-edge-between-nodes` | Link or unlink two nodes, by node id, URL or label |
| `delete-graph-node`, `resize-graph-node`, `edit-graph-node-color`, `edit-graph-node-type` | Change a node |
| `edit-graph-edge-label`, `edit-graph-edge-color`, `reverse-graph-edge`, `toggle-graph-edge-bidirectional`, `toggle-graph-edge-style` | Change an edge |
| `attach-clipping-to-graph-node` | Show a clipping on an existing node, by node reference and the clipping's `entityReference` |
| `add-clipping-graph-node` | Put a clipping on the graph as its own image node. Its `entityReference` then works as a node reference, so you can link it |
| `batch-update-graph` | Any of the node and edge changes above in one call, as `operationsJson` (clippings are the `attach-clipping` and `add-clipping-node` actions). Returns a short summary. Use it whenever you make more than one change |

## Tags
| Tool | What it does |
|---|---|
| `list-all-tags` | The tags in the project |
| `list-colour-palette` | The analyst's colours. Pick tag colours from here |
| `tag-entity` | Tag a page (`entityType=URL`) or a clipping (`entityType=SCREENSHOT`) |

## Mimic enrichments
Users also call enrichments and their results "widgets".

| Tool | What it does |
|---|---|
| `list-mimic-configurations` | The configured Mimic endpoints. Ask the user which one to use |
| `list-mimic-services` | The services on a configuration, and the modifiers each one takes |
| `fetch-all-mimic-results` | Everything already run in the project and what it produced, without the payloads |
| `fetch-mimic-results` | Search saved results by query or entity name |
| `execute-mimic-service` | Run a service. Prefer passing the `entityId` of a graph node: its type and properties go with it, and the result is linked to it. Otherwise pass `query`, with an optional type and properties. It can take several minutes; wait for it to finish. Returns a `resultId` |
| `get-mimic-result` | One result's rendered output, the cleaned-up view and almost always what you want, plus `rawResultSize` |
| `get-mimic-raw-result` | The untouched payload, which can run to hundreds of kilobytes. Last resort: only when the rendered output is empty or broken while `rawResultSize` says there was data |

## Memory and reports
| Tool | What it does |
|---|---|
| `get-project-memory`, `append-project-memory`, `save-project-memory` | Read, add to, or replace your working memory. Plain text |
| `get-mcp-report`, `append-mcp-report`, `edit-mcp-report` | Read, add to, or replace the user-facing report |
| `get-user-report` | Read the analyst's own report (read only) |
