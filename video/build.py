"""Fill composition/index.template.html from timing.json and the pre-extracted music RMS -> composition/index.html."""
import json, html
from pathlib import Path

root = Path(__file__).parent
timing = json.load(open(root / "timing.json"))
rms = json.load(open(root / "composition/assets/music/rms-30fps.json"))
sc = timing["scenes"]
end = timing["end"]
beat = timing["beat"]

# SFX moments (seconds)
sfx1 = 0.56                      # name lands (drop_001)
sfx2 = sc[2]["start"] + 0.35     # dashboard frame lands (impactSoft_medium_001)
sfx3 = sc[3]["start"] + 6.2      # live caption cards (drop_002)
sfx4 = sc[5]["start"] + 0.45     # close name (bong_001)

# Music automation: fade in, duck under every narration clip, fade out at the end.
pts = [{"t": 0, "v": 0}, {"t": 0.6, "v": 0.30}]
for s in sc:
    pts += [{"t": round(s["vo_start"] - 0.35, 3), "v": 0.30}, {"t": round(s["vo_start"], 3), "v": 0.14},
            {"t": round(s["vo_end"], 3), "v": 0.14}, {"t": round(s["vo_end"] + 0.45, 3), "v": 0.30}]
pts += [{"t": round(end - 1.3, 3), "v": 0.30}, {"t": round(end, 3), "v": 0}]
pts = sorted(pts, key=lambda p: p["t"])
automation = html.escape(json.dumps({"version": 1, "lanes": [{"target": "volume", "points": pts}]}), quote=True)

T = {"s%d" % (i + 1): s["start"] for i, s in enumerate(sc)}
T.update({"v%d" % (i + 1): s["vo_start"] for i, s in enumerate(sc)})
T.update({"ve%d" % (i + 1): s["vo_end"] for i, s in enumerate(sc)})
T.update({"end": end, "sfx1": sfx1, "sfx2": sfx2, "sfx3": sfx3, "sfx4": sfx4})

tpl = (root / "index.template.html").read_text(encoding="utf-8")
rep = {"{{END}}": str(end), "{{AUTOMATION}}": automation, "{{RMS}}": json.dumps(rms, separators=(",", ":")),
       "{{TIMING}}": json.dumps(T), "{{BEAT}}": str(round(beat, 5)),
       "{{SFX1}}": str(sfx1), "{{SFX2}}": str(round(sfx2, 3)), "{{SFX3}}": str(round(sfx3, 3)), "{{SFX4}}": str(round(sfx4, 3))}
for i, s in enumerate(sc, 1):
    rep["{{S%d}}" % i] = str(s["start"]); rep["{{D%d}}" % i] = str(s["duration"])
    rep["{{V%d}}" % i] = str(s["vo_start"]); rep["{{VD%d}}" % i] = str(s["vo_duration"])
out = tpl
for k, v in rep.items():
    out = out.replace(k, v)
assert "{{" not in out, [l for l in out.splitlines() if "{{" in l][:3]
(root / "composition/index.html").write_text(out, encoding="utf-8")
print("wrote composition/index.html — end", end, "sfx", sfx1, round(sfx2, 3), round(sfx3, 3), round(sfx4, 3))
