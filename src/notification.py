from winotify import Notification


def send_notification(title, message):
    """Display a Windows desktop notification."""
    notification = Notification(
        app_id="Battery Monitor",
        title=title,
        msg=message,
    )
    notification.show()
