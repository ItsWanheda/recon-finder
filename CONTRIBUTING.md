# Contributing to Recon-Finder

Thank you for your interest in contributing to **Recon-Finder**.

Recon-Finder is a small Python reconnaissance project, and contributions are welcome as long as they remain aligned with the project's purpose: **authorized, non-destructive security reconnaissance**.

---

## 📋 Before You Start

Before submitting a contribution:

* Read the `README.md`.
* Review the project's security policy.
* Make sure your changes have a clear purpose.
* Keep the implementation simple and maintainable.
* Avoid unnecessary dependencies.
* Do not introduce offensive or destructive functionality.

For security-sensitive changes, review `SECURITY.md` before opening a pull request.

---

## 🛠️ Development Setup

Clone the repository:

```bash
git clone https://github.com/ItsWanheda/recon-finder.git
cd recon-finder
```

Create a virtual environment.

### Windows

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the development dependencies:

```bash
py -m pip install -e ".[dev]"
```

---

## 🧪 Running Tests

Run the complete test suite:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_scanner.py -v
```

New functionality should include appropriate tests.

Avoid tests that require access to external systems or real targets.

Mock network requests whenever possible.

---

## 📁 Project Structure

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
├── SECURITY.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── pyproject.toml
└── requirements.txt
```

---

## ✨ Adding Features

When adding a feature:

1. Keep the change focused.
2. Follow the existing project structure.
3. Prefer small functions and clear interfaces.
4. Add tests.
5. Update documentation when necessary.
6. Make sure existing tests still pass.

For example:

```text
Feature
   │
   ├── Implementation
   ├── Tests
   └── Documentation
```

---

## 🧹 Code Style

Please keep Python code:

* Readable
* Explicit
* Modular
* PEP 8 compatible
* Type-annotated where practical
* Free from unnecessary complexity

Prefer descriptive names:

```python
timeout_seconds
```

instead of:

```python
t
```

Keep functions focused on a single responsibility.

---

## 📦 Dependencies

Avoid adding dependencies unless they provide meaningful value.

Before adding a dependency, consider:

* Is the functionality already available in the standard library?
* Is the dependency actively maintained?
* Does it introduce unnecessary security risk?
* Does it significantly increase project complexity?

Update dependency documentation when adding or removing packages.

---

## 🔒 Security Contributions

Do not contribute functionality intended to:

* Exploit vulnerabilities
* Bypass authentication
* Steal credentials
* Deploy malware
* Execute arbitrary commands against targets
* Destroy or modify remote systems
* Evade security controls

Recon-Finder should remain focused on **authorized discovery and enumeration**.

If you discover a vulnerability in the existing project, follow `SECURITY.md` instead of opening a public issue with sensitive details.

---

## 🌿 Branching

Create a descriptive branch for your work:

```bash
git checkout -b feature/json-output
```

Examples:

```text
feature/concurrent-scanning
feature/json-output
fix/url-validation
docs/update-installation
test/scanner-errors
```

---

## 💬 Commit Messages

Use clear and descriptive commit messages.

Examples:

```bash
git commit -m "feat: add JSON result output"
```

```bash
git commit -m "fix: handle malformed target URLs"
```

```bash
git commit -m "test: add scanner timeout coverage"
```

```bash
git commit -m "docs: improve installation instructions"
```

---

## 🔀 Pull Requests

Before opening a pull request:

```bash
pytest -v
```

Make sure:

* Tests pass.
* New functionality is tested.
* Documentation is updated where necessary.
* No secrets are committed.
* No unrelated changes are included.
* The pull request has a clear description.

A good pull request should explain:

### What changed?

Briefly describe the implementation.

### Why?

Explain the problem or use case.

### Testing

Describe how the change was tested.

---

## 🐛 Bug Reports

When reporting a bug, include:

* Recon-Finder version
* Python version
* Operating system
* Command used
* Expected behavior
* Actual behavior
* Relevant error output
* Minimal reproduction steps

Remove credentials, API keys, tokens, and other sensitive information before posting.

---

## 💡 Feature Requests

Feature requests are welcome.

Please explain:

* What problem the feature solves
* How you expect it to work
* Why it fits Recon-Finder
* Any relevant security considerations

Keep proposals consistent with the project's reconnaissance-focused scope.

---

## 🤝 Code of Conduct

By participating in the project, you agree to follow the rules described in [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

Be respectful, constructive, and professional.

---

## 📄 License

By contributing code to Recon-Finder, you agree that your contributions will be released under the project's **MIT License**.

---

## 🙏 Thank You

Every contribution helps improve Recon-Finder.

Whether you're fixing a typo, adding a test, improving documentation, or implementing a feature, thank you for taking the time to contribute.
