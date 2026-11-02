# Ubikron

Teaches an AI agent to run an OSINT investigation in Ubikron the way an experienced investigator would: confirm a value is unique before spending credits on it, search exhaustively rather than cherry-picking, work in rounds, and document every step in the Ubikron project so you can check its work.

## Use it

Ask the agent to investigate a person, company, domain, email address, phone number or alias, or to continue a Ubikron project. It works out whether it's running in a terminal (Claude Code, Codex), in the Claude in Chrome side panel, or in chat without a browser, and adjusts. Before browsing, it checks that Ubikron is recording.

## Install

In Claude Code:

```
/plugin marketplace add Ubikron-Tech-Farm/ubikron-ai
/plugin install ubikron@ubikron
```

On claude.ai: Customize > Plugins > Add marketplace, and paste `https://github.com/Ubikron-Tech-Farm/ubikron-ai`.

You need a Ubikron license and the Ubikron MCP server connected. Setup: https://ubikron.com/ai

## Data

The skill itself sends nothing anywhere. The agent uses your Ubikron server through its MCP tools, and the Ubikron extension records the pages it visits, as it does yours. Mimic enrichments go to the providers configured on your server. Privacy policy: https://ubikron.com/legal/privacy
