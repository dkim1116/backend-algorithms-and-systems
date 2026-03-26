from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from collections import defaultdict, deque
import time

app = FastAPI()

class User:
    def __init__(self, userId: int, userCapacity: int):
        self.userId = userId
        self.userCapacity = userCapacity

class CreateUserRequest(BaseModel):
    userId: int
    userCapacity: int

class AllowRequestResponse(BaseModel):
    userId: int
    allowed: bool
    tokensLeft: float


class UserBucketResponse(BaseModel):
    userId: int
    tokenPerMin: int
    tokensLeft: float
    lastFilled: float

class RateLimiter:
    def __init__(self, globalCapacity: int, timeLimit: int):
        self.globalCapacity = globalCapacity
        self.timeLimit = timeLimit
        self.globalQueue = deque()
        self.userTokenBucket = {}

    def set_user_capacity(self, user: User) -> None:
        self.userTokenBucket[user.userId] = {
            "tokenPerMin": user.userCapacity,
            "tokensLeft": user.userCapacity,
            "lastFilled": time.time()
        }
    
    def allow_request(self, userId: int) -> bool:
        if userId not in self.userTokenBucket:
            return False
    
        self.clean_globalQueue()
        self.fill_tokens(userId)

        if len(self.globalQueue) >= self.globalCapacity:
            return False

        if self.userTokenBucket[userId]["tokensLeft"] < 1:
            return False

        self.userTokenBucket[userId]["tokensLeft"] -= 1
        self.globalQueue.append({"userId": userId, "time": time.time()})
        return True

    def fill_tokens(self, userId: int):
        bucket = self.userTokenBucket[userId]

        currentTime = time.time()
        elapsedSeconds = currentTime - bucket["lastFilled"]
        
        tokensPerSec = bucket["tokenPerMin"] / 60
        tokensToFill = tokensPerSec * elapsedSeconds

        bucket["tokensLeft"] = min(
            tokensToFill + bucket["tokensLeft"],
            bucket["tokenPerMin"]
        )
        bucket["lastFilled"] = currentTime

    def clean_globalQueue(self):
        while self.globalQueue and time.time() - self.globalQueue[0]["time"] >= self.timeLimit:
            self.globalQueue.popleft()

    def get_user_bucket(self, userId: int):
        if userId not in self.userTokenBucket:
            return None
        return self.userTokenBucket[userId]

    def user_exists(self, userId: int) -> bool:
        return userId in self.userTokenBucket

rate_limiter = RateLimiter(globalCapacity=100, timeLimit=60)

@app.get("/")
def health_check():
    return { "message": "Rate Limiter API with token bucket is running." }

@app.post("/newUser")
def add_user(request: CreateUserRequest):
    userId = request.userId
    userCapacity = request.userCapacity

    if rate_limiter.user_exists(userId):
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(userId=userId, userCapacity=userCapacity)
    rate_limiter.set_user_capacity(user)

    return {
        "message": "User created successfully",
        "user": {
            "userId": userId,
            "userCapacity": userCapacity
        }
    }

@app.post("/allowRequest/{userId}", response_model=AllowRequestResponse)
def allow_request(userId: int):
    if not rate_limiter.user_exists(userId):
        raise HTTPException(status_code=404, detail="User not found")

    allowed = rate_limiter.allow_request(userId)
    bucket = rate_limiter.get_user_bucket(userId)

    return AllowRequestResponse(
        userId=userId,
        allowed=allowed,
        tokensLeft=bucket["tokensLeft"]
    )


@app.get("/userBucket/{userId}", response_model=UserBucketResponse)
def get_user_bucket(userId: int):
    bucket = rate_limiter.get_user_bucket(userId)
    if bucket is None:
        raise HTTPException(status_code=404, detail="User not found")

    return UserBucketResponse(
        userId=userId,
        tokenPerMin=bucket["tokenPerMin"],
        tokensLeft=bucket["tokensLeft"],
        lastFilled=bucket["lastFilled"]
    )
