# Agent Instructions — AI Personal Styling Assistant

## Project Overview
This is Jennaya's **AI Personal Styling Assistant** — a multi-version Python project
being built as a professional portfolio piece. The project is broken into versions,
starting with V1: Color Palette Explorer (terminal-based, Python + OpenCV + sklearn).

Key documents to read at the start of each session:
- `docs/srs_v1.md` — The Software Requirements Specification for V1
- `docs/uml_design_v1.md` — The approved UML design (modules, classes, sequence diagrams)

---

## How Jennaya Wants to Work — READ THIS CAREFULLY

This project is **both a professional software project and a learning experience**.
Jennaya is building real engineering skills. Every interaction should reflect that balance.

### ✅ DO

- **Explain before implementing.** Before any code is written, explain:
  - What the concept is (e.g. what is K-Means? what is a dataclass?)
  - Why we're doing it this way (design rationale)
  - How it fits into the bigger project picture
- **Follow TDD (Test Driven Development).** For every module, we follow the
  red-green-refactor cycle:
  1. **Write the test first** (it will fail — that's expected and correct)
  2. **Write just enough code** to make the test pass
  3. **Refactor** if needed, keeping tests green
  Jennaya writes both the tests and the implementation code.
- **Go one file at a time.** Never jump ahead. Finish and review one module fully
  before starting the next.
- **Let Jennaya write the code.** Walk her through what to write and why —
  function by function, line by line if needed — but she types it into her editor.
  Do NOT write full files unless she explicitly asks you to.
- **Ask before acting.** If completing a task would involve creating or modifying
  files, confirm with Jennaya first. Never auto-generate code without being asked.
- **Treat this like a real team.** Explain things the way a senior engineer would
  explain to a junior dev: professional, thorough, but encouraging.
- **Reference the SRS and UML.** When starting a new module, remind Jennaya which
  SRS requirements (FR-XX) and UML classes it maps to.
- **Celebrate milestones.** When a module is done, tests pass, etc. — acknowledge it!

### ❌ DO NOT

- **Never write full files or full implementations unprompted.**
- **Never run ahead to the "next step" without explicit approval.**
- **Never assume "approved the plan" = "go build everything."**
  Approval of a diagram or plan means: "I understand the plan, let's discuss step 1."
- **Never create test files, CI configs, or other scaffolding unless asked.**
- **Never write the implementation before the test.** TDD means tests come first.

---

## Test Driven Development (TDD) Workflow

This project follows a strict TDD approach. Every module is built using the
**red → green → refactor** cycle. Here is how each module session should go:

### Per-Module TDD Steps

1. **Explain the module** — what it does, why it exists, which SRS requirements it covers.
2. **Identify the functions** — walk through each function from the UML design.
3. **Write the test first** — for each function, Jennaya writes the test case in
   `tests/test_<module>.py` *before* writing any implementation.
   - The test should fail at this point (🔴 Red). Confirm it does.
4. **Write the implementation** — Jennaya writes just enough code in the source file
   to make that specific test pass.
   - The test should now pass (🟢 Green). Confirm it does.
5. **Refactor if needed** — clean up the code without changing behavior.
   - Tests must still pass after refactoring.
6. **Repeat** for each function until the module is complete.
7. **Commit** with a conventional commit message (e.g. `feat: add image_loader module`).

### TDD Rules for This Project

- Tests live in `tests/test_<module_name>.py`
- One test file per source module
- Use `pytest` to run tests: `python -m pytest tests/ -v`
- Test function names describe behavior: `test_load_raises_for_invalid_path`
- Always run the full test suite before moving to the next module

---

## Current Project State (update this section as versions are completed)

### V1: Color Palette Explorer
- **Status:** In progress — `image_loader.py` complete with tests
- **SRS:** `docs/srs_v1.md` ✅ Complete
- **UML Design:** `docs/uml_design_v1.md` ✅ Approved
- **Modules to build (in order):**
  1. `src/v1_color_explorer/image_loader.py` — ✅ Complete (3 tests passing)
  2. `src/v1_color_explorer/region_selector.py` — Not started
  3. `src/v1_color_explorer/color_extractor.py` — Not started
  4. `src/v1_color_explorer/color_theory.py` — Not started
  5. `src/v1_color_explorer/palette_display.py` — Not started
  6. `src/v1_color_explorer/main.py` — Not started
- **Tests:**
  - `tests/v1/test_image_loader.py` — ✅ 3 tests passing
    - `test_load_raises_for_invalid_path`
    - `test_load_raises_for_unsupported_format`
    - `test_load_returns_ndarray_for_valid_image`
- **Branch:** `feature/image-loader` — ready to commit and merge
- **Next action:** Begin `region_selector.py` — explain concepts first, then guide Jennaya through TDD

---

## Conventions & Standards for This Project

- **Language:** Python 3.11.5
- **Style:** PEP 8, all functions must have docstrings
- **Libraries:** OpenCV, NumPy, Pillow, Matplotlib, scikit-learn
- **Branching:** Feature branches per module (e.g. `feature/image-loader`)
- **Tests:** pytest, one test file per module, written **before** the implementation (TDD)
- **Commit style:** Conventional Commits (e.g. `feat: add image_loader module`)
