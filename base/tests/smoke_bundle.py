#!/usr/bin/env python3
"""Offline integration check for the bundled ARIS copy; no model or network calls."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    base = Path(__file__).resolve().parents[1]
    out = args.out_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((base / 'ARIS_SNAPSHOT.json').read_text())
    verified = []
    for row in manifest['files']:
        data = (base / row['source_path']).read_bytes()
        blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        assert blob == row['source_blob'], row['source_path']
        verified.append(row['source_path'])
    commands = []
    with tempfile.TemporaryDirectory(prefix='mathrsi-aris-smoke-') as scratch:
        root = Path(scratch)
        relocated = root / 'relocated-base'
        shutil.copytree(base, relocated, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', 'evidence'))
        workspace = root / 'task-workspace'
        workspace.mkdir()
        # Explicit helper paths prevent all project/global fallback selection.
        # ARIS_REPO is assigned in each executed shell, not inherited from HOME.
        def run(relative, *argv, expected=0):
            helper = relocated / relative
            command = [sys.executable, str(helper), *map(str, argv)]
            import os
            env = os.environ.copy()
            env['ARIS_REPO'] = str(relocated)
            env['PYTHONDONTWRITEBYTECODE'] = '1'
            result = subprocess.run(command, cwd=workspace, env=env, text=True, capture_output=True)
            commands.append({'argv': command, 'cwd': str(workspace), 'ARIS_REPO': str(relocated),
                             'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr})
            assert result.returncode == expected, commands[-1]
            return result.stdout
        wiki = workspace / 'research-wiki'
        run('tools/research_wiki.py', 'init', wiki)
        run('tools/research_wiki.py', 'add_claim', wiki, '--slug', 'smoke-local-obligation',
            '--name', 'Integration fixture: no mathematical assertion', '--status', 'unproven',
            '--statement', 'This fixture checks local claim bookkeeping only.',
            '--evidence', 'No proof or numerical computation has been supplied.')
        stats = run('tools/research_wiki.py', 'stats', wiki)
        assert (wiki / 'claims' / 'smoke-local-obligation.md').is_file()
        assert 'unproven' in (wiki / 'claims' / 'smoke-local-obligation.md').read_text()
        assert (wiki / 'query_pack.md').is_file()
        default_route = json.loads(run('tools/reviewer_route.py', '--project', workspace, '--host', 'codex'))
        assert default_route['backend'] == 'codex' and default_route['transport'] == 'native'
        (workspace / '.aris').mkdir(exist_ok=True)
        (workspace / '.aris/reviewer.json').write_text(json.dumps({'backend': 'grok', 'model': 'grok-4.7', 'effort': 'xhigh'}))
        project_route = json.loads(run('tools/reviewer_route.py', '--project', workspace, '--host', 'codex'))
        assert project_route['backend'] == 'grok' and project_route['source'] == 'project'
        inline_route = json.loads(run('tools/reviewer_route.py', '--project', workspace, '--host', 'codex',
                                     '--reviewer', 'gemini', '--effort', 'high'))
        assert inline_route['backend'] == 'antigravity' and inline_route['source'] == 'inline'
        run('tools/reviewer_route.py', '--project', workspace, '--host', 'codex', '--reviewer', 'nonexistent', expected=2)
        fixture = workspace / 'fixture.md'
        fixture.write_text('# Local smoke artifact\n\nThis is a renderer integration fixture.\n\n$$x^2 + y^2 = z^2$$\n\n| Kind | Status |\n| --- | --- |\n| Proof | unproven |\n')
        for host, template in [('skills/skills-codex', 'academic'), ('skills', 'dashboard')]:
            target = workspace / (template + '.html')
            run(f'{host}/render-html/scripts/render_html.py', fixture, '--template', template,
                '--out', target, '--offline', '--title', 'MathRSI integration fixture')
            html = target.read_text()
            assert 'MathRSI integration fixture' in html
            assert 'x^2 + y^2 = z^2' in html
            assert 'cdn.jsdelivr.net' not in html and 'cdnjs.cloudflare.com' not in html
            shutil.copy2(target, out / target.name)
        shutil.copytree(wiki, out / 'research-wiki', dirs_exist_ok=True)
        result = {'status': 'PASS', 'source_revision': manifest['revision'],
                  'verified_upstream_files': len(verified), 'skills_per_host': len(manifest['selection']),
                  'relocated_copy': str(relocated), 'commands': commands,
                  'scope': 'Offline local integration only: provenance, wiki claim bookkeeping, reviewer parsing, both HTML templates. No model/network/Lean/LaTeX invocation.',
                  'offline_math': 'Raw formula text retained; no embedded SVG math claimed.'}
        (out / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'verified_upstream_files': len(verified), 'commands': len(commands), 'evidence': str(out)}))


if __name__ == '__main__':
    main()
