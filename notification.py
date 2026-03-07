from plyer import notification

class Notification:
    def __init__(self):
        pass

    def send(self, message):
        """Send a notification to the user."""
        notification.notify(
            title="PTK",
            message=message,
            timeout=5  # Duration in seconds
        )