# bb\_toolkit

> One toolkit to rule them all. Automated installation, updating, and recon for your bug bounty hustle. Built for macOS, built for bounty hunters, built for **you**.

## 🤘 What Is This?

`bb_toolkit.py` is your personal bug bounty Swiss Army knife. It's a Python-powered automation script that:

- Installs and updates dozens of bug bounty tools
- Clones or pulls repos from GitHub if brew can't handle it
- Sets up easy-to-use aliases so you can run stuff from anywhere
- Handles wordlists and tool separation like a champ (Homebrew vs GitHub)
- Sends updates to your Discord channel (because why not?)

All designed to keep your recon sharp and your flow smooth.

---


## 🧰 Tools Included

### 🔍 Recon & Subdomain Discovery
- `amass`
- `subfinder`
- `assetfinder` *(requires manual install)*
- `httpx`
- `waybackurls` *(consider replacing with `waybackpy`)*

### 🕷️ Crawling & URL Gathering
- `hakrawler`
- `ffuf`
- `gau`
- `arjun`
- `xnLinkFinder`
- `urlhunter`

### 🚨 Vulnerability Scanners
- `nuclei` (with community templates)
- `dalfox`
- `kiterunner`

### 🧠 Pattern Matching & Payloads
- `gf` (Good Finds)
- `qsreplace` *(may require manual install)*

### ⚙️ Miscellaneous Tools
- `xray`
- `whatweb` *(Ruby@2.3 dependency – manual workaround needed)*
- `dirsearch`
- `unfurl`
- `waymore`
- `CRLFsuite`
- `bypass-403`

> ⚠️ Some tools may need extra setup or Python deps. We use `--break-system-packages` for pip3 to help with Homebrew Python.

---

## 📁 File Structure (Recommended)

```bash
~/BB/               # Your main Bug Bounty directory
├── tools/          # Tools that can't be installed via Homebrew
│   └── scripts/    # bb_toolkit.py lives here
│   └── SecLists/   # Wordlists live here
├── H1/             # HackerOne targets
├── Bugcrowd/       # Bugcrowd targets
└── ReconResults/   # Output results go here (automatically generated)
```

---

## 🚀 Usage

```bash
python3 bb_toolkit.py [install|update]
```

### Example:

```bash
python3 bb_toolkit.py install
```

Installs all the tools in the script.

```bash
python3 bb_toolkit.py update
```

Updates everything you've already installed.

### Want global access?

Add this to your `.zshrc`:

```bash
alias bbtool='python3 ~/BB/tools/scripts/bb_toolkit.py'
```

Then just run:

```bash
bbtool install
```

From anywhere 💥

---

## 🔔 Discord Notifications

The toolkit sends messages to your Discord via webhook:

- Status updates while installing
- Errors if something goes wrong
- Success messages when things are done

Set your webhook in the script like so:

```python
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/...."
```

---

## 🛡️ License

MIT for the `bb_toolkit.py` script itself.

Third-party tools installed by this script retain **their own licenses**, which may include MIT, Apache 2.0, GPL, or others. Please check each tool's repo individually for specifics.

---

## ❤️ Credits
- **Author**: [@archangelneo18](https://github.com/archangelneo18) — U.S. Army Veteran and bug bounty hunter

Massive shoutout to:

- - [ProjectDiscovery](https://github.com/projectdiscovery)
- - [TomNomNom](https://github.com/tomnomnom)
- - [vavkamil](https://github.com/vavkamil/awesome-bugbounty-tools)
- - You, the hacker, for pushing boundaries
- **Built for**: The bug bounty community to streamline setup and recon

---
## 👨‍💻 Contributors

Security is a shared responsibility. Please:

- Keep your GitHub account secure
- Enable 2FA on your GitHub account
- Don’t push secrets or tokens — use `.env` and `.gitignore`

---

## 💬 Final Word

Bug bounty can be overwhelming. Tooling shouldn't be. Let `bb_toolkit` be your assistant while you focus on hunting 🔍

Now get out there and hack something. 🐞💰

