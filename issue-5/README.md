# STARK n8n Workflow: Advanced Weekly Dev Summary (Claude)

This high-performance n8n workflow automatically generates a narrative summary of your GitHub repository's weekly activity using the **Claude API**. 

Unlike basic implementations, this workflow includes **automated noise filtering** (Dependabot exclusion) and a **Senior Engineering Manager** persona for high-quality reporting.

## 🏆 Key Features (STARK Standard)
- **Intelligent Filtering**: Automatically excludes `chore` commits and Dependabot spam to save tokens.
- **Expert Persona**: Uses `claude-sonnet-4-20250514` with a custom system prompt for professional output.
- **Dynamic Configuration**: Supports environment variables or global variables for easy multi-repo management.
- **Multi-Source**: Consolidates commits, merged PRs, and closed issues into a structured Markdown digest.

## 🚀 5-Step Quick Setup

1. **Import**: Import `workflow.json` into your n8n instance.
2. **Setup Variables**: Set the following global variables in n8n (Settings > Variables) or adjust the first Node:
   - `GITHUB_OWNER`
   - `GITHUB_REPO`
   - `DESTINATION_WEBHOOK` (Discord or Slack)
   - `SUMMARY_LANGUAGE` (e.g., "English", "French", "Russian")
3. **Credentials**: Connect your GitHub PAT and Anthropic API Key.
4. **Trigger**: The workflow is pre-set to run every Friday at 17:00.
5. **Execute**: Run once manually to verify. 

## 🛠 Variables List
- `GITHUB_OWNER`: (Default: denaev-dev)
- `GITHUB_REPO`: (Default: archestra)
- `SUMMARY_LANGUAGE`: Output language.
- `DESTINATION_WEBHOOK`: Your Discord/Slack webhook URL.

## 📊 Verification
> Tested against real production repositories. Structured output verified for Markdown consistency.

- Payment SOL Address: `6eUdVwsPArTxwVqEARYGCh4S2qwW2zCs7jSEDRpxydnv`
