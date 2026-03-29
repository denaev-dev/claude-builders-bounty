# Autonomous PR Reviewer Agent

A zero-dependency AI agent that performs deep semantic analysis of GitHub Pull Requests using raw diff data.

## 🚀 Setup

1. **Prerequisites**: Python 3.6+ (No external libraries required).
2. **Environment**:
   ```bash
   export GITHUB_TOKEN="your_token"
   export ANTHROPIC_API_KEY="your_key"
   ```
3. **Run**:
   ```bash
   python3 review-pr.py https://github.com/owner/repo/pull/123
   ```

## 🛠 Features
- **Token Efficiency**: Fetches raw diffs (`application/vnd.github.v3.diff`) to minimize context usage.
- **Architectural Audit**: Analyzes logic, security, and performance using a Principal Engineer persona.
- **Confidence Scoring**: Helps maintainers prioritize reviews with a 1-10 reliability metric.
