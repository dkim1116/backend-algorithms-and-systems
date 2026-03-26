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

class UserTokenBucket(BaseModel):
    userId: int
    userCapacity: int
    tokenPerMin: int
    tokensLeft: int
    lastFilled: int

class AllowRequestReponse(BaseModel):
    userId: int
    allowRequest: bool
    tokensLeft: float

class RateLimiter:
    def __init__(self, globalCapacity: int, timeLimit: int):
        self.globalCapacity = globalCapacity
        self.timeLimit = timeLimit
        self.globalQueue = deque()
        self.userQueue = defaultdict(deque)
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
        else:
            self.userTokenBucket[userId]["tokensLeft"] -= 1
            self.userQueue[userId].append({ "userId": userId, "time": time.time() })
            self.globalQueue.append({ "userId": userId, "time": time.time() })
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
    
    def get_bucket(self, userId: int) -> UserTokenBucket:
        if userId not in self.userTokenBucket:
            return None
        
        return self.userTokenBucket[userId]
    
    def user_exists(self, userId: int) -> bool:
        return userId in self.userTokenBucket
        

rateLimiter = RateLimiter(100, 10)

@app.get("/")
def health_check():
    return { "message": "Rate Limiter API with token bucket is running." }

@app.post("/newUser")
def add_user(request: CreateUserRequest):
    userId = request.userId
    userCapacity = request.userCapacity

    if rateLimiter.user_exists(userId):
        return HTTPException(404, detail="User already exists")
    
    user = User(userId=userId, userCapacity=userCapacity)
    rateLimiter.set_user_capacity(user=user)

    return {
        "message": "user created successfully"
    }

