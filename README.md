# Battery Monitor

A lightweight Windows battery monitoring tool built with Python. It continuously tracks battery level and charger state, sends desktop notifications for important events, and records battery status history in CSV format.

## ✨ Features

- 🔋 Monitor battery percentage continuously
- 🔌 Detect charger connection and disconnection
- ⚠️ Detect low-battery conditions
- 🔔 Send native Windows desktop notifications
- 📊 Log battery percentage and charger state to CSV
- ⏱️ Run continuously with a configurable polling interval

## 🛠️ Tech Stack

- **Python 3.12+**
- **psutil** — battery and system information
- **winotify** — Windows desktop notifications
- **CSV** — lightweight local logging

## 📁 Project Structure

```text
battery-monitor/
├── src/
│   ├── __init__.py
│   ├── battery.py          # Reads battery information
│   ├── notification.py     # Sends Windows notifications
│   └── main.py             # Monitoring loop and logging
├── data/                   # Generated battery logs
├── .gitignore
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

### 1. Clone the repository

```powershell
git clone https://github.com/mazenwalid-cloud/battery-monitor.git
cd battery-monitor
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, activate the environment from Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run the monitor

```powershell
python -m src.main
```

The application will start monitoring the battery and create `data/battery_log.csv` automatically. The generated log file is intentionally ignored by Git.

## ⚙️ Configuration

The main settings are defined in `src/main.py`:

```python
LOW_BATTERY = 30
CHECK_INTERVAL = 60
```

- `LOW_BATTERY` — battery percentage that triggers the low-battery alert.
- `CHECK_INTERVAL` — number of seconds between battery checks.

## 🔔 Notifications

The application sends a Windows notification when:

- The charger is connected.
- The charger is disconnected.
- The battery reaches the configured low-battery threshold while unplugged.

## 📊 Logging

Each monitoring cycle records:

| Field | Description |
|---|---|
| `Time` | Timestamp of the reading |
| `Battery` | Battery percentage |
| `Charger` | Connected or Disconnected |

Example:

```text
Time,Battery,Charger
2026-09-13 18:00:00,78,Connected
2026-09-13 18:01:00,78,Connected
```

## 💻 Platform

This project is designed for **Windows**, because desktop notifications are implemented with `winotify`.

## 📌 Notes

- A device without a detectable battery may return no battery information.
- The monitor runs continuously until it is stopped with `Ctrl+C`.
- Generated logs and Python cache/virtual-environment files are excluded from version control.

## 📄 License

No license has been added yet. If you plan to distribute or reuse this project publicly, consider adding an appropriate open-source license.

---

**Author:** Mazen Walid  
**Focus:** AI / Machine Learning · Python · Practical Engineering