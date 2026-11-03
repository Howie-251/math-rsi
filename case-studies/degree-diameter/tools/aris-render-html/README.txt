ARIS render-html source snapshot

These files are preserved from this repository's bundled ARIS implementation:
base/skills/skills-codex/render-html/scripts/render_html.py
base/skills/skills-codex/render-html/scripts/templates/academic.html
base/LICENSE

Upstream: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
Skill: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/main/skills/render-html/SKILL.md

The Degree–Diameter case adapter uses the repository copy when available and
this bundled snapshot when the case directory is extracted by itself.
The original renderer and template are unmodified. The adapter adds the local
interactive figures and omits fingerprint fields without computing them.

From the case directory, render both manuscripts with:
python3 tools/render_index.py
