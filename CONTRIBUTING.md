# Contributing to MathRSI

[English](CONTRIBUTING.md) | [中文版](CONTRIBUTING.zh-CN.md)

Thank you for your interest in contributing to MathRSI! This guide explains how the repository is organized and how to contribute domain plugins, verifiers, harness improvements, and documentation.

## Ways to Contribute

- **Domain plugins & mathematical results**: Add a new domain plugin under `plugins/<domain>/` or deepen an existing one with reductions, failure diagnostics, curated certificates, and standalone verifiers.
- **Verification & formalization**: Contribute independent replay checkers (`plugins/<domain>/tools/`), bounded counterexample checks, or Lean 4 formalizations for working proofs and open parameters ([Six-case index](case-studies/README.md)).
- **Base harness improvements**: Propose evidence-backed workflow refinements grounded in real research bottlenecks via [`mathrsi-meta-evolve`](base/skills/mathrsi-meta-evolve/SKILL.md) ([Evolution workflow](docs/EVOLUTION_WORKFLOW.md)).
- **Documentation, readers & bug reports**: Fix broken commands or links, clarify proof scopes, report issues, or improve bilingual docs and public readers ([Public Pages guide](docs/PAGES.md)).

## Getting Started

1. Fork the repository on GitHub and clone your fork (or create an isolated `git worktree` if working as a repository maintainer):
   ```bash
   git clone https://github.com/YOUR_USERNAME/math-rsi.git
   cd math-rsi
   ```
2. Create a focused branch for your changes:
   ```bash
   git checkout -b feat/your-topic
   ```
3. Follow [Quick Start](docs/QUICKSTART.md) to run skills in **Claude Code** (`/skill-name`) or **Codex** (`$skill-name`).

## Development & Repository Conventions

### Three-layer boundary

- **Base** (`base/`) supplies domain-agnostic orchestration (`Prepare → Route → Prove → Verify → Handoff`) and the pinned ARIS snapshot ([`base/ARIS_SNAPSHOT.json`](base/ARIS_SNAPSHOT.json)). Do not hardcode domain-specific tactics into `base/` during single-problem solving, and do not modify files pinned by `ARIS_SNAPSHOT.json` without updating upstream provenance ([Provenance](docs/PROVENANCE.md)).
- **Domain plugins** (`plugins/<domain>/`) hold domain skills, mathematical references, failure maps, curated `archive/` inputs, and runnable `tools/` checkers. Follow the [Plugin Contract](docs/PLUGIN_CONTRACT.md) and register stage entry points in [`docs/DOMAIN_ROUTING.md`](docs/DOMAIN_ROUTING.md).
- **Active task workspaces** stay outside the repository (for example, `../my-problem/`) while research is in progress ([Workspace guide](docs/WORKSPACE.md)); curate established proofs, checkers, and reusable methods into `plugins/` and `case-studies/` upon handoff.

### Skill authoring & dual-host discovery

Each skill is a `SKILL.md` file with YAML frontmatter (`name`, `description`) and actionable prose covering scope, preconditions, exact tool/reference calls, failure recovery, and return artifacts ([Skill Acceptance](docs/SKILL_ACCEPTANCE.md)):

```markdown
---
name: my-domain-skill
description: What mathematical obligation or workflow stage this skill handles.
---

# Skill Title

Scope, preconditions, mathematical references, verifier commands, and return contract...
```

Expose new MathRSI or domain skills to both hosts by adding relative symlinks under `.claude/skills/<skill-name>` (Claude Code) and `.agents/skills/<skill-name>` (Codex).

### Evidence integrity & artifact size

- **Accurate verification scope**: State explicitly whether a result is Lean-verified, backed by an independently replayed computational certificate, reviewed via cross-model or same-family provisional audit, or an unreviewed working manuscript. Never silently upgrade claim status, and never move fixed release tags (`v1`–`v6`).
- **Readable sources, `< 50 MiB` per file, no Git LFS**: Unpack curated proofs, source code, and compact certificates directly—do **not** commit opaque `.zip` or `.rar` archives. Keep every tracked file **under 50 MiB** with zero Git LFS; record omitted large SAT/CNF/DRAT traces or search pools in an `INVENTORY.json` with byte sizes, SHA-256 hashes, and reproduction instructions.

## Testing Your Changes

Run the offline standard-library checks from the repository root before submitting:

```bash
# 1. Verify local Markdown links and .claude/.agents skill symlinks
python3 tools/check_links.py

# 2. Verify bundled ARIS snapshot & offline helper smoke test (when touching base/)
python3 base/tests/smoke_bundle.py --out-dir /tmp/mathrsi-smoke

# 3. Verify explicit allowlist build for GitHub Pages (when touching public site/readers)
python3 tools/build_public_site.py --output /tmp/mathrsi-site
```

Also run any new or modified domain checkers in `plugins/<domain>/tools/` on real inputs, and test modified skills in Claude Code or Codex.

## Pull Request Process

1. Keep each PR focused on a single coherent change and write clear commit messages.
2. Update `README.md`, `README.zh-CN.md`, and [`docs/DOMAIN_ROUTING.md`](docs/DOMAIN_ROUTING.md) when adding new skills, plugins, or headline results.
3. Describe the exact scope verified and note any unverified branches or external dependencies.

### PR Checklist

- [ ] Links and `.claude`/`.agents` skill symlinks pass `python3 tools/check_links.py`
- [ ] Verification status, provisional/review scope, and provenance are stated accurately
- [ ] No raw `.zip`/`.rar` archives, Git LFS objects, or files `>= 50 MiB` are added
- [ ] Affected domain checkers, skills, and smoke/site builds are tested locally

## Code of Conduct

- Be respectful, constructive, and grounded in reproducible mathematical and engineering evidence.
- Distinguish established theorems, bounded computational checks, and open conjectures clearly.

## Questions?

Feel free to open a GitHub Issue for bug reports, questions, or research collaboration inquiries.

## License

By contributing to MathRSI workflows, documentation, and scripts, you agree that your contributions will be licensed under the [MIT License](LICENSE). Archived papers and third-party materials retain their original copyrights ([Provenance](docs/PROVENANCE.md)).
