# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python-based CV/resume generation system: JSON data → PDF via ReportLab. Uses a "master + variants" pattern where `super-json.json` holds every fact about the candidate's career, and each tailored JSON is a filtered, job-specific subset used to generate one PDF.

## Commands

Do **not** rely on `source .venv/bin/activate.fish` — the agent shell is not fish and that script fails to parse. Call the venv interpreter directly:

```shell
# Generate a PDF
.venv/bin/python cv.py --json-file ./cv_actualizado.json --output-file daniel_banariba_cv.pdf

# Validate content limits without generating a PDF
.venv/bin/python cv.py --json-file ./cv_actualizado.json --only-validate

# Defaults to cv_generado.pdf when --output-file is omitted
.venv/bin/python cv.py --json-file ./super-json.json
```

Only dependency: `reportlab` (installed in `.venv/`, Python 3.14.7). There is no test suite, linter, or build step.

### Verify the PDF after generating

`cv.py` exits 0 even when layout breaks, so a successful run proves nothing about the output. Always check:

```shell
pdfinfo daniel_banariba_cv.pdf | grep Pages
pdftoppm -png -r 100 daniel_banariba_cv.pdf <scratchpad>/page && # then Read the PNGs
```

Reading the rendered pages is the only way to catch orphaned section headers, overflow, and bad page breaks.

## Architecture

### cv.py pipeline

`load_json()` → `validate_cv_content()` → `setup_styles()` → `build_cv_content()` → `generate_cv_pdf()`

- `build_cv_content()` emits sections in fixed order: personal info → profile → experience → skills → projects → education → certifications → languages → references. Every section is conditional: absent key means the section is skipped entirely, so a tailored JSON drops sections simply by omitting them.
- Section **order is hardcoded**; only the section *titles* are data-driven via `section_titles`.
- Skills rendering iterates `skill_labels`, not `skills`. A skills category with no matching key in `skill_labels` renders **nothing** — when adding a category, always add both.
- `setup_styles(base_font_size=10)` is the single global knob for typography scale.
- Contact links render as bare domains (`github.com/handle`) via `format_url_display()` while the `href` keeps the full URL — deliberate, so ATS parsers read the text rather than the word "GitHub".
- Page setup is standard `letter` (612 × 792 pts), margins 0.5" sides, 0.4" top, 0.5" bottom. The current CVs are **two pages by design** — do not compress content to force one page unless asked.

### Content limits are advisory

`CV_LIMITS` (profile 500 chars · 3 jobs · 5 responsibilities/job at 120 chars · 4 projects · 3 education · 4 certifications · 8 skills per category) only produces console warnings. The PDF generates regardless.

**The real tailored CVs deliberately exceed the 120-char-per-responsibility and skills-per-category limits.** Bullets carry quantified outcomes, and those don't fit in 120 characters. Treat these warnings as expected noise, not a defect to fix.

### JSON schema

```json
{
  "personal_info": { "name", "email", "phone", "location", "website", "github", "linkedin" },
  "profile": "string",
  "experience": [{ "company", "position", "date_range", "location", "responsibilities": [], "technologies" }],
  "skills": { "<category>": "comma-separated string" },
  "projects": [{ "title", "description", "technologies" }],
  "education": [{ "institution", "degree", "date_range", "location" }],
  "certifications": ["string"],
  "languages": ["Español: Nativo"],
  "references": [{ "name", "position", "company", "phone" }],
  "section_titles": { "experience", "skills", "projects", "education", "certifications", "languages", "references" },
  "skill_labels": { "<category>": "Display Label" }
}
```

Skill category keys are **arbitrary** — `skills` and `skill_labels` just have to agree. Reorder skill categories by reordering `skill_labels` (e.g. a frontend role leads with `frontend`, a data role with `data`). `languages` also accepts `[{"language": "x", "level": "y"}]`.

**Schema difference in `super-json.json`:** its `skills` is hierarchical (objects with `name`/`variations`/`frameworks`/`level`), not flat strings, and its `projects` carry extra `github`/`live`/`type` fields. It is a data source for humans and agents, **not** a valid input for `cv.py` rendering — always derive a flat tailored JSON from it. It also holds `profiles` (`short`/`medium`/`long`/`detailed`) and a `keywords` section grouped by role type for ATS work.

### File taxonomy

| File | Role |
|---|---|
| `super-json.json` | Master record. Every job, project, skill, keyword. Edit this first when new career facts land. |
| `cv_actualizado.json` → `daniel_banariba_cv.pdf` | Current general-purpose Spanish CV. |
| `cv_english.json` → `daniel_banariba_cv_english.pdf` | English counterpart; `section_titles` flipped to English. Keep in sync with the Spanish one. |
| `cv_<company>_<role>.json` → `daniel_banariba_cv_<company>.pdf` | Per-application tailored CVs. |
| `cv_automatico.json`, `cv_impactante.json`, `cv_completo_referencias.json`, `cv_data_ai.json` | Older variants kept for reference. |
| `cv_templates/` | Superseded copy of `cv.py` (custom 8.5"×11.2" page) and a sample JSON with full address. Reference only. |

The generator's console output and code comments are Spanish. CV **content** language is per-JSON — an English CV flips `section_titles`, `skill_labels`, and all prose.

## CV tailoring workflow

`README.md` contains the ATS prompt this project is built around. The rules that matter:

1. Analyze the job posting for exact keywords, required skills, and hard requirements.
2. Filter `super-json.json` down to what is relevant, reordering skill categories so the role's primary discipline leads.
3. Use the posting's **exact wording** — if it says "HTML5", write "HTML5", not "HTML"; if it says "Responsive Design", don't write "diseño adaptable". ATS matching is literal.
4. Write the tailored JSON, generate the PDF, then render and read the pages.

**Never invent experience.** If the posting requires something `super-json.json` does not back (a CMS, a framework, a certification), leave it out and tell the user the gap exists plainly. A keyword that wins a screening and loses the interview is worse than an honest omission.

## Foreign agent configs available to import

`~/.codex/config.toml` and `~/.gemini/settings.json` exist on this machine. If the user wants their MCP servers, slash commands, subagents, skills, or instructions brought into Claude Code, tell them to run `/import` to scan and list what's importable, then `/import --yes=<digest>` to apply it. Do not read those files or hand-write the config.
