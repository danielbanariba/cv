# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python-based CV/resume generation system: JSON data → PDF via ReportLab. Uses a "master + variants" pattern where `super-json.json` holds all professional data, and tailored JSON files are AI-filtered subsets for specific job applications.

## Commands

```shell
# Activate virtual environment
source .venv/bin/activate  # bash/zsh
source .venv/bin/activate.fish  # fish

# Generate PDF (default output: cv_generado.pdf)
python cv.py --json-file ./cv_actualizado.json --output-file cv.pdf

# Validate content limits without generating PDF
python cv.py --json-file ./cv_actualizado.json --only-validate

# Generate with defaults
python cv.py --json-file ./super-json.json
```

Only dependency: `reportlab` (installed in `.venv/`, Python 3.14).

## Architecture

### cv.py Pipeline

1. **`load_json()`** → Parse JSON with error handling
2. **`validate_cv_content()`** → Check against `CV_LIMITS` (warnings only — PDF still generates if limits exceeded)
3. **`setup_styles()`** → Configure all ReportLab ParagraphStyles (base_font_size param adjusts globally)
4. **`build_cv_content()`** → Build PDF story: personal info → profile → experience → skills → projects → education → certifications → languages → references
5. **`generate_cv_pdf()`** → Render to PDF (custom page: 8.5" × 11.2", taller than letter to fit more content; margins: 0.5" sides, 0.2" top, 0.5" bottom)

### Content Limits (CV_LIMITS)

Profile: 500 chars | Jobs: 3 max, 5 responsibilities each (120 chars) | Projects: 4 | Education: 3 | Certifications: 4 | Skills/category: 8

These are **recommendations**, not hard blocks. The system warns but generates anyway.

### JSON Schema

Tailored CV files use this structure:

```json
{
  "personal_info": { "name", "email", "phone", "location", "website", "github", "linkedin" },
  "profile": "string",
  "experience": [{ "company", "position", "date_range", "location", "responsibilities": [], "technologies" }],
  "skills": { "languages": "string", "frameworks": "string", "databases": "string", "cloud": "string", ... },
  "projects": [{ "title", "description", "technologies" }],
  "education": [{ "institution", "degree", "date_range", "location" }],
  "certifications": ["string"],
  "languages": ["Español: Nativo", "Inglés: B2"],  // also accepts [{"language": "x", "level": "y"}]
  "references": [{ "name", "position", "company", "phone" }],
  "section_titles": { "experience", "skills", "projects", ... },
  "skill_labels": { "languages", "frameworks", "databases", ... }
}
```

**Important schema difference:** `super-json.json` uses a hierarchical skills structure with objects containing `name`, `variations`, `frameworks`, `level` fields. Tailored JSONs use simplified comma-separated strings per category. The `build_cv_content()` function handles both formats.

`super-json.json` also has a `profiles` object with `short`/`medium`/`long`/`detailed` variants, and a `keywords` section categorized by role type for ATS optimization.

### `cv_templates/`

Contains older/variant versions of `cv.py` and sample JSON files (e.g., `cv_con_direccion.json` with full address). Reference only — the root `cv.py` is the active generator.

## Key Conventions

- **Language:** All UI output, comments, section titles, and content are in **Spanish**
- **Section titles customizable** via `section_titles` dict in JSON (e.g., "EXPERIENCIA LABORAL")
- **Skill labels customizable** via `skill_labels` dict (e.g., "Lenguajes", "Frameworks")
- **Safe access:** Use `get_value(data, key, default)` helper for dictionary lookups
- **Conditional rendering:** Sections only render if their data exists in the JSON
- **Table layouts:** Experience uses [Company | Date] columns, Education uses [Institution | Location]

## CV Optimization Workflow

The README.md contains a prompt for AI-assisted CV tailoring:
1. Analyze job posting for keywords and requirements
2. Filter `super-json.json` to match the role
3. Use **exact keywords** from the job posting (never synonyms — critical for ATS)
4. Output a tailored JSON file for PDF generation
