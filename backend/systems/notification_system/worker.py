from models import Notification
from notification_queue import NotificationQueue


class Worker:
    def __init__(self, notification_queue: NotificationQueue):
        self.notification_queue = notification_queue

    def process_once(self) -> None:
        notification = self.notification_queue.dequeue()
        if not notification:
            return
        
        success = self.send(notification)

        if not success:
            if notification.retry_count < 3:
                notification.retry_count += 1
                self.notification_queue.enqueue(notification)
            else:
                print(f"Giving up on retries after three attempts for user: {notification.user_id}")


    def send(self, notification: Notification) -> bool:
        if notification.channel == "sms" and notification.retry_count == 0:
            print(f"FAILED sending {notification.channel} to user {notification.user_id}")
            return False

        print(
            f"SENT {notification.channel} to user {notification.user_id}: "
            f"{notification.message}"
        )
        return True