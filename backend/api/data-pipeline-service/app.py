from collections import Counter
from fastapi import FastAPI
import csv
import requests
import os

app = FastAPI()

EXTERNAL_API_DOMAIN = "https://jsonplaceholder.typicode.com"

POSTS_ENDPOINT = "/posts"
USERS_ENDPOINT = "/users"
FILE_PATH = "data/raw"

# Helper functions
def get_header(token: str):
    return { "Authorization" : f"Bearer {token}" }

def write_csv(data, file_name: str):
    if not data:
        return None
    
    header = data[0].keys()
    file_path = f"{FILE_PATH}/{file_name}"

    os.makedirs(FILE_PATH, exist_ok=True)
    
    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)
    
    return file_path

def read_csv(file_path: str):
    rows = []

    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    return rows

def aggregate(posts):
    total_posts = len(posts)
    user_counts = Counter(post["userId"] for post in posts)
    top_user = max(user_counts.items(), key=lambda x: x[1])

    return {
        "total_posts": total_posts,
        "posts_per_user": dict(user_counts),
        "top_user": {
            "userId": top_user[0],
            "count": top_user[1]
        }
    }

def fetch_users():
    response = requests.get(
        EXTERNAL_API_DOMAIN + USERS_ENDPOINT,
        headers=get_header("dummy"),
        timeout=10
    )

    if response.status_code != 200:
        raise Exception(f"Fetching for users failed with statusCode: {response.status_code}")
    
    return response.json()

def fetch_posts():
    posts = []

    page = 1
    limit = 10

    while True:
        response = requests.get(
            EXTERNAL_API_DOMAIN + POSTS_ENDPOINT,
            params={"_page": page, "_limit": limit},
            headers=get_header("dummy"),
            timeout=10
        )

        if response.status_code != 200:
            raise Exception(f"Fetching posts failed with statusCode: {response.status_code}")
        
        posts_json = response.json()

        if not posts_json:
            break

        posts.extend(posts_json)
        page += 1

    return posts

@app.get("/ingest")
def ingest_endpoint():
    users = fetch_users()
    posts = fetch_posts()

    user_csv = write_csv(users, "user_data.csv")
    post_csv = write_csv(posts, "post_data.csv")

    return {
        "message": "csv files successfully written.",
        "userCount": len(users),
        "postCount": len(posts),
        "userDataPath": user_csv,
        "postDataPath": post_csv
    }

@app.get("/summary")
def summary_endpoint():
    posts = read_csv(f"{FILE_PATH}/post_data.csv")
    return aggregate(posts)