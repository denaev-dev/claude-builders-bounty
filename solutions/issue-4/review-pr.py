import sys
import os
import json
import re
import urllib.request
import urllib.error

def get_pr_data(pr_url, token):
    """Fetches diff and metadata from GitHub API."""
    # Regex to parse PR URL: https://github.com/owner/repo/pull/number
    match = re.search(r"github\.com/([^/]+)/([^/]+)/pull/(\d+)", pr_url)
    if not match:
        raise ValueError("Invalid GitHub PR URL")
    
    owner, repo, pr_number = match.groups()
    base_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
    
    # 1. Get Metadata (Title/Body)
    req_meta = urllib.request.Request(base_url)
    req_meta.add_header("Authorization", f"token {token}")
    req_meta.add_header("Accept", "application/vnd.github.v3+json")
    
    with urllib.request.urlopen(req_meta) as response:
        metadata = json.loads(response.read().decode())
    
    # 2. Get Raw Diff
    req_diff = urllib.request.Request(base_url)
    req_diff.add_header("Authorization", f"token {token}")
    req_diff.add_header("Accept", "application/vnd.github.v3.diff")
    
    with urllib.request.urlopen(req_diff) as response:
        diff = response.read().decode()
        
    return metadata, diff

def review_with_claude(metadata, diff, anthropic_key):
    """Sends context and diff to Claude for analysis."""
    url = "https://api.anthropic.com/v1/messages"
    
    prompt = f"""You are a Principal Software Engineer performing a Code Review.
PR Title: {metadata.get('title')}
PR Description: {metadata.get('body')}

Instructions:
1. Analyze the following GIT DIFF for logic errors, security risks, performance issues, and architectural alignment.
2. Group findings into Summary, Critical (Blockers), and Recommendations.
3. Provide an actionable code snippet for every critical issue.
4. Assign a Confidence Score (1-10) based on how much context you have.

GIT DIFF:
{diff[:50000]}  # Simple truncation for context limits
"""

    data = {
        "model": "claude-3-5-sonnet-20240620",
        "max_tokens": 2048,
        "messages": [{"role": "user", "content": prompt}],
        "system": "You are an elite code auditor. Your tone is professional, concise, and technical. Focus on high-impact feedback."
    }
    
    req = urllib.request.Request(url, data=json.dumps(data).encode())
    req.add_header("x-api-key", anthropic_key)
    req.add_header("anthropic-version", "2023-06-01")
    req.add_header("content-type", "application/json")
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            return result['content'][0]['text']
    except urllib.error.HTTPError as e:
        return f"AI Analysis Failed: {e.read().decode()}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 review-pr.py <PR_URL>")
        sys.exit(1)
        
    pr_url = sys.argv[1]
    github_token = os.getenv("GITHUB_TOKEN")
    anthropic_key = ""
    
    if not github_token or not anthropic_key:
        print("Error: GITHUB_TOKEN and ANTHROPIC_API_KEY environment variables are required.")
        sys.exit(1)
        
    try:
        print(f"Fetching PR data for {pr_url}...")
        metadata, diff = get_pr_data(pr_url, github_token)
        
        print("Performing AI Audit...")
        review_text = review_with_claude(metadata, diff, anthropic_key)
        
        print("\n--- AI CODE REVIEW REPORT ---")
        print(review_text)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
