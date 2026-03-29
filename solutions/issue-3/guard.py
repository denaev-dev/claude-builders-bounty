import sys
import json
import shlex
import os
import shutil

# Destructive patterns to block
DESTRUCTIVE_BINARIES = {'rm', 'drop', 'truncate', 'delete'}
DANGEROUS_FLAGS = {'-rf', '-fr', '--recursive', '--force'}

def block(reason):
    print(f"SECURITY BLOCK: {reason}", file=sys.stderr)
    sys.exit(2)

def install_hook():
    """Automated installer for Claude Code global settings."""
    home = os.path.expanduser("~")
    hooks_dir = os.path.join(home, ".claude", "hooks")
    settings_path = os.path.join(home, ".claude", "settings.json")
    
    os.makedirs(hooks_dir, exist_ok=True)
    target_path = os.path.abspath(__file__)
    
    # Update settings.json
    settings = {}
    if os.path.exists(settings_path):
        with open(settings_path, 'r') as f:
            try:
                settings = json.load(f)
            except json.JSONDecodeError:
                settings = {}

    hooks = settings.get("hooks", {})
    pre_tool = hooks.get("PreToolUse", [])
    
    # Check if already installed
    if any(h.get("hooks", [{}])[0].get("command", "").endswith("guard.py") for h in pre_tool):
        print("Hook already installed.")
        return

    new_hook = {
        "matcher": "Bash",
        "hooks": [{"type": "command", "command": f"python3 {target_path}"}]
    }
    pre_tool.append(new_hook)
    hooks["PreToolUse"] = pre_tool
    settings["hooks"] = hooks

    with open(settings_path, 'w') as f:
        json.dump(settings, f, indent=2)
    
    print(f"Successfully installed hook to {settings_path}")

def analyze_command(command):
    try:
        tokens = shlex.split(command)
        if not tokens:
            return
        
        binary = tokens[0].lower()
        
        # 1. Check for rm -rf variants
        if binary == 'rm':
            if any(flag in tokens for flag in DANGEROUS_FLAGS):
                block("Recursive force deletion (rm -rf) is prohibited.")
        
        # 2. Check for SQL destruction (simplified)
        cmd_upper = command.upper()
        if "DROP TABLE" in cmd_upper or "DROP DATABASE" in cmd_upper:
            block("Database destruction (DROP) is prohibited.")
        if "TRUNCATE" in cmd_upper:
            block("Table truncation is prohibited.")
        if "DELETE FROM" in cmd_upper and "WHERE" not in cmd_upper:
            block("Bulk deletion without WHERE clause is prohibited.")
            
        # 3. Check for git force push
        if binary == 'git' and 'push' in tokens:
            if '--force' in tokens or '-f' in tokens:
                if '--force-with-lease' not in tokens:
                    block("Standard force push is prohibited. Use --force-with-lease.")

        # 4. Check for insecure permissions
        if binary == 'chmod' and '777' in tokens:
            block("Insecure permissions (chmod 777) are prohibited.")

    except ValueError:
        # If shlex fails (unclosed quotes), it's a suspicious command
        block("Malformed shell command detected.")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--install":
        install_hook()
        return

    try:
        data = sys.stdin.read()
        if not data:
            sys.exit(0)
        
        payload = json.loads(data)
        if payload.get("tool_name") == "Bash":
            command = payload.get("tool_input", {}).get("command", "")
            analyze_command(command)
            
    except Exception:
        # Fail-open on hook internal error to avoid locking the user
        sys.exit(0)

if __name__ == "__main__":
    main()
