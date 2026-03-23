#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_brief(title: str, pages: str, aspect: str, language: str) -> str:
    return f"""# Brief

## Topic
{title}

## Audience
- [Fill in target audience]

## Goal
- [Fill in the presentation goal]

## Slide Count
{pages}

## Aspect Ratio
{aspect}

## Language
{language}

## Style Keywords
- [Fill in target look and tone]

## Style Red Flags
- [Fill in what to avoid]

## Constraints
- [Fill in constraints]

## Core Narrative
1. [Opening idea]
2. [Middle logic]
3. [Ending takeaway]
"""


def build_manuscript() -> str:
    return """# Outline

## Slide 1

### Core Insight
[Write the one thing the audience should remember]

### Evidence
- [Key fact]
- [Key figure]

### Visual Direction
- [Chart / diagram / image / comparison]

## Slide 2

### Core Insight
[Write the next one thing the audience should remember]

### Evidence
- [Key fact]
- [Key figure]

### Visual Direction
- [Chart / diagram / image / comparison]
"""


def build_style_draft() -> str:
    return """# Style Draft

## Theme Positioning
- [What is the presentation trying to assert]

## Audience and Use Scene
- [Who will see it and in what setting]

## Desired Tone
- [e.g. board-level, keynote, editorial, security report]

## Desired Visual Cues
- [e.g. calm, severe, premium, dense, open, technical]

## Must Avoid
- [e.g. noisy backgrounds, too many badges, overdone gradients]

## Representative Sample Page
- [Which page should be used for the 3 style options]

## Approval Status
- Pending user confirmation
"""


def build_style_decision() -> str:
    return """# Style Decision

## Selected Option
- [Option A / Option B / Option C / Mixed]

## What To Keep
- [List selected traits]

## What To Remove
- [List rejected traits]

## User Confirmation
- Pending
"""


def build_template_choice() -> str:
    return """# Template Choice

## Candidate Templates
- [Template name]
- [Template name]
- [Template name]

## Why They Fit
- [Brief fit reason]

## Rejected Templates
- [Template name]: [Reason]

## Final 3 Used For Concepts
- [Option A template]
- [Option B template]
- [Option C template]
"""


def build_page_family_plan() -> str:
    return """# Page Family Plan

在开始整套生成前，先把每页的身份和节奏分配清楚。

| Slide | Role | Page Family | Density | Template Reference | Emphasis Mode |
|------|------|-------------|---------|--------------------|---------------|
| 1 | Opening claim | cover | low |  | hero title / manifesto |
| 2 | Core conclusion | core_conclusion | medium |  | strong judgment bar |
| 3 | Mechanism / system | process / system_diagram | medium |  | flow / relation |
| 4 | Evidence / contrast | comparison / matrix | medium |  | contrast |
| 5 | Risks / limits | risks | medium |  | warning row |
| 6 | Closing / action | summary | low-medium |  | conclusion block |

## Rules

- No more than 2 consecutive slides from the same page family.
- Adjacent slides should differ in at least 2 dimensions:
  - page family
  - density
  - card grammar
  - background treatment
  - emphasis mode
- For a 8-15 page deck, include at least:
  - 1 cover
  - 1 core_conclusion
  - 1 process or system_diagram
  - 1 comparison or matrix
  - 1 risks or limitation page
  - 1 summary
"""


def build_screen_copy() -> str:
    return """# Screen Copy

先在这里精修所有会上屏的文字，再开始生成 SVG。

## Slide 1

### Slide Title
[Keep it short and presentation-ready]

### Slide Subtitle
[Optional; compress context into one short sentence]

### Hero Lines
- [Line 1]
- [Line 2]
- [Line 3]

### Sections

#### Section A
- Title: [Short section title]
- Bullet 1: [16-28 Chinese characters or equivalent]
- Bullet 2: [16-28 Chinese characters or equivalent]

#### Section B
- Title: [Short section title]
- Bullet 1: [16-28 Chinese characters or equivalent]
- Bullet 2: [16-28 Chinese characters or equivalent]

### Cards

#### Card 1
- Title: [8-14 Chinese characters or equivalent]
- Line 1: [Short line]
- Line 2: [Short line]

#### Card 2
- Title: [8-14 Chinese characters or equivalent]
- Line 1: [Short line]
- Line 2: [Short line]

### Footer
- Source line: [One compact source line]
- Note line: [One compact note line]

## Editing Rules

- Do not paste source material paragraphs directly into this file.
- Rewrite for screen reading first; layout comes later.
- If a box feels crowded, shorten the copy before touching font size.
"""


