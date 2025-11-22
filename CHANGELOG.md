    # Changelog

All notable changes to this project will be documented in this file.

Initialized project repo and added pseudocode file.

Added README.md with project overview, run instructions, and structure.

Created DESIGN.md describing architecture, data structures, user flow.

Created USER_STORIES.md with stories and acceptance criteria.

Added LICENSE (MIT).

Added CHANGELOG.md and seeded it.

Added .github/workflows/ci.yml (GitHub Actions workflow to run pytest).

Added tests/ placeholders and implemented tests/test_cart.py.

Implemented cart.py (Cart class) and fixed circular import.

Added menu.json and module files (menu.py, coffee_app.py) and began modularizing the app.

Fixed .gitignore and removed __pycache__ artifacts.

Ran pytest locally — unit test for Cart passes.

Pushed changes to GitHub (some pushes rejected earlier due to PAT workflow scope; later fixed).

Created boilerplate plan / started template discussion (template repo task added to checklist).


## [Unreleased]
- Add GitHub Actions CI workflow (pytest) — CI configured but first run failing (see Actions tab).
- Add tests/ placeholders and unit tests (tests/test_cart.py) — initial unit test added.
- Prepare boilerplate-template plan for reuse across projects.

## [0.1.0] - 2025-11-22
### Added
- Implemented Cart class (cart.py) with add/remove/update/total/summary methods.
- Added passing unit test for Cart total calculation (tests/test_cart.py).
- Added .gitignore to exclude Python cache files.

## [0.0.3] - 2025-11-21
### Added
- Added `menu.py` (menu loader/display/find) and `menu.json` sample data.
- Updated coffee_app.py to use modular menu and cart modules (basic CLI loop).
- Fixed circular import and corrected tests.

## [0.0.2] - 2025-11-20
### Added
- Added DESIGN.md (architecture, data structures, user flow).
- Added USER_STORIES.md (stories + acceptance criteria).
- Added LICENSE (MIT) and README updates.

## [0.1.0] - 2025-11-18 

## Added

* Initialized project structure
* Added README.md, DESIGN.md, USER_STORIES.md
* Created menu.json storage file
* Started coffee_app.py (main application driver)
