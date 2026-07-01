# CyberNest - Cybersecurity SaaS Platform Foundation

CyberNest is a production-ready, clean-architecture cybersecurity SaaS platform built as a monorepo. This repository contains the scaffolded foundation, configuration, and tools.

## Architecture & Structure

```
cybernest/
├── .github/                 # GitHub Actions CI Workflows (lint, tests, build)
├── apps/
│   ├── web/                 # React + Vite + TypeScript Frontend
│   ├── api/                 # FastAPI Backend (SQLAlchemy 2.0, Alembic, PostgreSQL)
│   └── agent/               # Fingerprinting Python 3.11 Agent (with plugin architecture)
├── packages/
│   ├── shared-python/       # Shared Python libraries (Models, Cryptography, structlog)
│   └── shared-types/        # Shared TypeScript DTO type definitions
├── infrastructure/
│   ├── postgres/            # Database initialization scripts
│   ├── nginx/               # Reverse proxy routing rules
│   └── terraform/           # Reserved for infrastructure-as-code
├── scripts/                 # Development scripts
├── docs/                    # Architecture and documentation
└── tests/                   # Monorepo-level integration and E2E testing
```

## Tech Stack

- **Frontend**: React, Vite, TypeScript, Tailwind CSS v4, React Router
- **Backend**: FastAPI, SQLAlchemy 2.0, Alembic, PostgreSQL
- **Agent**: Python 3.11 with an extensible plugin engine
- **Python Tooling**: `uv` workspaces, Ruff, Black, mypy, structlog, Pydantic Settings
- **TypeScript Tooling**: `pnpm` workspaces, ESLint, Prettier

---

## Getting Started

### Prerequisites

- Node.js (>= 18) & `pnpm` (>= 8)
- Python 3.11 & `uv` package installer
- Docker & Docker Compose (supporting profile modes)

### Local Dev Setup

1. **Clone the repository**
2. **Setup virtual environments and dependencies**
   ```bash
   make setup
   ```
   This will install all npm/pnpm modules, initialize a python `.venv` using `uv`, mount the local modules in editable mode, and configure the git `pre-commit` hooks.

3. **Environments Configuration**
   Copy `.env.development` to `.env` or run apps pointing to the targeted env file (e.g. `.env.development`).

4. **Run Developer Services (Docker)**
   Orchestrate development services (web, api, database, agent) with file volume mounts for hot reload:
   ```bash
   make up-dev
   ```

5. **Stop Developer Services**
   ```bash
   make down
   ```

---

## Development Workflows

### Formatting and Linting

- **Auto-format code**:
  ```bash
  make format
  ```
  Runs `black` and `ruff --fix` for Python files, and `prettier` for TypeScript/CSS/JSON/Markdown.

- **Lint checks**:
  ```bash
  make lint
  ```
  Runs `ruff check`, `mypy`, and `pnpm lint` (ESLint) to ensure strict typing and rule compliance.

### Running Tests

- **Run all unit/integration tests**:
  ```bash
  make test
  ```
