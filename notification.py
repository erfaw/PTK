from plyer import notification
from winotify import Notification


class Notification:
    def __init__(self):
        # icon_fp = Path(__file__).resolve().parent / 'icons' / 'icon.ico'
        # self.icon_image = Image.open(icon_fp)
        pass

    def send_plyer(self, message):
        """Send a notification to the user."""
        # # TODO : use another thing to notify in windows. and search for cause of problem with pyinstaller (didnt work with plyer.notification)
        notification.notify(
            title="PTK",
            message=message,
            timeout=5,  # Duration in seconds
            # app_icon= self.icon_image
        )