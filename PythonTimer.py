import time
import datetime
import keyboard
import csv

def timeConvert(duration_seconds):
    total = int(duration_seconds)
    seconds = total % 60
    minutes = (total // 60) % 60
    hours = total // 3600
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def lapWriter(duration_seconds, filename):
    listing_time.append(duration_seconds)
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Lap', len(listing_time), duration_seconds])

def pauseWriter(startTC, pauseQty, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        elapsed = startTC - start_time
        writer.writerow(['Pause', pauseQty, elapsed])

start_time = time.perf_counter()
start_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
csv_filename = "Log.csv"


with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['EventType', 'EventNumber', 'Timestamp'])

print(f"Timer Started. Output will be saved to {csv_filename}")

try:
    listing_time = []
    stop_times = 0

    while True:
        time.sleep(0.00000000000001) 
        NowTimeCode = time.perf_counter()
        print(f"\rElapsed: {timeConvert(NowTimeCode - start_time)} ", end="", flush=True)
        
        if keyboard.is_pressed('l'):
            lapWriter(NowTimeCode - start_time, csv_filename)
            print(f",laps:{len(listing_time)}", flush=True) 
            while keyboard.is_pressed('l'): pass

        if keyboard.is_pressed("p"):
            stop_times += 1
            pausestart = time.perf_counter()
            pauseWriter(pausestart, stop_times, csv_filename)
            
            while not keyboard.is_pressed('r'):
                print(f"\rElapsed: {timeConvert(pausestart - start_time)} ,Paused", end="", flush=True)
                time.sleep(0.01)
            
            pauseend = time.perf_counter()

            start_time += (pauseend - pausestart)
            print("\r" + " " * 50 + "\r", end="", flush=True)
            while keyboard.is_pressed('r'): pass 

except KeyboardInterrupt:
    print("")
    ending_time = time.perf_counter()
    duration = ending_time - start_time

    print("Timer Stopped", end=", duration = ")
    print(timeConvert(duration))

    with open(csv_filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['TotalDuration', '', duration])
        writer.writerow(['End', '', ''])

    print("Will exit in 5 seconds")
    time.sleep(5)