#!/usr/bin/env bash
# Regenerates the six narration clips with Kokoro through HyperFrames.
# Requires: HYPERFRAMES_PYTHON pointing at a Python with `kokoro-onnx soundfile` installed.
set -euo pipefail
HF="${HF_BIN:-$HOME/AppData/Local/npm-cache/_npx/702923228c2ce1e6/node_modules/hyperframes/bin/hyperframes.mjs}"
VOICE="${VOICE:-am_michael}"
SPEED="${SPEED:-1.2}"
DIR="$(cd "$(dirname "$0")" && pwd)/composition/assets/voice"
mkdir -p "$DIR"
i=0
while IFS= read -r line; do
  i=$((i+1))
  [ -z "$line" ] && continue
  HYPERFRAMES_NO_UPDATE_CHECK=1 node "$HF" tts "$line" --voice "$VOICE" --speed "$SPEED" --output "$DIR/line-$i.wav" --json
done <<'LINES'
Hi, I'm Apoorv Raj, a software engineer focused on Python, backend systems, and applied AI.
I turn machine-learning models into software people can actually use: clear A-P-I's, reliable data, automated tests, and repeatable deployments.
Fraud Radar scores card transactions in real time, combining six business rules with an X-G-Boost model, and explaining every decision with SHAP.
My Image Captioning System takes the C-N-N Transformer model from my I-triple-E published research into a tested Fast-A-P-I service and React app.
At Node two dot I-O, I build Fast-A-P-I AI services, including an L-L-M booking assistant, and features in a Next J-S app on Postgres.
I care about engineering beyond the demo: correctness, evaluation, and getting the details right. I'm Apoorv Raj. Explore my work on GitHub.
LINES
