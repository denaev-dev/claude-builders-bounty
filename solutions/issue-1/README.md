# Git Changelog Generator (Bounty #1)

A zero-dependency solution for generating structured release notes using Claude Code and Git history.

## 🚀 Setup

1. **Copy Files**: Place `changelog.sh` and `SKILL.md` in your project root or `skills/` directory.
2. **Make Executable**:
   ```bash
   chmod +x changelog.sh
   ```
3. **Run**:
   - Via Claude Code: `/generate-changelog`
   - Standalone: `bash changelog.sh` (outputs raw data for AI analysis)

## 🛠 Features
- **Semantic Grouping**: Synthesizes multiple commits into coherent feature points.
- **Automatic Classification**: Intelligently identifies fixes, features, and breaking changes.
- **Zero Noise**: Filters out CI updates, chores, and linting spam.

## 📊 Sample Output
See `CHANGELOG.md` in this directory for a real-world example generated from this repository's history.
