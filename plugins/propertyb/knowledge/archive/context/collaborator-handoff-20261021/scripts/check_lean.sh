#!/usr/bin/env bash
# Run one completed theorem and its original-statement audit. No dependency updates.
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
project_root="$(cd -- "$script_dir/../../.." && pwd)"
mode="${1:-general}"

if [[ $# -gt 1 ]]; then
  printf 'Usage: bash %s [general|t32|t33]\n' "$0" >&2
  exit 2
fi

case "$mode" in
  general)
    module='Aris4Math.General.Growth.Twelve'
    audit='ReviewAuditGeneralGrowth12.lean'
    ;;
  t32)
    module='Aris4Math.Main'
    audit='ReviewAudit.lean'
    ;;
  t33)
    module='Aris4Math.ThirtyThree.Main'
    audit='ReviewAudit33.lean'
    ;;
  *)
    printf 'Usage: bash %s [general|t32|t33]\n' "$0" >&2
    exit 2
    ;;
esac

if ! command -v lake >/dev/null 2>&1; then
  printf 'lake is unavailable. Install elan/Lean and fetch the pinned cache as described in LEAN_REPRODUCE.md.\n' >&2
  exit 1
fi

cd -- "$project_root/formal"
printf 'Building %s with the pinned formal/lean-toolchain and manifest.\n' "$module"
lake build "$module"
printf 'Compiling original-statement audit %s.\n' "$audit"
lake env lean "$audit"
