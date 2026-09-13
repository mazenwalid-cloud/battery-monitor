import psutil


def get_battery_info():
    """Return current battery information, or None if unavailable."""
    battery = psutil.sensors_battery()

    if battery is None:
        return None

    return {
        "percent": battery.percent,
        "power_plugged": battery.power_plugged,
        "time_left": battery.secsleft,
    }
