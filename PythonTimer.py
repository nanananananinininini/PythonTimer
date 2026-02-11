import os
import time

def timeConvert(duration_seconds):
    total = int(duration_seconds)
    seconds = total % 60
    minutes = (total // 60) % 60
    hours = total // 3600
    return f"{hours:02}:{minutes:02}:{seconds:02}"


start_time = time.time()
print("Timer Started.")
try:
    while True:
        time.sleep(1)
        print(timeConvert(time.time() - start_time))

except KeyboardInterrupt:
    ending_time = time.time()
    duration = ending_time - start_time

    print("Timer Stopped.", end=", duration = ")
    print(timeConvert(duration)

    with open("DurationList.txt", 'a', encoding='utf-8') as f:
        f.write(timeConvert(duration) + "\n")