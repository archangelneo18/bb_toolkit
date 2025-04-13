# 🛠️ bb_toolkit

Welcome to **bb_toolkit** — your all-in-one, bug bounty power-up script for recon, automation, and chaos (the good kind 😎). Whether you’re new to bug bounty or a seasoned hunter building your ultimate recon machine, this toolkit helps you install, organize, and update all the tools you need, painlessly.

> “Why do things manually when you can automate them like a legend?”

---

## 🚀 What is `bb_toolkit`?

`bb_toolkit.py` is a **massive Python script** that installs, manages, and updates your bug bounty tooling stack. It combines tools from **Homebrew**, **Go**, **GitHub**, and **pip** to build a reliable recon environment for macOS (optimized for M1/M2/M3 Macs using Homebrew).

It’s designed to be:

- **Easy to use** (run it, grab coffee ☕)
- **Fully automated** (less typing, more hacking)
- **Discord-friendly** (optional status reports via webhook)
- **Expandable** (built for the long recon grind)

---

## 🧰 What It Does

- Installs tools from:
  - 🧪 `brew` (like `httpx`, `ffuf`, `nuclei`, `amass`, `gf`)
  - 🦫 `go install` (for those sweet CLI tools)
  - 🧬 `pip3` with `--break-system-packages` (for macOS compatibility)
  - 🧪 `git clone` for tools that don’t come in a box

- Creates helpful **aliases** for your `.zshrc` so you can run scripts from anywhere
- Detects and skips tools you already have (unless you’re updating)
- Keeps your setup tidy and contained inside `~/BB/tools`
- Provides **update mode** to refresh everything in one go (`python3 bb_toolkit.py update`)
- Built with ❤️ for bug bounty hunters

---

## 🗃️ Project Structure

```bash
BB/
├── tools/                  # Where all tools and SecLists live
│   ├── scripts/            # Where bb_toolkit.py lives
│   ├── git-clones/         # Cloned GitHub repos
│   └── SecLists/           # Wordlists and payloads (non-Homebrew)
├── H1/                     # Folder for HackerOne programs
├── Bugcrowd/               # Folder for Bugcrowd programs
└── README.md
