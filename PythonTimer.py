from io import StringIO
import time
import datetime
import keyboard

def timeConvert(duration_seconds):
    total = int(duration_seconds)
    seconds = total % 60
    minutes = (total // 60) % 60
    hours = total // 3600
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def lapWriter(duration_seconds):
    listing_time.append(duration_seconds)
    with open("DurationList.txt", 'a', encoding='utf-8') as f:
        f.write("L")
        f.write(str((len(listing_time))))
        f.write('_')
        f.write(listing_time[-1] + '\n')
start_time = time.perf_counter()
start_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(f"Timer Started.")

try:
    listing_time = []

    while True:
        time.sleep(1)
        NowTimeCode = time.perf_counter()
        print(f"\rElapsed: {timeConvert(NowTimeCode - start_time)}", end="", flush=True)
        if(keyboard.is_pressed('l')):
            lapWriter(timeConvert(NowTimeCode - start_time))
            print(f"laps:{len(listing_time)}", flush=True) # Changed from listing_time.count() to len(listing_time)

       
except ImportError:
    print("You may not use the Lap function or more features.")

except KeyboardInterrupt:
    print("")
    ending_time = time.perf_counter()
    duration = ending_time - start_time

    print("Timer Stopped", end=", duration = ")
    print(timeConvert(duration))

    with open("DurationList.txt", 'a', encoding='utf-8') as f:
        f.write(timeConvert(duration) + "\n")
        f.write("end all" + "\n")

    print("Will exit in 5 seconds")
    time.sleep(5)