from plyer import notification


class Console:
    def __init__(self, notifications: bool = True) -> None:
        self.notifications = notifications

    def print(self, content):
        print(content)
        if self.notifications:
            notification.notify(title="Pomody", message=content)
