import csv
import os
import time
from datetime import datetime

from src.battery import get_battery_info
from src.notification import send_notification


# Configuration
LOW_BATTERY = 30
CHECK_INTERVAL = 60

LOG_FOLDER = "data"
LOG_FILE = os.path.join(LOG_FOLDER, "battery_log.csv")


# Prepare the log directory and CSV file.
os.makedirs(LOG_FOLDER, exist_ok=True)

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Battery", "Charger"])


previous_plugged = None
low_notified = False


while True:
    battery_info = get_battery_info()

    if battery_info is None:
        print("Battery information is not available.")
        break

    percent = battery_info["percent"]
    plugged = battery_info["power_plugged"]

    charger_status = "Connected" if plugged else "Disconnected"

    if percent <= LOW_BATTERY and not plugged:
        battery_status = "Low"
    elif percent <= 60:
        battery_status = "Normal"
    else:
        battery_status = "Good"

    print(
        f"Battery: {percent}% | "
        f"Charger: {charger_status} | "
        f"Status: {battery_status}"
    )

    # Notify when the charger state changes.
    if previous_plugged is not None:
        if plugged and not previous_plugged:
            send_notification("Charger Connected", f"Battery is {percent}%")
        elif not plugged and previous_plugged:
            send_notification("Charger Disconnected", f"Battery is {percent}%")

    previous_plugged = plugged

    # Notify once when the battery enters the low-battery state.
    if percent <= LOW_BATTERY and not plugged:
        if not low_notified:
            send_notification("Battery Low", f"Battery is {percent}%")
            low_notified = True
    else:
        low_notified = False

    # Persist the current reading.
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([current_time, percent, charger_status])

    time.sleep(CHECK_INTERVAL)
