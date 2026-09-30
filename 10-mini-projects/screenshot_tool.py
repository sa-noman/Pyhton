from pathlib import Path
from datetime import datetime

def take_screenshot(folder="."):
    from PIL import ImageGrab
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    filename = folder / f"screenshot-{datetime.now():%Y%m%d-%H%M%S}.png"
    ImageGrab.grab().save(filename)
    return filename

if __name__ == "__main__":
    print(take_screenshot())
