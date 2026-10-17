"""Per-frame music RMS (0-100) for the first N seconds at 30 fps, via ffmpeg astats."""
import subprocess, sys, re, json
src, secs = sys.argv[1], float(sys.argv[2])
cmd = ["ffmpeg", "-hide_banner", "-nostats", "-t", str(secs), "-i", src, "-ac", "1", "-ar", "44100",
       "-af", "asetnsamples=1470,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-", "-f", "null", "-"]
out = subprocess.run(cmd, capture_output=True, text=True).stdout
vals = [float(m) for m in re.findall(r"RMS_level=(-?[0-9.]+|-inf)", out.replace("-inf", "-90"))]
lin = [10 ** (v / 20) for v in vals]
peak = max(lin) or 1
rms = [round(100 * v / peak) for v in lin]
print(json.dumps(rms))
