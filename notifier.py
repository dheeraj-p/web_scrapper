class Notification:
    def __init__(self, total_scrapped: int, total_updated: int):
        self.total_scrapped = total_scrapped
        self.total_updated = total_updated


class Notifier:
    def nofity(self, notification: Notification) -> bool:
        pass


class ConsoleNotifier(Notifier):
    def nofity(self, notification: Notification) -> bool:
        print("=====> Product Scrapped: {}".format(notification.total_scrapped))
        print("=====> Product Updated: {}".format(notification.total_updated))
        return True
