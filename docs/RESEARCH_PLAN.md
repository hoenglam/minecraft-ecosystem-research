# Research plan

## Purpose and current stage

This project explores Minecraft Java Edition mods and modpacks on CurseForge as a setting for empirical research on innovation and platform ecosystems. It is currently a feasibility and research-design project. Access to the CurseForge API has not yet been approved, and no empirical findings or causal claims are reported in this repository.

The initial feasibility collection selected 100 projects from two modpack manifests. This selection is not representative of the whole platform. Historical archive coverage is incomplete and must not be interpreted as complete release histories.

## Candidate questions

- How are complementary projects connected through dependencies and modpack membership?
- How do version compatibility and project maintenance evolve together?
- How does reliance on shared libraries relate to project activity and adoption?
- Which observations can support comparisons over time, and which support only a cross-sectional description?

These are candidate directions, not preregistered hypotheses. Final questions will depend on verified coverage, access permissions, and measurement quality.

## Design principles

Use stable project and file identifiers when available. Keep project relations, file dependencies, and modpack membership in separate tables. Record collection time separately from release time and archive capture time. Preserve the source and any known coverage limits for every observation.

Missing observations do not mean zero downloads, no releases, or no dependencies. Cumulative downloads measured on one date cannot reconstruct a historical adoption trajectory. A later collection of public metadata does not establish what was visible at an earlier date.

## Planned stages

1. Document access conditions and the permitted collection, storage, and sharing scope.
2. Evaluate field availability and sampling coverage.
3. Implement an authorized metadata collection process with documented request limits and provenance.
4. Validate identifiers, dates, relationship types, and missingness.
5. Select research questions and methods supported by the resulting evidence.
6. Release reusable code and aggregate findings where permitted.

No raw research dataset or mod binaries are distributed through this repository.

