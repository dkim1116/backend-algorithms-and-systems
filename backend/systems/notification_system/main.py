from notification_queue import NotificationQueue
from services import UserPreferenceService, RateLimiter, NotificationService
from worker import Worker


def main() -> None:
    preference_service = UserPreferenceService()
    notification_queue = NotificationQueue()
    rate_limiter = RateLimiter(max_per_user=5)

    notification_service = NotificationService(
        preference_service=preference_service,
        notification_queue=notification_queue,
        rate_limiter=rate_limiter,
    )

    worker = Worker(notification_queue)

    notification_service.handle_event(1, "new_message")
    
    while not notification_queue.is_empty():
        worker.process_once()


if __name__ == "__main__":
    main()