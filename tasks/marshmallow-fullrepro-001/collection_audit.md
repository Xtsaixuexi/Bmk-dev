# Collection Audit

- Source repo: `/root/autodl-tmp/e2e/marshmallow`
- Source commit: `cea3d44f40683832b88b792b84f4a91be032f7ad`
- Local worktree: clean when checked in Step 4.
- Direct `python -m pytest --collect-only -q tests` attempt failed because the active Python environment has no `pytest` installed.
- No project `.venv`, `.tox`, `uv`, or `pytest` executable was available locally.
- Therefore Step 4 uses the prior Bmk-dev collection artifact from the same source commit as the nodeid baseline, after removing the pytest summary footer.

Result: 1178 pure pytest nodeids.
