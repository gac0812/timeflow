# Dependency Management

## Runtime Baseline

| Area | Tool | Fixed version | Source of truth |
| --- | --- | --- | --- |
| Frontend runtime | Node.js | 20.20.2 | `.nvmrc` |
| Frontend package manager | npm | 10.8.2 | root and frontend `package.json` |
| Backend runtime | Python | 3.11.15 | `.python-version` |
| Backend package manager | uv | 0.11.28 | Dockerfile and CI workflow |
| Development database | PostgreSQL | 16.4 | `docker-compose.yml` |

## Allowed Commands

- Frontend dependencies: `npm --prefix frontend ci`.
- Backend dependencies: `cd backend && uv sync --locked --all-groups`.
- Frontend quality and security: `npm --prefix frontend run check` and `npm --prefix frontend audit --audit-level=moderate`.
- Backend quality: `cd backend && uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest`.

Do not use yarn, pnpm, pip install, Poetry, or a second lockfile in this repository.

## Lockfile Rules

- Commit `frontend/package-lock.json` whenever `frontend/package.json` changes.
- Commit `backend/uv.lock` whenever `backend/pyproject.toml` changes.
- Use `npm ci` and `uv sync --locked` for installation and CI. They must not modify a lockfile.
- Keep runtime dependencies and development-only dependencies in their declared sections.

## Update Procedure

1. Change one dependency declaration in its owning manifest.
2. Regenerate only that package manager's lockfile.
3. Run the owning quality checks and security audit.
4. For Expo changes, run Expo Doctor and an Android export before committing.
