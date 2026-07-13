# diskcache-fullrepro-001

SpecBench / Bmk full-reproduction task package.

Candidate-visible packet: `spec.md` only, plus generic implementation instructions. Scoring artifacts, generated oracle tests, nodeids, taxonomy, reference scores, reviews, and judge reports are hidden from candidates.

Scoring oracle source is generated-only and included at `tests/test_generated_diskcache.py` for reproducibility. Use `harness/score_pytest_original.py` with `--source-repo tasks/diskcache-fullrepro-001`, `--remove-path diskcache`, `--nodeids kept_nodeids.txt`, and `--taxonomy taxonomy.jsonl`.
