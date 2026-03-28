#!/bin/bash
# changelog-extractor.sh - Robust git history context provider for AI analysis
set -e

# Configuration
LATEST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || true)
if [ -z "$LATEST_TAG" ]; then
    RANGE="HEAD"
else
    RANGE="$LATEST_TAG..HEAD"
fi

# Output Metadata
echo "PROJECT_CONTEXT_START"
echo "DATE: $(date +%Y-%m-%d)"
echo "RANGE: $RANGE"
echo "LATEST_TAG: ${LATEST_TAG:-None}"
echo "PROJECT_CONTEXT_END"
echo ""

# Extract Rich Commit Data
echo "--- COMMIT HISTORY ---"
git log "$RANGE" --pretty=format:"[HASH]: %h%n[AUTHOR]: %an%n[DATE]: %ai%n[SUBJECT]: %s%n[BODY]:%n%b%n[FILES]:" --name-status
echo "--- END HISTORY ---"
