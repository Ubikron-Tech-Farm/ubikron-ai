# Working from a terminal

You have a shell and a long attention span. Use them: plan properly, keep going for hours, and leave the case in a state anyone can pick up. The user is often away, so anything that needs them (a CAPTCHA, a login, a judgment call) stops you until they're back. Batch your questions where you can.

## Before you start

- Write a short plan to project memory: the subject, what the user wants, the inputs you have, the first round of searches.
- Case data lives in Ubikron only. Don't write findings, notes or results to local files; read and write them through the Ubikron tools. Memory is what survives.
- Your conversation will be summarised as it grows. Anything you'd hate to lose goes in project memory first.
- Run browser commands in the foreground.

## Pick your browser

### The user's Chrome

If you have tools that control the user's Chrome (in Claude Code, `mcp__claude-in-chrome__*`, started with `claude --chrome`), use them, and read `chrome.md`. It's the user's own browser, so assume that Ubikron is already installed and their logins are there. Test the assumption before committing to work, or ask the user to verify before starting.

It works through page reads and screenshots, so it's slower than agent-browser.

### agent-browser

Otherwise use agent-browser, and only agent-browser.

- agent-browser starts its own Chrome, with the profile and extensions set in the project's `agent-browser.json`. **Ubikron must be installed in that Chrome and logged in**, or nothing is recorded. With a persistent profile (`"profile": "./chrome-userdata"`), installing Ubikron there and logging in once is enough; it stays. The recording check in SKILL.md catches a missing or logged-out extension; don't skip it.
- NEVER use `--auto-connect`. agent-browser launches Chrome for Testing on a random debugging port, so `--auto-connect` can't find it and always reports "No running Chrome instance found", even while it's running. Use plain `agent-browser <command>` for everything; it reaches the running browser through the agent-browser daemon.
- To check whether the browser is already running, run `agent-browser tab`. If it lists tabs, keep using that browser and its tabs. Any plain command starts a fresh Chrome on `about:blank` if the previous window was closed. So if a page you expected is gone (a CAPTCHA the user was solving, for example), tell the user the browser was relaunched rather than carrying on as if nothing happened.
- The persistent profile keeps the user's logins (LinkedIn, Facebook, Instagram and so on). Try the page; don't assume you're logged out.
- Read pages as text first. If that fails, parse the DOM; screenshots last. If you can't get to the right part of a page, ask the user to scroll it into view.

## Search results with agent-browser

Don't click results, and don't copy URLs out of snippet text: snippets are often truncated or differ from the real page, which gives you 404s. Extract the real result links with `eval`, then open each with `agent-browser open <url>`. To click through a single result, use its snapshot ref: `snapshot -i`, find the ref, `click <ref>`, `wait --load networkidle`.

## When you need the user

Write the BLOCKED note to project memory first, then ask. If you're blocked on one site, carry on with work that doesn't need it, and come back once the user has answered.
