from plyer import notification

class Notification:
    def __init__(self):
        pass

    def send_notification(self, message):
        """Send a notification to the user."""
        notification.notify(
            title="PTK",
            message=message,
            timeout=15  # Duration in seconds
        )