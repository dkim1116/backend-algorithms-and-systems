from collections import deque
from models import Notification

class NotificationQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, notification: Notification) -> None:
        self.queue.append(notification)

    def dequeue(self) -> Notification | None:
        if not self.queue:
            return None
        return self.queue.popleft()
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0