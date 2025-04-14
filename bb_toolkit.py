#!/usr/bin/env python3
#
# ______  ______  _______  _____   _____         _______
# |_____] |_____]    |    |     | |     | |      |______
# |_____] |_____]    |    |_____| |_____| |_____ ______|
#   Bug Bounty Toolkit Installer & Updater
#   https://github.com/archangelneo18/bb_toolkit
import os
import subprocess
from pathlib import Path

# === Configuration ===
TOOLS_DIR = Path.home() / "BB/tools"
SCRIPTS_DIR = TOOLS_DIR / "scripts"
GIT_CLONE_DIR = SCRIPTS_DIR / "git-clones"
SECLISTS_DIR = TOOLS_DIR / "SecLists"
PYTHON_INSTALL_CMD = "pip3 install --break-system-packages"

BREW_TOOLS = [
    "amass", "gf", "nuclei", "subfinder", "httpx", "ffuf", "waybackpy", "xray"
]

PIP_TOOLS = [
    "arjun", "dmut", "dalfox", "git+https://github.com/devanshbatham/ParamSpider.git",
    "git+https://github.com/s0md3v/uro.git"
]

GIT_TOOLS = {
    "Arjun": "https://github.com/s0md3v/Arjun.git",
    "kxss": "https://github.com/takshal/fuzzuli.git",  # Re-check if updated
    "JSFScan": "https://github.com/KathanP19/JSFScan.sh.git",
    "XSStrike": "https://github.com/s0md3v/XSStrike.git"
}

ALIASES = {
    "bbupdate": f"python3 {SCRIPTS_DIR}/bb_toolkit.py update"
}


# === Helpers ===
def run(cmd):
    print(f"[+] Running: {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Command failed: {cmd}\n    {e}")


def install_brew_tools():
    for tool in BREW_TOOLS:
        run(f"brew list {tool} || brew install {tool} || brew upgrade {tool}")


def install_pip_tools():
    for tool in PIP_TOOLS:
        run(f"{PYTHON_INSTALL_CMD} {tool}")


def clone_tools():
    GIT_CLONE_DIR.mkdir(parents=True, exist_ok=True)
    for name, url in GIT_TOOLS.items():
        dest = GIT_CLONE_DIR / name
        if not dest.exists():
            run(f"git clone {url} {dest}")
        else:
            print(f"[=] Skipping {name} (already cloned)")


def create_aliases():
    zshrc = Path.home() / ".zshrc"
    for name, cmd in ALIASES.items():
        alias_line = f"alias {name}='{cmd}'\n"
        with zshrc.open("a") as f:
            f.write(f"\n# Added by bb_toolkit\n{alias_line}")
    print("[+] Alias added to .zshrc. Run `source ~/.zshrc` to activate.")


def update_tools():
    print("\n🔄 Updating tools...\n")
    run("brew update && brew upgrade")
    run(f"{PYTHON_INSTALL_CMD} --upgrade pip setuptools wheel")
    for tool in PIP_TOOLS:
        run(f"{PYTHON_INSTALL_CMD} --upgrade {tool}")
    for tool_path in GIT_CLONE_DIR.glob("*"):
        if (tool_path / ".git").exists():
            run(f"git -C {tool_path} pull")


# === Main ===
def main():
    os.makedirs(SCRIPTS_DIR, exist_ok=True)

    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "update":
        update_tools()
        return

    install_brew_tools()
    install_pip_tools()
    clone_tools()
    create_aliases()
    print("\n✅ All tools installed and aliases created!\n")


if __name__ == "__main__":
    main()
