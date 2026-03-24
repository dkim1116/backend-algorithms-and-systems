from dataclasses import dataclass


@dataclass
class Notification:
    user_id: int
    channel: str
    message: str
    retry_count: int = 0