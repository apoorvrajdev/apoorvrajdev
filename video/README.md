# Introduction video — production notes

`apoorv-raj-introduction.mp4` is the narrated, 58-second personal introduction embedded at the top of the profile
README. It was produced on 2026-10-18 with the [Brag](https://github.com/latent-spaces/brag) workflow adapted for a
personal introduction, rendered by HyperFrames 0.8.58, and narrated with Kokoro-82M through `hyperframes tts`.

## Deliverables

| File | Where | Details |
|---|---|---|
| `apoorv-raj-introduction-web.mp4` | [GitHub Release `intro-video-v1`](https://github.com/apoorvrajdev/apoorvrajdev/releases/tag/intro-video-v1), and the README link | 1920×1080, 30 fps, 1,752 frames, 58.40 s, H.264 (CRF 25) + AAC 128 kbps 48 kHz stereo, 7.7 MB, faststart. Under GitHub's 10 MB free-plan video attachment limit, so it can be dragged into the README web editor to get an inline player. Frame 0 is the poster. |
| `apoorv-raj-introduction.mp4` | same release | Higher-bitrate 1080p encode (CRF 22), 11.5 MB |
| `apoorv-raj-introduction.jpg` | same release | Clean poster frame (scene 1 at 6.7 s), 1920×1080 |
| `assets/introduction-poster.jpg` | this repository | The README thumbnail: the poster frame plus a play affordance |

Validation performed on the delivered MP4s (the 7.7 MB web encode was re-checked the same way, plus a VMAF comparison against the 35.5 MB master): `hyperframes check` passed with zero errors (runtime, layout, motion and
53/53 WCAG AA contrast checks); `ffprobe` confirms the dimensions, frame rate, frame count, duration and audio
stream; a full `ffmpeg` decode reports no errors; frame 0 matches the poster at PSNR 46 dB; loudness inside the six
narration windows averages about −24 dB versus about −31 dB in the music-only gaps, so the narration is present and
audible; peak −3 dB.

## What is real

- Scenes 3 and 4 show 1920×1080 screenshots of the deployed apps, captured headless with Playwright on 2026-10-18
  (`landing.cjs`, `deep.cjs`): the Fraud Radar demo at fraud-radar-lilac.vercel.app (Overview and Alerts) and Caption
  Studio at image-captioning-system.vercel.app after a real *Compare both* run on the kitten example.
- The two captions and latencies in scene 4 are the unedited responses from the deployed Hugging Face Space during
  that run: greedy `"a cat is sitting on a keyboard of a computer"` (990.44 ms) and beam
  `"a close up of a cat laying on a keyboard"` (1748.44 ms), model `v2.0.0`.
- Every metric and job description comes from the resume or the project READMEs; `brag-plan.md` lists each claim
  with its source. No employer logo, dashboard, endorsement or customer figure was invented.

## Audio

- Narration: Kokoro-82M voice `am_michael`, speed 1.2, six clips (one per scene) generated with `make-voice.sh`;
  the spoken text is in `narration-script.md`. Music ducks to 0.14 under each clip.
- Music: *Happy Beats / Business Moves vol. 12* by ende.app, bundled with the Brag skill for this use.
- SFX: four CC0 Kenney.nl cues bundled with Brag (`drop_001`, `impactSoft_medium_001`, `drop_002`, `bong_001`).

## Reproducing the render

The committed source is deliberately slim; the media it references is not in this repository.

1. Install the Brag skill (fonts, music and SFX come with it) and HyperFrames 0.8.x; install Kokoro for narration
   (`pip install kokoro-onnx soundfile` in a venv, then `HYPERFRAMES_PYTHON=<that python>`).
2. Create `composition/assets/{fonts,vendor,music,sfx,img,voice}` and copy in Geist/Geist Mono woff2, `gsap.min.js`,
   the vol-12 MP3 and the four SFX files from the Brag skill.
3. Capture the screenshots: `node landing.cjs <dir>` and `node deep.cjs <dir>`, then copy `fr-overview.png`,
   `fr-alerts.png` and `cs-kitten-compare.png` into `composition/assets/img/`.
4. `bash make-voice.sh` (narration), `python rms.py <mp3> 62 > composition/assets/music/rms-30fps.json`,
   `python timing.py` (beat-snapped scene timings from the clip lengths), `python build.py` (fills
   `index.template.html` into `composition/index.html`).
5. `npx hyperframes check` in `composition/`, then `npx hyperframes render --quality high`.
6. Poster and delivery encode: extract the settled scene-1 frame with ffmpeg, bake it as frame 0 and re-encode at
   CRF 22 (commands in the production run's shell history; see the Brag `step-4-deliver.md` reference).

`composition/index.html` is the exact built composition that was rendered.
