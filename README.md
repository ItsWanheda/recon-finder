# 🔎 Recon-Finder

> **Simple HTTP reconnaissance & file discovery tool written in Python.**

Recon-Finder is a lightweight command-line tool for discovering common files, directories, and endpoints on web applications during **authorized security assessments**.

It uses a customizable wordlist and HTTP requests to identify accessible resources and reports useful response information such as status codes, response size, and request time.

---

## ✨ Features

* 🔍 HTTP path and file discovery
* 📝 Custom wordlist support
* 🌐 HTTP and HTTPS targets
* 📊 HTTP status code detection
* 📦 Response size reporting
* ⏱️ Request timing
* 🚦 Redirect detection
* 🔐 Authentication/authorization response detection
* 🎨 Rich terminal output
* ⚡ Lightweight and dependency-minimal
* 🧩 Modular Python architecture
* 🧪 Testable scanner implementation

---

## ⚠️ Legal Notice

Recon-Finder is intended for **authorized security testing, research, and educational purposes only**.

Only scan systems that you own or have explicit permission to assess.

Unauthorized scanning or reconnaissance may violate laws, regulations, contracts, or the target's terms of service.

The author is not responsible for misuse of this software.

---

## Example

```text
RECON-FINDER v0.1.0
Target: https://example.com
Wordlist: wordlists/common.txt

[200] https://example.com/robots.txt (142 bytes, 0.18s)
[200] https://example.com/sitemap.xml (834 bytes, 0.21s)
[301] https://example.com/admin (0 bytes, 0.16s)
[403] https://example.com/.well-known (287 bytes, 0.19s)

             Scan Summary
┏━━━━━━━━━━┳━━━━━━━┳━━━━━━━━┓
┃ Requests ┃ Found ┃ Errors ┃
┡━━━━━━━━━━╇━━━━━━━╇━━━━━━━━┩
│ 14       │ 4     │ 0      │
└──────────┴───────┴────────┘
```

---

## 📋 Requirements

* Python **3.9+**
* `requests`
* `rich`

For development:

* `pytest`

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/ItsWanheda/recon-finder.git
cd recon-finder
```

### Create a virtual environment

#### Windows

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
py -m pip install -r requirements.txt
```

### Install Recon-Finder

```bash
py -m pip install -e .
```

---

## 🛠️ Usage

### Basic scan

```bash
recon-finder https://example.com
```

Or:

```bash
py -m recon_finder https://example.com
```

### Custom wordlist

```bash
recon-finder https://example.com \
    --wordlist wordlists/common.txt
```

Windows PowerShell:

```powershell
recon-finder https://example.com `
    --wordlist wordlists/common.txt
```

### Custom timeout

```bash
recon-finder https://example.com --timeout 10
```

### Display version

```bash
recon-finder --version
```

---

## 📚 Wordlists

The default wordlist is:

```text
wordlists/common.txt
```

Example:

```text
admin
login
api
robots.txt
sitemap.xml
uploads
assets
static
backup
backups
config
docs
api/v1
.well-known
```

You can create your own:

```text
admin
dashboard
portal
api
api/v1
api/v2
uploads
files
docs
backup
```

Then scan with:

```bash
recon-finder https://example.com -w my-wordlist.txt
```

---

## 📊 HTTP Status Codes

Recon-Finder reports the HTTP status returned by each request.

| Status | Meaning                 |
| -----: | ----------------------- |
|  `200` | Resource available      |
|  `3xx` | Redirect                |
|  `401` | Authentication required |
|  `403` | Access forbidden        |
|  `404` | Resource not found      |
|  `5xx` | Server-side error       |

A response other than `404` is treated as potentially interesting by the initial discovery engine.

---

## 🏗️ Project Structure

```text
recon-finder/
│
├── src/
│   └── recon_finder/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── scanner.py
│       └── results.py
│
├── tests/
│   └── test_scanner.py
│
├── wordlists/
│   └── common.txt
│
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

## 🧩 Architecture

Recon-Finder separates responsibilities into small modules.

### `scanner.py`

Handles:

* HTTP requests
* Target URLs
* Wordlist processing
* Timeout handling
* Response collection

### `results.py`

Defines the scan result model:

```python
ScanResult
```

It stores:

* URL
* HTTP status
* response size
* request duration
* errors

### `cli.py`

Handles:

* Command-line arguments
* Input validation
* Terminal output
* Scan summaries

### `__main__.py`

Provides:

```bash
python -m recon_finder
```

support.

---

## 🧪 Testing

Run the test suite with:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

---

## 🔧 Development

Clone the repository:

```bash
git clone https://github.com/ItsWanheda/recon-finder.git
cd recon-finder
```

Create a development environment:

```bash
py -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install development dependencies:

```bash
py -m pip install -e ".[dev]"
```

Run:

```bash
py -m recon_finder https://example.com
```

---

## 🗺️ Roadmap

### v0.1.0 — Initial Release

* [x] HTTP discovery
* [x] HTTPS support
* [x] Custom wordlists
* [x] Status code detection
* [x] Response size
* [x] Request timing
* [x] Rich terminal output
* [x] Basic error handling
* [x] Modular architecture

### v0.2.0

* [ ] Concurrent requests
* [ ] Configurable thread count
* [ ] Status-code filtering
* [ ] Response-size filtering
* [ ] JSON output
* [ ] Better progress display

### v0.3.0

* [ ] Recursive discovery
* [ ] File-extension discovery
* [ ] Duplicate response detection
* [ ] Soft-404 detection
* [ ] Improved result filtering

### v0.4.0

* [ ] `robots.txt` parsing
* [ ] `sitemap.xml` parsing
* [ ] Link discovery
* [ ] Header analysis
* [ ] Technology hints

---

## 🔒 Security Philosophy

Recon-Finder is intentionally focused on **discovery rather than exploitation**.

The tool does not attempt to:

* Exploit discovered endpoints
* Bypass authentication
* Brute-force credentials
* Modify discovered resources
* Execute commands on remote systems
* Deploy payloads

Its purpose is to provide a small and understandable foundation for web reconnaissance tooling.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/my-feature
```

3. Make your changes.
4. Run the tests.

```bash
pytest -v
```

5. Commit your changes.

```bash
git commit -m "feat: add my feature"
```

6. Push your branch.

```bash
git push origin feature/my-feature
```

7. Open a pull request.

Please keep contributions focused, documented, and compatible with the project's authorized-security-testing purpose.

---

## 📄 License

Recon-Finder is released under the **MIT License**.

See [`LICENSE`](LICENSE) for the full license text.

---

## 👤 Author

**ItsWanheda**

GitHub: `https://github.com/ItsWanheda`

---

<div align="center">

**Recon-Finder**

`DISCOVER • ENUMERATE • UNDERSTAND`

Made for authorized security research.

</div>
