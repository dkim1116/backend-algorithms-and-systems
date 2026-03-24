from models import Notification
from notification_queue import NotificationQueue


class UserPreferenceService:
    def __init__(self):
        self.preferences = {
            1: ["email", "sms"],
            2: ["push"],
            3: ["email", "push"],
        }

    def get_channels(self, user_id: int) -> list[str]:
        return self.preferences.get(user_id, [])


class RateLimiter:
    def __init__(self, max_per_user: int):
        self.max_per_user = max_per_user
        self.user_map = {}

    def allow(self, user_id: int) -> bool:
        self.user_map[user_id] = self.user_map.get(user_id, self.max_per_user)
        if self.user_map[user_id] > 0:
            self.user_map[user_id] -= 1
            return True
        return False


class NotificationService:
    def __init__(
        self,
        preference_service: UserPreferenceService,
        notification_queue: NotificationQueue,
        rate_limiter: RateLimiter,
    ):
        self.preference_service = preference_service
        self.notification_queue = notification_queue
        self.rate_limiter = rate_limiter

    def handle_event(self, user_id: int, event_type: str) -> None:
        channels = self.preference_service.get_channels(user_id)

        if not channels:
            return

        if not self.rate_limiter.allow(user_id):
            return

        message = self.build_message(event_type)

        for channel in channels:
            notification = Notification(
                user_id=user_id,
                channel=channel,
                message=message,
            )
            self.notification_queue.enqueue(notification)

    def build_message(self, event_type: str) -> str:
        message_map = {
            "order_shipped": "Your order has shipped.",
            "new_message": "You received a new message.",
            "password_reset": "Your password reset was requested.",
        }

        return message_map.get(event_type, "You have a new notification.")