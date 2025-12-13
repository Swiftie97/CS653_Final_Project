import subprocess
from pathlib import Path

URLS_FILE = Path("data/audio/urls.txt")
OUT_DIR = Path("data/audio")

OUT_DIR.mkdir(exist_ok=True)

with URLS_FILE.open("r", encoding="utf-8") as f:
    for idx, line in enumerate(f):
        url = line.strip()
        if not url:
            continue

        prefix = f"{idx:04d}"  # Add prefix to file name

        cmd = [
            "yt-dlp",
            "-x",
            "--audio-format", "wav",
            "-o", str(OUT_DIR / f"{prefix}_%(title)s [%(id)s].wav"),
            url,
        ]

        print(f"[{prefix}] Downloading: {url}")
        subprocess.run(cmd, check=True)
