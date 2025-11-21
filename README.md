# ☕ Coffee App

![CI](https://github.com/joanita-cygnusX-1/coffee_app/actions/workflows/ci.yml/badge.svg)

A simple Python CLI coffee-ordering app used to learn backend design patterns, modular code organization, testing, and CI.

---

## Project Overview
This project demonstrates:
- Modular design (`menu.py`, `cart.py`, `coffee_app.py`)
- Clear developer artifacts (`README.md`, `DESIGN.md`, `USER_STORIES.md`, `CHANGELOG.md`)
- A small JSON-backed data store (`menu.json`) for quick local development
- Unit testing with `pytest` and CI using GitHub Actions

---

## Quick Start (run locally)
1. Clone repository:
```bash
git clone https://github.com/joanita-cygnusX-1/coffee_app.git
cd coffee_app


Project Structure
coffee_app/
├─ coffee_app.py    # CLI entrypoint (uses modules)
├─ cart.py          # Cart class and methods
├─ menu.py          # menu load/display/find helper functions
├─ menu.json        # sample data
├─ coffee_pseudocode.txt
├─ USER_STORIES.md
├─ DESIGN.md
├─ CHANGELOG.md
├─ README.md
└─ LICENSE

Documentation

Design: DESIGN.md — architecture, flow, data structures, and future scaling notes.

User stories: USER_STORIES.md — acceptance criteria used to guide development.

Pseudocode: coffee_pseudocode.txt — developer planning and logic.

Changelog: CHANGELOG.md — project history & version notes.

CI / Tests

This repo uses GitHub Actions to run pytest on every push (see .github/workflows/ci.yml).
Add tests under tests/ (e.g., tests/test_cart.py) and they will be executed automatically.

Future Enhancements

Convert CLI to FastAPI backend (REST endpoints)

Persist data in SQLite/Postgres and add migrations

Add authentication & sessions

Add PDF/email receipts and a demo video/screenshots

Add GitHub Actions CI badge after first successful run

Author

Joanita Nyashanu — joanita-cygnusX-1
Copyright (c) 2025 Joanita Nyashanu


---

## 2) **CHANGELOG.md** (copy & paste)
```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
- Add modular code: `menu.py`, `cart.py`, `coffee_app.py`
- Add `DESIGN.md`, `USER_STORIES.md`, `CHANGELOG.md`
- Add basic GitHub Actions CI for pytest

## [2025-11-20] - Initial commit
- Project created with pseudocode, README, and menu sample
