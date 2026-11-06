# Implementation

The primary language is Python. Core logic lives in `app.py` and is separated from the interaction/command interface where practical.



## Checks

The repository tests exercise the domain algorithm with valid examples and invalid/boundary cases. CI uses synthetic fixtures and does not start paid services or connect to user accounts. See `README.md` and `.github/workflows/ci.yml` for exact commands.

## Extending the project

Add format support or new operations with corresponding tests. Preserve validation and explicit format boundaries. Keep generated data and secrets outside source control.
