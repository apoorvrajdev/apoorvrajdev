# Brag plan — "Apoorv Raj: models into tested software"

Personal introduction video for the GitHub profile README of `apoorvrajdev`. Adapted from the `/brag`
product-launch workflow: same tooling (HyperFrames 0.8.58 + bundled music/SFX + Kokoro narration via
`hyperframes tts`), but a longer, narrated, first-person format (target 50-60 s) instead of a 15-25 s launch clip.

## Planning rubric

1. **What is it?** A software engineer's introduction: who Apoorv is, what they build, and two pieces of proof.
2. **Who is it for?** Technical recruiters, hiring managers and collaborators landing on the GitHub profile.
3. **Strongest claim?** Models are turned into tested, deployed software: APIs, data integrity, tests, CI/CD.
4. **Hook?** The name and a one-line role, landing on the first music beat, with the role line typed in.
5. **Show the thing:** real 1920x1080 screenshots of both deployed apps, captured on 2026-10-18 with Playwright
   (`landing.cjs`, `deep.cjs`), including a real greedy-vs-beam caption run returned by the deployed Space.
6. **Tone:** `polished`: understated, dark background, restrained blue accent, Geist type, deliberate motion.
7. **Format:** landscape 1920x1080, 30 fps.
8. **Audio:** music bed `happy-beats-business-moves-vol-12` (polished preset, 110 BPM) ducked under narration,
   four soft SFX, Kokoro `am_michael` narration (six clips, one per scene, speed 1.12).
9. **Outro:** name, one accurate engineering line, `github.com/apoorvrajdev`.

## Fact sheet (every on-screen or spoken claim and its source)

| Claim | Source |
|---|---|
| Python software engineer; backend, REST APIs, SQL, applied ML | Both resumes, header + summary |
| Node2.io: AI Engineer (Independent Contractor, Founding Contributor), Jan 2026-present; FastAPI AI service, LLM booking assistant (LangChain tool calling), complaint-prioritisation engine; Next.js + TypeScript app on PostgreSQL (Supabase) | Resume, Experience |
| IEEE paper *AI Narratives: Bridging Visual Content and Linguistic Expression*, ICSPCRE 2024 | Resume; DOI 10.1109/ICSPCRE62303.2024.10675203 (resolves) |
| Fraud Radar: 6 rules + XGBoost, SHAP per decision, p50 3.7 ms, 1,407 tests, idempotent ingestion, audit log | fraud-radar README (At a glance, Engineering notes) |
| Fraud Radar PR-AUC 0.93 synthetic held-out / 0.77 real ULB (284,807 rows) | fraud-radar README benchmark tables |
| Image Captioning: InceptionV3 + Transformer, FastAPI on Hugging Face Spaces, React on Vercel, 563 pytest + 27 Playwright, CI-gated deploys | image-captioning-system README (badges, Software checks, CI) |
| Captions "a cat is sitting on a keyboard of a computer" (greedy, 990.4 ms) / "a close up of a cat laying on a keyboard" (beam, 1748.4 ms), model v2.0.0 | Live responses captured by `deep.cjs` on 2026-10-18 |

Numbers deliberately **not** used: the resume's 420/14 test counts and 95,918-caption figure (superseded by the
repository), and any production, customer, scale or revenue figure (none exists).

## Visual identity

- Background `#080a0f`, text `#eef1f6`, muted `#8b94a5`, accent blue `#4f8ef7` (the profile's typing-SVG colour) with
  `#2563eb` glow, one restrained violet `#a78bfa` for the captioning scene (the app's own accent).
- Display and body: Geist; code/metrics: Geist Mono. Persistent grid + two drifting glows + vignette, glow breathing
  with music RMS (pre-extracted at 30 fps, `assets/music/rms-30fps.json`). No waveforms, no particles.

## Storyboard (exact timings in `timing.json`, computed from the measured narration clips)

### Scene 1 — Identity (hook)
Name "Apoorv Raj" lands on the first beat; role line "Software engineer · Python · backend · applied AI" types in;
small chips: `github.com/apoorvrajdev`, `B.E. CSE 2024`, `IEEE-published`.
Narration 1. Audio: music fades in, `drop_001` on the name.

### Scene 2 — Engineering focus
Six-node pipeline rail: REST API + validation, SQL data layer, ML inference, automated tests, CI/CD, Docker deploy.
A single pulse travels the rail and lights each node; caption "Models, then the software around them".
Narration 2. Sequential: nodes arrive on consecutive beats, then hold.

### Scene 3 — Fraud Radar
Real Overview dashboard screenshot in a browser frame with a slow push-in; the Alerts queue crossfades in.
Metric chips: `6 rules + XGBoost`, `SHAP per decision`, `p50 3.7 ms`, `1,407 tests`, and the evaluation line
`PR-AUC 0.93 synthetic held-out · 0.77 real (ULB)`. Narration 3. SFX: `impactSoft_medium_001` on the frame landing.

### Scene 4 — Image Captioning
Real Caption Studio screenshot (kitten example, Compare both), push-in toward the two caption cards with their
measured latencies. Chips: `InceptionV3 + Transformer`, `FastAPI · Hugging Face Spaces`, `React · Vercel`,
`563 pytest + 27 Playwright`, `IEEE ICSPCRE 2024`. Narration 4. SFX: `drop_002` on the caption cards.

### Scene 5 — Node2.io
Text card (no employer logo, nothing fabricated): role title exactly as on the resume, Jan 2026 - present, four
bullets from the resume. Narration 5. Sequential: bullets on alternate beats.

### Scene 6 — Close
"Apoorv Raj" · "Backend engineering × applied AI" · `github.com/apoorvrajdev` · LinkedIn · portfolio. Narration 6.
`bong_001` under the name; music fades out over the last second.

## Music cue guidance
Preset `happy-beats-business-moves-vol-12` (109.96 BPM, beat 0.5457 s). Scene starts are snapped to the beat grid
(within 0.10 s); the name reveal and the close are the two strong-cue locks. The readability floor applies to every
chip row: reveal on alternate beats, then hold the full set.

## Voiceover script
See `narration-script.md`. Music ducks to 0.14 under each clip and returns to 0.30 between clips.
