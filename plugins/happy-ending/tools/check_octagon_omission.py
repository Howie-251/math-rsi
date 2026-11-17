#!/usr/bin/env python3
"""Portable wrapper for replaying the 15-file octagon omission-tree subset (`finite-inputs.zip`).

Extracts `finite-inputs.zip` into a temporary directory, verifies SHA-256 hashes of all 15 files,
runs `es7_es8_bounds_81_319_v1/tools/check_octagon_finite.py`, and writes a clean JSON receipt
without modifying `archive/`. Note: this replays Schroeder's public finite omission trees
(`C_8 <= 193`, `D_8 <= 124`); the project's abstract signotope cyclic-sign packet bridge in
`EIGHT-CYCLE-TRANSFER.md` remains a paper proof pending independent review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
import time
import zipfile


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--zip-path",
        type=Path,
        default=Path("plugins/happy-ending/archive/nmrs-20261117/source/reports/n79-overlap-20261116/octagon-source-replay/finite-inputs.zip"),
    )
    ap.add_argument("--output", type=Path, default=None, help="JSON receipt path (outside archive)")
    args = ap.parse_args()

    zip_path = args.zip_path.resolve()
    zip_sha = sha256_bytes(zip_path.read_bytes())
    began = time.monotonic()

    with tempfile.TemporaryDirectory(prefix="mathrsi-octagon-finite-") as tmp:
        tmp_dir = Path(tmp)
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(tmp_dir)
        sub = tmp_dir / "es7_es8_bounds_81_319_v1"
        checker = sub / "tools/check_octagon_finite.py"
        inner_out = tmp_dir / "finite-result.json"
        proc = subprocess.run(
            [sys.executable, "-B", str(checker), "--output", str(inner_out)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        assert proc.returncode == 0, f"check_octagon_finite.py failed:\n{proc.stdout}\n{proc.stderr}"
        inner = json.loads(inner_out.read_text(encoding="utf-8"))
        assert inner.get("status") == "PASS"

    receipt = {
        "status": "PASS",
        "platform": platform.platform(),
        "seconds": round(time.monotonic() - began, 4),
        "input_zip_sha256": zip_sha,
        "finite_check": inner,
        "scope_note": "Replays Schroeder's 15-file public finite omission-tree arithmetic (balanced <= 193, residual <= 124). Does not build Lean or certify the signotope cyclic-sign packet bridge.",
    }
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "seconds": receipt["seconds"],
        "balanced_bound": inner["balanced"]["omission_tree"]["bound"],
        "residual_bound": inner["residual"]["omission_tree"]["bound"],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
