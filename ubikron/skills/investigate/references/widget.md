# The Ubikron widget

The widget is the small Ubikron logo pinned to the edge of every page. It does three things:

| Action | What it does | How |
|---|---|---|
| Take a clipping | Cuts a region of the visible page into a clipping, with a note and tags | Ctrl+`` ` `` |
| Save page as MHTML | Stores a full archive of the page as the analyst sees it | The widget's **WEB** button |
| Save page as PDF | Scrolls the page and stores it as a PDF, whole or a marked area | The widget's **PDF** button, which opens the Ubikron popup |

## Reaching the buttons

- The buttons only appear while the mouse is over the logo. Hover it first (`computer`, `hover`), then take a screenshot to see them before clicking.
- The widget lives in an open shadow root, `#ubikron-ui-root`. When a click misses, reach a button directly with `javascript_tool`, for example `document.getElementById('ubikron-ui-root').shadowRoot.querySelector('[data-testid="widget-save-mhtml-btn"]')`. The buttons only exist while the widget is hovered.

## Take a clipping

Clip anything that proves a pivot point: a profile photo, a name next to an employer, a registration record, a post.

1. Scroll so the whole region is on screen. A clipping only covers the visible viewport.
2. Press Ctrl+`` ` `` (Control and the backtick key). The page freezes into a screenshot with a crosshair. If nothing happens, hover the widget and click its clipping button (`widget-clipping-btn`).
3. Drag from one corner of the region to the opposite one (`computer`, `left_click_drag`).
4. Take a screenshot and check the box. If it's off, adjust it rather than starting again: drag a corner or edge handle to resize, or drag inside the box to move it.
5. A **Notes** panel opens under the box, with the cursor in its "Write a note here" field. Type a short note. Don't repeat what the clipping already shows. Enter saves, so use Shift+Enter for a new line.
6. Tags: the clipping starts with the analyst's last-used clipping tags, shown under the note. Remove a wrong one with its x. Add one with the tag button in the Notes header.
7. Save with Enter, or the save button in the Notes header. Escape cancels.
8. Confirm it landed with `fetch-all-clippings`, then use its `entityReference` to put it on the graph where it belongs: `attach-clipping-to-graph-node` or `add-clipping-graph-node`.

## Save page as MHTML

For any pivotal page, or one likely to change or disappear (social posts, profiles, news).

1. Hover the widget and click **WEB** (`widget-save-mhtml-btn`).
2. A "Saved page" message confirms it. The archive then shows in `fetch-all-history-urls-with-mhtml`. The analyst's settings may also tag the page on save.
3. Don't save a page you took a clipping on: clipping saves the page already. Saving twice wastes storage.

## Save page as PDF

For long pages where the whole scroll is evidence: a full timeline, a long list of results.

1. Hover the widget, then hover **WEB**. A **PDF** button appears beside it. Click it (`widget-save-pdf-btn`) to open the Ubikron popup.
2. In the popup, **Start** captures the whole page. For part of a page, set the number of scrolls (3 to 100), click **Area** and drag the area to keep; it's captured on every scroll.
3. A progress bar shows the scroll. Escape, or **Stop** in the popup, ends it early.
4. The popup opens outside the page. Take a screenshot to check you can see it. If you can't reach it, ask the analyst to click **Start** (or **Area**) for you, and wait for them to confirm.
