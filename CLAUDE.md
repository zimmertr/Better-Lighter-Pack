# Better-Lighter-Pack

A CLI that reads LighterPack CSV exports and prints counts, weight and cost totals per trip. Start with [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

This repo took a trimmed set of the files a new project starts with (zimmertr/yggdrasil record 0038). When a change here makes a decision, write its record under `docs/architectural-decision-records/`; when it needs a page `docs/` doesn't have yet, add it in the same PR. The issue templates and security policy come from the account's shared `.github` repo (zimmertr/yggdrasil record 0041), so this repo has none of its own.

## Documentation

A change that makes any page untrue updates it in the same PR. The README is TJ's: keep it accurate and in his voice, and never restructure it.

| Doc | Holds |
|---|---|
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | What `main.py` reads and prints, and the Dockerfile |
| [`docs/CICD.md`](docs/CICD.md) | What CI runs on a PR, the release to GHCR, and how Dependabot updates merge |

## Rules

- Run everything in Docker, as [`README.md`](README.md) shows. Nothing installs on the workstation.
- The Dockerfile's `FROM` carries a tag and a digest; Dependabot moves both together.
- Every merge to `main` releases `ghcr.io/zimmertr/better-lighter-pack`, and the PR title sets the version bump.
- There are no tests yet.

## Issues

File issues with the `create-issue` skill from zimmertr/ai-config: the two-sentence summary, the six sections, the hemingway and humanizer passes, one priority, one type, the area labels and the session label. The skill reads the four things below from this section.

- **The reader**: TJ, who wrote the script and uses it to plan backpacking trips.
- **The gates**: `PR Title / PR Title`, the three `Lint /` checks and `Docker Build / Docker Build` pass; the `docs/` page that owns the topic changes in the same PR; the README changes only to stay accurate.
- **The constraints**: no real personal data in `trips/` beyond what is there; the script keeps reading LighterPack's CSV format.
- **The areas**: `code` (`main.py`), `docker` (the Dockerfile), `ci` (the workflows and Dependabot), `security`.

## Working in this repo

- Work in a fresh clone in the session's scratchpad, never in TJ's checkout. Branch from the latest `origin/main`.
- Everything reaches main through a squash-merged PR. Never push to main.
- The PR title is `type(scope): summary`; the `PR Title` check refuses anything else.
- CI runs on zimmertr/yggdrasil's `pr-title`, `lint`, `docker-build`, `release` and `auto-merge` modules, pinned by commit SHA with the version beside it. Dependabot bumps the pin after three days.
