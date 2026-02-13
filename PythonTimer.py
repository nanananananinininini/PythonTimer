# -*- coding: utf-8 -*-
import time
import datetime
import keyboard
import csv

# =================================================================================

def timeConvert(duration_seconds): # convert time to HH:MM:SS
    total = int(duration_seconds)
    seconds = total % 60
    minutes = (total // 60) % 60
    hours = total // 3600
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def lapWriter(duration_seconds, filename): # write lap records into the csv file
    listing_time.append(duration_seconds)
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Lap', len(listing_time), duration_seconds])

def pauseWriter(startTC, pauseQty, filename): # write pause records into the csv file
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        elapsed = startTC - start_time
        writer.writerow(['Pause', pauseQty, elapsed])

def resumeWriter(resumeTC, resumeQty, filename): # write resume records into the csv file
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Resume', resumeQty, '---'])

def csvCleaner():
    with open(csv_filename, 'w',  newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['EventType', 'EventNumber', 'Timestamp'])

# =================================================================================
# Initialization
start_time = time.perf_counter()
start_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
csv_filename = "Log.csv"

# =================================================================================
# Initialize CSV and UI
with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['EventType', 'EventNumber', 'Timestamp'])

print("="*70)
# beautiful artwork
print(r"""
  _____       _   _                    _______ _                     
 |  __ \     | | | |                  |__   __(_)                    
 | |__) |   _| |_| |__   ___  _ __       | |   _ _ __ ___   ___ _ __ 
 |  ___/ | | | __| '_ \ / _ \| '_ \      | |  | | '_ ` _ \ / _ \ '__|
 | |   | |_| | |_| | | | (_) | | | |     | |  | | | | | | |  __/ |   
 |_|    \__, |\__|_| |_|\___/|_| |_|     |_|  |_|_| |_| |_|\___|_|   
         __/ |                                                       
        |___/
""")

print("="*70)
time.sleep(1) 
print(f"Timer Started. Output: {csv_filename}")

# =================================================================================

try:
    listing_time = []
    stop_times = 0

    while True:
        time.sleep(0.0001) 
        NowTimeCode = time.perf_counter()
        print(f"\rElapsed: {timeConvert(NowTimeCode - start_time)} ", end="", flush=True)

# =================================================================================
        
        if keyboard.is_pressed('l'):
            lapWriter(NowTimeCode - start_time, csv_filename)
            print(f",laps:{len(listing_time)}", flush=True) 
            while keyboard.is_pressed('l'): pass

# =================================================================================

        if keyboard.is_pressed("p"):
            stop_times += 1
            pausestart = time.perf_counter()
            pauseWriter(pausestart, stop_times, csv_filename)
            
            # Pause Loop
            while not keyboard.is_pressed('r'):
                print(f"\rElapsed: {timeConvert(pausestart - start_time)} , Paused ", end="", flush=True)
                time.sleep(0.01)
            
            pauseend = time.perf_counter()
            resumeWriter(pauseend, stop_times, csv_filename)

# =================================================================================

            start_time += (pauseend - pausestart)
            print("\r" + " " * 50 + "\r", end="", flush=True)
            while keyboard.is_pressed('r'): pass

# =================================================================================
        if keyboard.is_pressed('c'):
            print("\r" + " " * 100 + "\r", end="", flush=True)
            while True:
                print(f"\rElapsed: {timeConvert(NowTimeCode - start_time)}, Clear Log.csv? (y/n): ", end="", flush=True)
                if keyboard.is_pressed('y'):
                    csvCleaner()
                    listing_time = []
                    print(f"\rElapsed: {timeConvert(NowTimeCode - start_time)}, Re-write finished. {' ' * 20}", end = '', flush=True)
                    while keyboard.is_pressed('y'): time.sleep(0.1)
                    break
                if keyboard.is_pressed('n'):
                    while keyboard.is_pressed('n'): time.sleep(0.1)
                    break 
            print("\r" + " " * 100 + "\r", end="", flush=True)
            
# =================================================================================             

except KeyboardInterrupt:
    print("")
    ending_time = time.perf_counter()
    duration = ending_time - start_time

    print(f"Timer Stopped, duration = {timeConvert(duration)}")

    with open(csv_filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['TotalDuration', '', duration])
        writer.writerow(['End', '', ''])

    print("Will exit in 5 seconds")
    time.sleep(5)

# =================================================================================

except PermissionError:
    print('Please close the program which is accessing the Log.csv.')