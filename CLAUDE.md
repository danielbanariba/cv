# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a CV generation system written in Python that creates PDF resumes from JSON data. The system includes:

- A Python script (`cv.py`) for PDF generation using ReportLab
- JSON templates for storing CV data (`super-json.json`, `cv_actualizado.json`, etc.)
- A CV optimization prompt workflow for tailoring resumes to specific job offers

## Core Architecture

### Main Components

- **cv.py**: Main PDF generator script using ReportLab
  - Uses modular content validation with `CV_LIMITS` constants
  - Builds PDF using `build_cv_content()` and styled paragraphs
  - Validates content against recommended limits for one-page CVs

- **JSON Data Structure**: All CV files follow this schema:
  ```json
  {
    "personal_info": {},
    "profile": "",
    "experience": [],
    "skills": {},
    "projects": [],
    "education": [],
    "certifications": [],
    "languages": [],
    "section_titles": {},
    "skill_labels": {}
  }
  ```

- **super-json.json**: Master CV file containing all professional information
- **Specialized JSONs**: Tailored versions for specific job applications

## Common Development Commands

### Generate CV PDF
```shell
python cv.py --json-file ./cv_actualizado.json --output-file cv.pdf
```

### Validate CV Content Only
```shell
python cv.py --json-file ./cv_actualizado.json --only-validate
```

### Generate with Default Settings
```shell
python cv.py --json-file ./super-json.json
```

## CV Content Limits

The system enforces these limits for optimal one-page formatting:
- Profile: 500 characters max
- Experience: 3 jobs max, 5 responsibilities each
- Projects: 4 max
- Education: 3 entries max
- Certifications: 4 max
- Skills per category: 8 max
- Responsibility length: 120 characters max

## Workflow for CV Optimization

The README.md contains a comprehensive prompt for CV optimization using AI:
1. Analyze job offer for keywords and requirements
2. Filter super-json.json to match job-specific needs
3. Use exact keywords from job posting (not synonyms)
4. Generate tailored JSON for PDF creation

## File Structure

- `cv_templates/`: Template files and variations
- `generated_cvs/`: Output directory for generated PDFs
- `env/`: Python virtual environment
- Various JSON files: Different CV versions and configurations

## Python Dependencies

The project uses ReportLab for PDF generation with these key imports:
- `reportlab.lib.colors`
- `reportlab.platypus` (SimpleDocTemplate, Paragraph, etc.)
- `reportlab.lib.styles`
- Standard library: `json`, `argparse`