from collections import defaultdict, deque
import time

class RateLimiter:
    def __init__(self, global_limit, user_limit, timelimit):
        self.global_queue = deque()
        self.user_queue = defaultdict(deque)
        self.global_limit = global_limit
        self.limit = user_limit
        self.timelimit = timelimit
        self.user_limit = {}

    def set_user_limit(self, user_id, limit) -> None:
        self.user_limit[user_id] = limit

    def allow_request(self, user_id) -> bool:
        user_queue = self.user_queue[user_id]
        user_limit = self.user_limit.get(user_id, self.limit)

        now = time.time()

        while self.global_queue and now - self.global_queue[0] >= self.timelimit:
            self.global_queue.popleft()

        while user_queue and now - user_queue[0] >= self.timelimit:
            user_queue.popleft()

        if len(self.global_queue) >= self.global_limit:
            return False
        
        if len(user_queue) >= user_limit:
            return False
        
        self.global_queue.append(now)
        user_queue.append(now)

        return True
    

if __name__ == "__main__":
    print("Rate limiter created with global limit 10, user limit 5")
    rate_limiter = RateLimiter(10, 5, 3)
    rate_limiter.set_user_limit("a", 3)
    rate_limiter.set_user_limit("b", 10)

    print("User A with limit 3")
    for i in range(5):
        print(rate_limiter.allow_request("a"))

    print("User B with limit 10")
    for i in range(10):
        print(rate_limiter.allow_request("b"))
