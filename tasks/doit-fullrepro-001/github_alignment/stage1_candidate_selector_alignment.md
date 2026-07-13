# Stage 1 GitHub Alignment: doit-fullrepro-001

Generated: 2026-07-09T09:00:00Z

Authority:

- `github_alignment/raw_main/skills/candidate-selector/SKILL.md`
- `github_alignment/raw_main/skills/task-synthesizer/SKILL.md`
- Fetch manifest: `github_alignment/raw_main/FETCH_MANIFEST.json`

## Alignment Checks

- PASS: Candidate was selected only after logical de-duplication and existing task exclusion.
- PASS: Hard gate evidence is recorded in `candidate_selection.md` and `source_audit.json`.
- PASS: Source pointer records repo path, commit, and remote for builder use only.
- PASS: Test import/collection risk was pre-screened with pytest collect.
- PASS: Risks are routed to Stage 3 filtering rather than hidden inside the public spec.
- PASS: Stage 2 handoff artifacts are present: `candidate_selection.md`, `source_audit.json`, `source_pointer.md`, `filter_notes.md`, and `PIPELINE_STATE.md`.

Verdict: PASS. Stage 1 is aligned with the GitHub `candidate-selector` workflow and ready for model review.
