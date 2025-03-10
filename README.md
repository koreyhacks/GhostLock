# GhostLock Ransomware Simulator

![GhostLock](https://img.shields.io/badge/GhostLock-v1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.6%2B-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Purpose](https://img.shields.io/badge/Purpose-Educational-red)

## 👻 Overview

GhostLock is an educational ransomware simulator designed for security professionals, penetration testers, and educational purposes. It safely demonstrates how ransomware behaves without causing actual harm to your files.

> ⚠️ **DISCLAIMER:** This tool is intended for EDUCATIONAL PURPOSES ONLY. Do not use this tool maliciously or on any systems without proper authorization.

## 🔐 Features

- **Safe Mode Operation:** By default, GhostLock runs in safe mode, only logging what would happen without modifying any files
- **Visual Feedback:** Animated Mario-style ghost characters provide visual feedback during scanning and encryption simulation
- **Targeted File Extensions:** Configurable list of file extensions to target
- **Detailed Logging:** Comprehensive logging of all simulated actions
- **Cleanup Function:** Built-in ability to remove simulation artifacts
- **Educational Ransom Note:** Displays information about what would happen in a real attack

## 🛠️ Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/ghostlock.git
cd ghostlock
```

2. No external dependencies required - GhostLock uses only Python standard libraries

## 🚀 Usage

### Basic Usage

Run in safe mode (default - no files are modified):
```bash
python ghostlock.py --target-dir /path/to/test/directory
```

Run in simulation mode (creates marker files but doesn't modify originals):
```bash
python ghostlock.py --target-dir /path/to/test/directory --simulate
```

### Safety Features

For your protection, GhostLock includes several safety measures:
- Safe mode is enabled by default (no file modifications)
- Explicit confirmation is required to run
- Clear visual indicators show that it's a simulation

### Command-line Options

```
--target-dir    Required. Directory to simulate on
--safe-mode     Run in safe mode (default: True)
--simulate      Run in simulation mode (creates marker files)
--extensions    File extensions to target (default: .txt .docx .xlsx .pdf .jpg .png)
--log-file      Path to log file
--cleanup       Clean up simulation artifacts from previous runs
```

## 📊 Educational Value

GhostLock demonstrates several techniques used by actual ransomware:
- File enumeration
- Extension filtering
- Simulated encryption
- Ransom notification
- File marking

## 🖼️ Screenshots

```
  ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓ ██▓     ▒█████   ▄████▄   ██ ▄█▀
 ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒ 
▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░ 
░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ ▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄ 
░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄
 ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    ░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░
░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░        ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░ 
      ░  ░  ░  ░    ░ ░        ░               ░  ░    ░ ░  ░ ░      ░  ░   
                                                          ░                  
```

## 🔍 How It Works

1. **Scanning Phase:** GhostLock scans the target directory for files matching the specified extensions
2. **Simulation Phase:** In simulation mode, it creates small marker files to represent "encrypted" files
3. **Notification Phase:** Displays a ransom note showing what would happen in a real attack
4. **Cleanup Phase:** Optionally removes all simulation artifacts

## 👨‍💻 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## 🙏 Credits

- Created by koreyhacks_
- Mario-style ghost animations inspired by Super Mario Bros.

## 🔗 Contact

For questions, feedback, or suggestions, please open an issue on GitHub.

---

*Remember: This tool is for educational purposes only. Always use responsibly and ethically.*
