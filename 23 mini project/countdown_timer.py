import time

def countdown(seconds, sleep=time.sleep):
    if seconds < 0:
        raise ValueError("seconds cannot be negative")
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        sleep(1)
    print("00:00")

if __name__ == "__main__":
    countdown(int(input("Seconds: ")))
