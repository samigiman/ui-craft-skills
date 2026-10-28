# What validation establishes

| Check | Establishes | Does not establish |
| --- | --- | --- |
| `scripts/validate.py` | Six expected skill folders, valid frontmatter, consistent UI metadata and resolvable local links. | Good visual judgement or complete agent compatibility. |
| Scanner behavior tests | Read-only source triage, bounded output, exclusions and no quality verdict. | Detection of AI authorship or all visual problems. |
| Installer tests | Correct copying, visible dry run, explicit selection, no overwrite and preflight conflict handling. | Automatic skill discovery in every agent/version. |
| CI | Those automated checks passed for the tested commit/runtime. | A real application's accessibility, responsiveness or client approval. |

The instructions call for rendered comparison and actual task-state checks when
used on a project. This repository does not bundle an independent evaluation of
model design quality or claim measurable conversion improvements.

The examples are generalized instructional cases. No client assets, private
conversation exports, account identifiers or local machine audit manifests are
included in this public collection.

Installation and helper execution use only the Python standard library. Structural
validation needs the development dependency in `requirements-dev.txt`.
