# Data scope and management plan

This is a proposed research data model, not a guarantee that every field is available through the CurseForge API. Availability and allowed uses must be confirmed before collection. No API access or data-sharing permission is implied by this repository.

| Unit | Candidate fields | Interpretation and coverage notes |
| --- | --- | --- |
| Project | ID, slug, name, category, creation/update dates, status, cumulative downloads, public links | Store the observation time. A present-day count is not a historical series. |
| Release/file | File ID, project ID, publication date, release type, game versions, loaders | Keep version labels and dates as supplied; distinguish unavailable history from no releases. |
| Public project participation | Public author/profile identifiers and displayed project roles | Collect only research-relevant public information, subject to permission. Roles may change. |
| Project relation | Source and target project IDs, original relation label, observation time | Preserve direction and the source's classification. |
| File dependency | Source file ID, target project/file ID if available, dependency type | File-level dependencies must not be merged silently with project-level relations. |
| Modpack membership | Modpack ID, manifest version, project/file IDs | Co-membership is distinct from a dependency. |
| Provenance/coverage | Retrieval time, archive capture time, source URL/type, page coverage, failure status | Collection failures and incomplete lists remain explicitly marked. |

## Access and storage

The project seeks authorized access for non-commercial academic research. Before collecting at scale, confirm permitted retention, caching, request volume, and publication practices with the data provider. A granted API key alone will not be treated as blanket permission to redistribute data.

Any collected raw records will remain outside this public repository. Future public releases may include code, documentation, synthetic examples, and permitted aggregate results. Credentials are kept outside version control. Data retention and deletion arrangements will follow the applicable permissions agreed with the provider.

## Synthetic validation example

`examples/synthetic_projects.json` contains invented records only. It illustrates a small normalized model, not a raw API response or research result. Project IDs are strings, observations use timezone-aware ISO 8601 timestamps, downloads are non-negative integers or `null`, and relationships retain a type and observation time.

The example validator checks these basic structural conditions, duplicate project IDs, and relationship endpoints. It does not assess sampling representativeness, source reliability, API compatibility, or permission to collect or share data. Its example relationship labels are illustrative and are not a complete provider taxonomy.

