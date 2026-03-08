from plyer import notification
from PIL import Image
from pathlib import Path

class Notification:
    def __init__(self):
        # icon_fp = Path(__file__).resolve().parent / 'icon.ico'
        # self.icon_image = Image.open(icon_fp)
        pass

    def send(self, message):
        """Send a notification to the user."""
        notification.notify(
            title="PTK",
            message=message,
            timeout=5,  # Duration in seconds
            # app_icon= self.icon_image
        )