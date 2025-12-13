import subprocess
from pathlib import Path

AUDIO_DIR = Path("data/audio")
SUBS_DIR = Path("data/subtitles")
MODEL = "large-v3" # tiny/base/small/medium/large/large-v2/large-v3/turbo
FORMAT = "srt" # subtitles format

SUBS_DIR.mkdir(exist_ok=True)

for wav in sorted(AUDIO_DIR.glob("*.wav")):
    out_srt = SUBS_DIR / f"{wav.stem}.{FORMAT}"
    if out_srt.exists():
        print(f"Skipping (already exists): {out_srt.name}")
        continue

    cmd = [
        "whisper",
        str(wav),
        "--model", MODEL,
        "--output_format", FORMAT,
        "--output_dir", str(SUBS_DIR),
    ]

    print(f"Transcribing: {wav.name}")
    subprocess.run(cmd, check=True)
