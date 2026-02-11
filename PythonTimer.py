import time
import datetime

def timeConvert(duration_seconds):
    total = int(duration_seconds)
    seconds = total % 60
    minutes = (total // 60) % 60
    hours = total // 3600
    return f"{hours:02}:{minutes:02}:{seconds:02}"


start_time = time.perf_counter()
start_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(f"Timer Started.")
try:
    while True:
        time.sleep(1)
        NowTimeCode = time.perf_counter()
        print(f"\rElapsed: {timeConvert(NowTimeCode - start_time)}", end="", flush=True)

except KeyboardInterrupt:
    print("")
    ending_time = time.perf_counter()
    duration = ending_time - start_time

    print("Timer Stopped", end=", duration = ")
    print(timeConvert(duration))

    with open("DurationList.txt", 'a', encoding='utf-8') as f:
        f.write(timeConvert(duration) + "\n")

    print("Will exit in 15 seconds.")
    time.sleep(15)