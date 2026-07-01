.PHONY: setup dev build-dev build-prod up-dev up-prod down lint format test clean

# Default shell
SHELL := /bin/bash

setup:
	@echo "Setting up Node packages and pre-commit hooks..."
	pnpm install
	@echo "Installing python dependencies using uv..."
	uv venv --python 3.11
	uv pip install -e ./packages/shared-python -e ./apps/api -e ./apps/agent
	@echo "Installing pre-commit hooks..."
	pre-commit install

dev: up-dev

# Docker compose recipes using profiles
up-dev:
	docker compose --profile development up --build -d

down-dev:
	docker compose --profile development down

up-prod:
	docker compose --profile production up --build -d

down-prod:
	docker compose --profile production down

down:
	docker compose --profile development --profile production down

# Build recipes
build-dev:
	docker compose --profile development build

build-prod:
	docker compose --profile production build

# Linting recipes
lint:
	@echo "=== Linting TypeScript and CSS ==="
	pnpm lint
	@echo "=== Linting Python ==="
	uv run ruff check .
	uv run mypy .

# Formatting recipes
format:
	@echo "=== Formatting Web Assets ==="
	pnpm format
	@echo "=== Formatting Python ==="
	uv run black .
	uv run ruff check --fix .

# Testing recipes
test:
	@echo "=== Running Python Tests ==="
	uv run pytest tests/
	@echo "=== Running App Tests ==="
	uv run pytest apps/api/tests/
	uv run pytest apps/agent/tests/
	pnpm --filter web test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	rm -rf node_modules apps/web/node_modules packages/shared-types/node_modules
	rm -rf .venv
