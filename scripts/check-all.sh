#!/usr/bin/env bash

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-all}"

case "$TARGET" in
  all|backend|frontend) ;;
  *)
    echo "Usage: $0 [all|backend|frontend]" >&2
    exit 2
    ;;
esac

if [[ "$TARGET" == "all" || "$TARGET" == "backend" ]]; then
  (
    cd "$ROOT/backend"
    uv sync --locked --all-groups
    uv run ruff check .
    uv run ruff format --check .
    uv run mypy
    uv run pytest
  )
fi

if [[ "$TARGET" == "all" || "$TARGET" == "frontend" ]]; then
  npm --prefix "$ROOT/frontend" ci
  npm --prefix "$ROOT/frontend" run check
fi
