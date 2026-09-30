from pathlib import Path
import argparse
import time

def capture_frames(folder, seconds=5, interval=0.25):
    from mss import mss
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    end = time.time() + seconds
    count = 0
    with mss() as sct:
        monitor = sct.monitors[1]
        while time.time() < end:
            path = folder / f"frame-{count:05d}.png"
            sct.shot(mon=1, output=str(path))
            count += 1
            time.sleep(interval)
    return count

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", default="screen-recording")
    parser.add_argument("--seconds", type=int, default=5)
    args = parser.parse_args()
    print("Frames captured:", capture_frames(args.folder, args.seconds))
