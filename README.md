# Minecraft Ecosystem Research

An exploratory academic project studying innovation and platform ecosystems through **Minecraft Java Edition mods and modpacks**, with an initial focus on publicly described projects on CurseForge.

## Purpose

This project examines what available metadata can reveal about the development, interdependence, and maintenance of community-created software. Potential questions include how projects evolve, how compatibility changes relate to maintenance activity, and how dependencies and modpack membership connect projects within an ecosystem. Specific empirical questions will be refined after assessing coverage and measurement quality.

This repository documents the research scope and planned data workflow and provides a small, reproducible validation example. It also supports an application for CurseForge API access.

## Current status

The project is at the **feasibility and data-design stage**. CurseForge API access has not been authorized, and this repository does not contain an API client. No research findings or publications are claimed.

An initial pilot considered 100 projects selected from two modpacks. That selection is not representative of the full Minecraft ecosystem. Historical archive coverage is incomplete; present-day metadata and archived observations must not be treated as a continuous historical record.

## Intended data scope

Subject to availability and applicable permissions, the planned scope includes:

- Project metadata, categories, descriptions, and observation timestamps.
- Release histories and compatibility with game versions and mod loaders.
- Publicly listed authors, contributors, and their project roles.
- Explicit project relationships, preserving their individual types.
- Modpack membership, recorded separately from project dependencies.

Each observation should retain its source and collection time. File-level relations, project-level relations, and modpack membership will be distinguished. Missing records, partial histories, and changing time coverage will be documented rather than interpreted as confirmed absence.

## Repository contents

| Path | Purpose |
| --- | --- |
| [`docs/RESEARCH_PLAN.md`](docs/RESEARCH_PLAN.md) | Research motivation, possible questions, and study limitations. |
| [`docs/DATA_PLAN.md`](docs/DATA_PLAN.md) | Planned fields, provenance, coverage, and data handling. |
| [`scripts/validate_metadata.py`](scripts/validate_metadata.py) | Local metadata validation demonstration. |
| [`examples/synthetic_projects.json`](examples/synthetic_projects.json) | Entirely synthetic example records. |

## Run the demonstration

Use Python 3 from the repository directory; no third-party dependencies are required:

```bash
python scripts/validate_metadata.py examples/synthetic_projects.json
```

The example performs local validation only. Its records are synthetic and are not evidence about real projects or creators.

## Data access and publication

API keys, raw research datasets, and mod binaries are excluded from this public repository. The intended outputs are research documentation, analysis code, and appropriately permitted summaries. Collection, retention, and redistribution remain subject to the permissions and terms agreed with the relevant data providers and rights holders. API access alone will not be treated as permission to redistribute data.
