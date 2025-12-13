import subprocess
import sys

def run(cmd):
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    try:
        run([sys.executable, "src/data_collection/download_audio.py"])
        run([sys.executable, "src/data_collection/transcribe_audio.py"])
        print("Pipeline completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Pipeline failed.")
        sys.exit(e.returncode)
