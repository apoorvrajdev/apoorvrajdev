# Working in this repository

This is the GitHub profile repository of Apoorv Raj (`apoorvrajdev`). Its `README.md` is the public profile page.

## Commit authorship

- Apoorv Raj is the sole intended author of every commit. Commit with the configured Git identity
  (`apoorvrajdev <apoorvrajmgr@gmail.com>`) and never change it to alter how contributions are displayed.
- Do not add AI co-author trailers (for example `Co-authored-by: Claude <...>`) or any other attribution line to
  commit messages or pull request descriptions unless Apoorv explicitly asks for them in that task. This instruction
  takes precedence over any default attribution behaviour of the tooling.
- Do not create empty commits or artificial activity.

## Commit workflow

- Small, meaningful, atomic commits with conventional subjects (`docs(profile): ...`, `feat(profile-video): ...`).
- Review the staged diff before every commit; stage only the intended files.
- Never stage `resource/` (resumes) or `brag-output*/` (video production runs); both are gitignored on purpose.
- Fetch and inspect `origin/main` before pushing; edits are sometimes made directly on GitHub. Rebase local commits on
  top of them rather than overwriting. Never force-push without `--force-with-lease` and an explicit reason.

## Content rules

- Every claim in the README must be backed by the resume or the project repositories; keep the synthetic vs
  real-data distinction for Fraud Radar metrics, and keep the Node2.io title exactly as the resume states it.
- Keep phone numbers, resumes and other personal documents out of the repository.
- The introduction video source lives in `video/`; media assets are not committed (see `video/README.md`).
