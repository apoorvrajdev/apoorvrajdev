# Hyperframes Composition Brief: Apoorv Raj — personal introduction

## Objective
A 50-60 s narrated, first-person introduction for the GitHub profile README. Polished tone, understated engineering
aesthetic, real product visuals, every claim traceable (see `brag-plan.md`, Fact sheet).

## Output
- Composition directory: `composition/`
- Rendered video: `apoorv-raj-introduction.mp4` (1920x1080, 30 fps, H.264 + AAC), poster `apoorv-raj-introduction.jpg`
- Duration: set by the six narration clips (`timing.json`)

## Source material
- Profile README (`../README.md`) for palette, badges and positioning; both resumes for career facts.
- `assets/img/fr-overview.png`, `assets/img/fr-alerts.png`: Fraud Radar demo (fraud-radar-lilac.vercel.app), 2026-10-18.
- `assets/img/cs-kitten-compare.png`: Caption Studio (image-captioning-system.vercel.app) after a real Compare both run.
- Copy that must appear verbatim: "Apoorv Raj"; "github.com/apoorvrajdev"; the two captions and latencies exactly as
  returned by the API; "AI Engineer (Independent Contractor, Founding Contributor)".

## Creative direction
- Tone: `polished`. Pacing: fast-in, long hold. No generic SaaS language, no fabricated logos or dashboards.
- Hook: name on beat 1, typed role line. Outro: name + "Backend engineering × applied AI" + GitHub URL.

## Visual identity
Background `#080a0f`; text `#eef1f6`; muted `#8b94a5`; accent `#4f8ef7`; glow `#2563eb`; captioning accent `#a78bfa`.
Fonts: Geist (display/body), Geist Mono (metrics), local woff2.

## Audio
- Music: `assets/music/happy-beats-business-moves-vol-12-by-ende-dot-app.mp3`, track 10, automation 0 to 0.30 fade-in,
  0.14 under each narration clip, 0.30 between, fade to 0 over the final second.
- Narration: `assets/voice/line-1..6.wav` on track 3, volume 1.0, one clip per scene.
- SFX (tracks 11+): `drop_001` (name), `impactSoft_medium_001` (dashboard landing), `drop_002` (caption cards),
  `bong_001` (close). Volumes 0.45-0.6.
- Audio-reactive: music RMS (`assets/music/rms-30fps.json`) breathes the main glow's scale/opacity. Subtle only.
- Beat sync: vol-12 preset grid; scene starts and chip reveals snapped to beats; two strong-cue locks.

## Hyperframes instructions
Single `index.html`, `data-composition-id="main"`, scenes as timed `<section>` clips on track 1, persistent untimed
background, GSAP paused timeline registered on `window.__timelines.main`. Gate: `hyperframes check` with zero errors;
render with `hyperframes render --quality high`.
