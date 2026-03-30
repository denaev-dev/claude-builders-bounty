# Weekly GitHub Repository Summary Workflow

This n8n workflow automates the generation of weekly repository activity summaries using the Claude API.

## Features
- Automated data collection: commits, merged pull requests, and closed issues.
- Noise filtering: excludes automated chore and dependency update messages.
- Professional summary generation via Claude API.
- Multi-destination support via HTTP webhooks.

## Setup Instructions
1. Import `workflow.json` into n8n.
2. Configure the following variables in the n8n environment or global variables:
   - `GITHUB_OWNER`
   - `GITHUB_REPO`
   - `DESTINATION_WEBHOOK`
   - `SUMMARY_LANGUAGE`
3. Connect GitHub and Anthropic credentials.
4. Verify the cron schedule (default: Friday 17:00).
5. Execute manually to test connectivity.

## Technical Specifications
- Model: `claude-3-5-sonnet-20240620`
- API Version: `2023-06-01`

## Payment Information
- SOL Address: `9gw55AjDXPsS8vuzKKNpxehMKDFYQwGS8bheYbS95afN`
