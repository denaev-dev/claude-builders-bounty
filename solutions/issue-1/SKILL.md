---
name: changelog-generator
description: Automatically generates a high-quality, structured CHANGELOG.md from git history using semantic analysis.
---

# Changelog Generator Skill

Transform raw git logs into human-centric release notes.

## Commands

- `/generate-changelog` - Executes the extraction and synthesis process to update your `CHANGELOG.md`.

## Execution Workflow

1. **Extraction**:
   - Run `bash changelog.sh` to retrieve structured git context (commits, authors, file changes).

2. **Synthesis (The Intelligence)**:
   - **Categorize**: Group changes into `Added`, `Fixed`, `Changed`, `Removed`, `Security`.
   - **Abstract**: Combine multiple related technical commits into single meaningful feature points.
   - **Narrate**: Describe the *value* of the change from a user's perspective. Avoid "Updated X.ts".

3. **Output**:
   - Prepend the new entries to `CHANGELOG.md` following the [Keep a Changelog](https://keepachangelog.com/) standard.

## Guidelines

- **Concise English**: No technical jargon unless necessary.
- **Traceability**: Append the primary commit hash to each major point.
- **Standards**: Strictly follow SemVer and Markdown best practices.
