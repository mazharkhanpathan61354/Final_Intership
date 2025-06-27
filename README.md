🔐 Password Strength Analyzer with Custom Wordlist Generator

This project evaluates the strength of user passwords and generates custom wordlists based on personal inputs for password cracking simulations.

💡 Features
- Password strength scoring using `zxcvbn`
- Suggests improvements for weak passwords
- Generates wordlists with leetspeak, years, and common patterns
- Saves to `custom_wordlist.txt`
- Command-line interface (CLI)

 🛠 Tools & Libraries
- Python 3.x
- [zxcvbn](https://github.com/dropbox/zxcvbn)
- argparse

## 🚀 How to Use

1. Evaluate Password Strength**
```bash
python password_analyzer.py --password MyP@ssw0rd123
