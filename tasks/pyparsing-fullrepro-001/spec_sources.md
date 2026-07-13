# Spec Source Plan

This file records the public sources to inspect during Step 3 spec drafting. It is internal and must not be shown to candidate agents.

## Primary Public Documentation

- `/root/autodl-tmp/e2e/pyparsing/README.rst`
- `/root/autodl-tmp/e2e/pyparsing/docs/index.rst`
- `/root/autodl-tmp/e2e/pyparsing/docs/HowToUsePyparsing.rst`
- `/root/autodl-tmp/e2e/pyparsing/docs/pyparsing.rst`
- `/root/autodl-tmp/e2e/pyparsing/docs/pyparsing_classes.md`
- `/root/autodl-tmp/e2e/pyparsing/examples/`

## Public API Discovery Sources

- `/root/autodl-tmp/e2e/pyparsing/pyparsing/__init__.py`
- `/root/autodl-tmp/e2e/pyparsing/pyparsing/core.py`
- `/root/autodl-tmp/e2e/pyparsing/pyparsing/results.py`
- `/root/autodl-tmp/e2e/pyparsing/pyparsing/exceptions.py`
- `/root/autodl-tmp/e2e/pyparsing/pyparsing/actions.py`
- `/root/autodl-tmp/e2e/pyparsing/pyparsing/helpers.py`
- `/root/autodl-tmp/e2e/pyparsing/pyparsing/common.py`
- `/root/autodl-tmp/e2e/pyparsing/pyparsing/unicode.py`
- `/root/autodl-tmp/e2e/pyparsing/pyparsing/testing.py`

## Drafting Notes

- Start from `pyparsing.__all__` and public examples, then decide each public name by the spec-writer Q1/Q2 rules.
- Include behavior for parser construction, expression composition, parse actions, exception classes, `ParseResults`, helper namespaces, and testing helpers only when it is part of the public contract and not obvious from general parser-combinator knowledge.
- Treat exact warning text, diagnostic formatting, railroad diagram layout, and legacy compatibility aliases as filtering risks unless public docs make them a required user-visible contract.
