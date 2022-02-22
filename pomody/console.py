from plyer import notification
from rich.console import Console

console = Console()


class Console:
    def __init__(self, notifications: bool = True) -> None:
        self.notifications = notifications

    def print(self, content):
        console.print(content)
        if self.notifications:
            notification.notify(title="Pomody", message=content)