def build_design_plan(aspect: str) -> str:
    return f"""# Design Spec

## Canvas
- Aspect ratio: {aspect}
- Use fixed-layout slide thinking, not responsive web thinking
- Default SVG artboard should stay consistent across all slides

## Visual System
- [Primary color]
- [Secondary color]
- [Accent color]
- [Font choice]
- [Mood]

## Style Tokens
- color_scheme:
  - background
  - text
  - muted
  - panel
  - accent
- typography:
  - heading_font
  - body_font
  - cjk_font
  - mono_font
- card_style:
  - border_radius
  - border
  - shadow
  - gap
- gradients:
  - hero
  - highlight
  - terminal emphasis
- elevation:
  - subtle
  - medium
  - strong
- decoration:
  - pattern
  - pattern_opacity
  - icon_style

## Slide Type Overrides
- cover:
  - [How cover pages differ]
- core_conclusion:
  - [How claim pages differ]
- comparison:
  - [How comparison pages differ]
- dashboard:
  - [How dashboard pages differ]
- process:
  - [How process pages differ]
- matrix / system_diagram:
  - [How structure pages differ]
- risks:
  - [How risks pages differ]
- summary:
  - [How closing pages differ]

## Layout Rules
- One slide, one core insight
- Prefer stable spacing and strong hierarchy
- Use Bento Grid only when content naturally splits into blocks
- Keep images and diagrams as content, not decoration
- Define text budgets for major containers before drawing the slide
- Match the selected page family for each slide in `page_family_plan.md`

## SVG Rules
- One file per slide
- Fixed viewBox
- Inline styling only
- No script, no external CSS
- Preserve readable type before adding more text
"""


def build_svg_placeholder(index: int) -> str:
    return f"""<svg width="1600" height="900" viewBox="0 0 1600 900" xmlns="http://www.w3.org/2000/svg">
  <rect width="1600" height="900" fill="#F5F7FA"/>
  <text x="90" y="120" font-size="40" font-weight="700" fill="#12344D">Slide {index:02d}</text>
  <text x="90" y="180" font-size="22" fill="#52606D">Replace this placeholder with the final SVG for this slide.</text>
</svg>
"""


def build_legacy_manuscript_note() -> str:
    return """# Notes

- Confirm `brief.md` and `style_draft.md` with the user first.
- Check `templates/TEMPLATE_LIBRARY.md` before drawing the 3 concept pages.
- Write `template_choice.md` to record which templates were shortlisted and why.
- Generate 3 style options under `concepts/` before the full deck.
- Render each SVG to a preview image and inspect the image before finalizing.
- Use `outline.md` for page planning after style approval.
- Generate one SVG per slide under `slides/`.
- If the user later requests `.pptx`, import or convert the SVG set after validation.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize a PPT task workspace.")
    parser.add_argument("output_dir", help="Workspace directory to create")
    parser.add_argument("--title", default="Untitled Presentation")
    parser.add_argument("--pages", default="8-12")
    parser.add_argument("--aspect", default="16:9")
    parser.add_argument("--language", default="zh")
    args = parser.parse_args()

    root = Path(args.output_dir).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    for name in ["assets", "concepts", "notes", "previews", "slides", "outputs", "source"]:
        (root / name).mkdir(exist_ok=True)

    write_file(
        root / "brief.md",
        build_brief(args.title, args.pages, args.aspect, args.language),
    )
    write_file(root / "style_draft.md", build_style_draft())
    write_file(root / "style_decision.md", build_style_decision())
    write_file(root / "template_choice.md", build_template_choice())
    write_file(root / "page_family_plan.md", build_page_family_plan())
    write_file(root / "outline.md", build_manuscript())
    write_file(root / "screen_copy.md", build_screen_copy())
    write_file(root / "design_spec.md", build_design_plan(args.aspect))
    write_file(root / "notes.md", build_legacy_manuscript_note())
    for option in ["a", "b", "c"]:
        write_file(root / "concepts" / f"option_{option}.svg", build_svg_placeholder(0))
    for idx in range(1, 4):
        write_file(root / "slides" / f"slide_{idx:02d}.svg", build_svg_placeholder(idx))
    write_file(
        root / "run_notes.md",
        "# Run Notes\n\n- Route: single-model-svg\n- Status: initialized\n- Waiting for style approval: yes\n",
    )

    print(root)


if __name__ == "__main__":
    main()
