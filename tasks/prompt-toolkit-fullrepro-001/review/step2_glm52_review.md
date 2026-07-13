## Benchmark Spec Review: prompt-toolkit-fullrepro-001

### Verdict: PASS / CONTINUE

Stage 2 output is well-constructed and ready for Stage 3 test filtering. No blockers. Minor required corrections noted below.

---

### Blockers

None.

---

### Required Corrections

**1. Positive `start_position` assertion wording is inverted**

The Error Semantics section states:
> `Completion(...)` must raise `AssertionError` when `start_position` is positive.

But the Public API section states:
> `start_position` must be zero or negative.

These are consistent with each other, but the error semantics entry is the more useful one to keep precise. The constructor signature shows `start_position: int = 0`, so valid values are `<= 0`. The error semantics entry is correct as written — no change needed here. ✓ (Self-resolving on re-read.)

**2. `style.get_attrs_for_style_str` in the workflow example is not confirmed public API**

The Representative Workflows section includes:

```python
assert style.get_attrs_for_style_str("class:b").bold is True
```

`get_attrs_for_style_str` is not listed anywhere in the Installable Surface or Public API sections. If this method is part of the `BaseStyle` / `Style` contract it must be listed in the styles section. If it is internal, the example must be rewritten to use a verifiable public path (e.g., asserting via formatted output or a documented lookup method). This is the one concrete leakage risk into Stage 3 — a test writer following this example could target a non-public method.

**Action:** Either add `get_attrs_for_style_str` to the Styles public surface with a behavioral `must` clause, or replace the assertion in the example with one that uses a documented path.

**3. `Attrs` and `DEFAULT_ATTRS` are listed but `Attrs` fields are never specified**

The Styles section lists `Attrs` and `DEFAULT_ATTRS` as public exports but gives no behavioral contract for what `Attrs` contains. Since `Attrs` is the return type of style resolution and `bold`, `italic`, `underline`, etc. are accessed as fields in the workflow example, the spec should include a minimal description of the `Attrs` named fields — at minimum the boolean attributes `bold`, `italic`, `underline`, `blink`, `reverse`, `hidden`, `dim`, `strike`, and the color fields `color` and `bgcolor`.

**Action:** Add a short `Attrs` field description to the Styles section.

**4. `Buffer.validate()` signature inconsistency**

The Buffer section specifies `Buffer.validate(set_cursor: bool = False)` but Error Semantics states `Buffer.validate()` without the parameter. This is just a documentation inconsistency — the Error Semantics entry should read `Buffer.validate(set_cursor=False)` for alignment.

**Action:** Trivial wording fix in Error Semantics.

**5. `PromptSession` interrupt/EOF exception type defaults are unspecified**

The spec says `prompt()` must raise "the configured interrupt exception" and "the configured EOF exception" but never states what the defaults are when the caller does not configure them. Stage 3 test writers need to know the defaults (`KeyboardInterrupt` and `EOFError` respectively, per the library) to write baseline tests without custom configuration.

**Action:** Add the default exception types parenthetically in both the PromptSession section and the corresponding Error Semantics entry.

---

### Recommended Corrections (non-blocking)

- The `KeyProcessor` description says "unknown keys must be ignored after allowing any shorter suffix match to run" — this is slightly ambiguous about what "shorter suffix match" means. Consider tightening to "any binding whose key sequence is a suffix of the unmatched sequence."
- `Fragment_list_width` is listed in the Installable Surface but has no behavioral clause in the Formatted Text section. A one-line `must` clause (returns total display-cell width of all fragments) would make it testable.
- The `Template.format(...)` behavioral clause is minimal. A note that positional/keyword arguments must accept formatted-text values and that the plain text of the result equals the plain text of the template with arguments substituted would help Stage 3.

---

### Structural Checks

| Check | Result |
|---|---|
| Reads as library docs, not benchmark scaffolding | ✓ |
| No hidden source paths, task IDs, or commit hashes in candidate-visible body | ✓ |
| No private module names or test paths exposed | ✓ |
| Required sections present (Overview, Scope, PSM, Public API, Error Semantics, Cross-View Invariants, Non-Goals, Evaluation Notes) | ✓ |
| Behavioral `must`/`returns`/`raises` language throughout | ✓ |
| Product State Model covers all three projections with invariants | ✓ |
| Cross-View Invariants cover text, interaction, presentation, and I/O | ✓ |
| Non-goals explicitly exclude terminal bytes, snapshots, private internals, contrib | ✓ |
| No escape hatches permitting behavioral skipping | ✓ |
| Error semantics attached to public exception classes, not message strings | ✓ |
| Evaluation Notes framed for public-API oracle construction | ✓ |

---

### Stage 3 Readiness Notes

The spec is scoped conservatively and the non-goals are explicit enough that test filtering decisions are straightforward. The one item that genuinely needs resolution before Stage 3 begins is item 2 above (`get_attrs_for_style_str`) — if a Stage 3 test is written from that example verbatim it could target a non-public method and fail filtering. All other corrections can be applied in parallel with Stage 3 prep.

**Proceed to Stage 3 after resolving items 2 and 5. Items 3 and 4 are low-risk and can be folded into the same edit pass.**