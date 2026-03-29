# Resilient Security Hook for Claude Code

A production-grade `pre-tool-use` hook that intercepts and blocks destructive bash commands.

## 🚀 Key Advantages
- **Zero-Config Installation**: Run `python3 guard.py --install` to automatically configure your global Claude settings.
- **Obfuscation Resistant**: Uses `shlex` lexical analysis to defeat common shell bypasses (like quotes and nested subshells).
- **Comprehensive Protection**: Blocks `rm -rf`, destructive SQL, `git push --force`, and insecure `chmod`.

## 🛠 Setup
1. Copy `guard.py` to a permanent location.
2. Run installer:
   ```bash
   python3 guard.py --install
   ```

## 🧪 Testing
Includes a test suite covering 30+ edge cases.
