# Project Structure

```text
timeflow/
├── .env.example                 # Docker Compose development defaults
├── .github/workflows/ci.yml     # Quality, security, export, and container checks
├── backend/
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── uv.lock
│   ├── src/timeapp/
│   │   ├── agents/              # Main Agent and internal capability skeletons
│   │   ├── api/                 # HTTP routing and health endpoint
│   │   ├── basic/               # Manual business and OCR/ASR boundaries
│   │   ├── common/              # Contracts and shared capability boundaries
│   │   └── core/                # Settings and database infrastructure
│   └── tests/
├── docs/
│   ├── dependency-management.md
│   └── project-structure.md
├── frontend/
│   ├── .env.example             # Android emulator API base URL
│   ├── package.json
│   ├── package-lock.json
│   └── src/
│       ├── api/
│       ├── constants/
│       └── screens/
├── docker-compose.yml           # API and PostgreSQL development stack
├── package.json                 # Cross-project commands only
└── scripts/check-all.sh
```

`agents/` contains only the orchestration and capability framework. It does not contain implemented LLM, confirmation, CRUD, or database business logic. `common/` owns cross-Agent contracts and future shared capabilities; `basic/` owns non-Agent product boundaries.
