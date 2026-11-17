"""Render this report with the repository's ARIS helper and a local template.

Usage: python3 render.py [--helper /path/to/render_html.py]
The generated HTML is standalone; only regeneration needs the helper.
"""
import argparse
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--helper', type=Path, default=HERE.parents[3] / 'math-rsi/base/skills/skills-codex/render-html/scripts/render_html.py')
args = parser.parse_args()
spec = importlib.util.spec_from_file_location('aris_render_html', args.helper)
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
renderer.TEMPLATES_DIR = HERE / 'templates'
raise SystemExit(renderer.main([
    str(HERE / 'Q8_683_FRAMEWORK.md'), '--template', 'academic',
    '--out', str(HERE / 'Q8_683_FRAMEWORK.html'), '--offline',
    '--title', 'MathRSI × 上下界协同｜Q8 上界 683 研究说明',
]))
