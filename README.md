# 🔐 Secure Password Generator & Leak Checker

This Python script helps you:

- ✅ Generate strong, random passwords
- ✅ Analyze password strength (length, character variety)
- ✅ Check if a password has been exposed in known data breaches (using [Have I Been Pwned](https://haveibeenpwned.com/))

---

## 🚀 Features

- **Secure password generation** using Python's `secrets` module
- **Strength analysis** based on:
  - Length
  - Uppercase
  - Lowercase
  - Digits
  - Special characters
- **Breach check** using [Pwned Passwords API](https://haveibeenpwned.com/API/v3#PwnedPasswords)

---

## 📦 Requirements

- Python 3.6+
- `requests` library

Install dependencies:

```bash
pip install requests
