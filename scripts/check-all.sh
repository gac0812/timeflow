#!/usr/bin/env bash
# 全仓质量检查入口：后端 ruff/mypy/pytest + 前端 eslint/prettier/tsc。
# 用法: scripts/check-all.sh [backend|frontend]（不带参数则两端都跑）
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-all}"
FAILED=0

case "$TARGET" in
  all | backend | frontend) ;;
  *)
    echo "用法: $0 [backend|frontend]" >&2
    exit 2
    ;;
esac

run_step() {
  local name="$1"
  shift
  echo "==> ${name}"
  if ! "$@"; then
    echo "!! ${name} 未通过"
    FAILED=1
  fi
}

if [[ "$TARGET" == "all" || "$TARGET" == "backend" ]]; then
  if cd "$ROOT/backend"; then
    run_step "backend: ruff check" uv run ruff check .
    run_step "backend: ruff format" uv run ruff format --check .
    run_step "backend: mypy" uv run mypy
    run_step "backend: pytest" uv run pytest
  else
    echo "!! 找不到后端目录：$ROOT/backend"
    FAILED=1
  fi
fi

if [[ "$TARGET" == "all" || "$TARGET" == "frontend" ]]; then
  if cd "$ROOT/frontend"; then
    run_step "frontend: eslint" npm run --silent lint
    run_step "frontend: prettier" npm run --silent format:check
    run_step "frontend: tsc" npm run --silent typecheck
  else
    echo "!! 找不到前端目录：$ROOT/frontend"
    FAILED=1
  fi
fi

if [[ "$FAILED" -ne 0 ]]; then
  echo ""
  echo "检查未通过，请修复后重试。"
  exit 1
fi
echo ""
echo "全部检查通过。"
