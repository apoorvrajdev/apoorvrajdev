"""Compute scene/narration timings from the measured clip durations; snap scene starts to the vol-12 beat grid."""
import json, subprocess, re
BEAT = 60 / 109.96
beats = [round(0.56 + i * BEAT, 3) for i in range(0, 140)]
def snap(t):
    return min(beats, key=lambda b: abs(b - t))
clips = []
for i in range(1, 7):
    f = f"composition/assets/voice/line-{i}.wav"
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout)
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", f, "-af", "silencedetect=n=-45dB:d=0.15", "-f", "null", "-"], capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", out)]
    ends = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", out)]
    # speech end = start of a trailing silence that never ends, else full duration
    speech_end = dur
    if starts and (len(ends) < len(starts)):
        speech_end = starts[-1]
    clips.append({"file": f, "duration": round(dur, 3), "speech_end": round(speech_end, 3)})
LEAD = 0.35   # scene start -> narration start
TAIL = 0.40   # narration end -> next scene start
scenes = []
t = 0.0
for i, c in enumerate(clips):
    start = 0.0 if i == 0 else snap(t)
    vo_start = round(start + LEAD, 3)
    vo_dur = round(c["duration"], 3)
    vo_end = round(vo_start + vo_dur, 3)
    scenes.append({"scene": i + 1, "start": round(start, 3), "vo_start": vo_start, "vo_duration": vo_dur, "vo_end": vo_end})
    t = vo_end + TAIL
end = snap(scenes[-1]["vo_end"] + 1.7)
for i, s in enumerate(scenes):
    nxt = scenes[i + 1]["start"] if i + 1 < len(scenes) else end
    s["duration"] = round(nxt - s["start"] + (0.7 if i + 1 < len(scenes) else 0), 3)  # overlap for the push transition
json.dump({"beat": BEAT, "clips": clips, "scenes": scenes, "end": end}, open("timing.json", "w"), indent=1)
print(json.dumps(scenes, indent=0)); print("END", end)
