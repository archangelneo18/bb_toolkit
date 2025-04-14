#!/usr/bin/env python3
 # ______  ______  _______  _____   _____         _______      _______ _     _ _______  _____   ______ _______ _______  _____  __   _
 # |_____] |_____]    |    |     | |     | |      |______      |_____| |     |    |    |     | |_____/ |______ |       |     | | \  |
 # |_____] |_____]    |    |_____| |_____| |_____ ______|      |     | |_____|    |    |_____| |    \_ |______ |_____  |_____| |  \_|
                                                                                                                                   
import argparse
import os
import subprocess
import datetime
import requests

# Configurations
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TOOL_OUTPUT_DIR = os.path.join(SCRIPT_DIR, "recon_results")
DISCORD_WEBHOOK = "YOUR_DISCORD_WEBHOOK_HERE"  # Optional: Replace or set via env var
SECLISTS_DIR = os.path.expanduser("~/BB/tools/SecLists")  # Default SecLists path

# Tools and commands
TOOLS = {
    "subfinder": lambda target: f"subfinder -d {target} -silent",
    "httpx": lambda target: f"echo {target} | httpx -silent",
    "hakrawler": lambda target: f"echo {target} | hakrawler -d 2 -subs -u -timeout 10",
    "ffuf": lambda target: f"ffuf -u {target}/FUZZ -w {SECLISTS_DIR}/Discovery/Web-Content/raft-small-words.txt -mc 200,403 -t 50 -of json",
    "nuclei": lambda target: f"echo {target} | nuclei -t cves/ -t misconfiguration/ -t vulnerabilities/ -silent",
}

# Send Discord notification

def notify_discord(message):
    if not DISCORD_WEBHOOK:
        return
    try:
        requests.post(DISCORD_WEBHOOK, data={"content": message})
    except Exception as e:
        print(f"[!] Failed to notify Discord: {e}")

# Run tool and save results

def run_tool(name, command, output_path):
    print(f"[+] Running {name}...")
    notify_discord(f"🛠 Running `{name}` on target.")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        with open(output_path, 'w') as f:
            f.write(result.stdout)
        notify_discord(f"✅ `{name}` completed. Output saved to `{output_path}`.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error running {name}: {e.stderr}")
        notify_discord(f"❌ `{name}` failed: {e.stderr.strip()[:200]}")

# Main automation logic

def main(target):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    target_dir = os.path.join(TOOL_OUTPUT_DIR, f"{target.replace('.', '_')}_{timestamp}")
    os.makedirs(target_dir, exist_ok=True)

    notify_discord(f"🚀 Starting automated recon on `{target}`")
    for tool, command_fn in TOOLS.items():
        output_file = os.path.join(target_dir, f"{tool}.txt")
        run_tool(tool, command_fn(target), output_file)
    notify_discord(f"🎯 Recon on `{target}` complete! Results in `{target_dir}`")

# Argument parser
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate bb_toolkit scanning on a target.")
    parser.add_argument("target", help="Domain or URL to scan")
    args = parser.parse_args()
    main(args.target)
