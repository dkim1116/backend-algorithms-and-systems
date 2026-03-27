from fastapi import FastAPI
from collections import Counter
import requests
import csv
import os

EXTERNAL_API_DOMAIN = "https://jsonplaceholder.typicode.com"

COMMENT_RESOURCE_NAME = "comments"
USER_RESOURCE_NAME = "users"

app = FastAPI()

# Helper functions
def fetch_resource(resource_name: str):
    params = {}

    if resource_name == COMMENT_RESOURCE_NAME:
        params["_page"] = 1
        params["_limit"] = 10

    result = []

    while True:
        response = requests.get(
            url=f"{EXTERNAL_API_DOMAIN}/{resource_name}",
            timeout=10,
            params=params
        )

        if response.status_code != 200:
            raise Exception(f"Fetch request failed for getting {resource_name} with statusCode: {response.status_code}")
        
        response_data = response.json()

        if not response_data:
            break

        result.extend(response_data)

        if resource_name == COMMENT_RESOURCE_NAME:
            params["_page"] += 1
        else:
            break

    return result

def write_csv(file_name: str, data):
    if not data:
        return None
    
    dir_path = "data/csv/"
    headers = data[0].keys()

    os.makedirs(dir_path, exist_ok=True)

    file_path = f"{dir_path}/{file_name}"

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()
        writer.writerows(data)
    return file_path

def read_csv(file_name: str):
    if not file_name:
        raise Exception("File name has not been provided for reading CSV file.")
    
    file_path = f"data/csv/{file_name}"

    result = []

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            result.append(row)
    return result

        

@app.get("/ingestion")
def ingestion_endpoint():
    user_data = fetch_resource(USER_RESOURCE_NAME)
    comments_data = fetch_resource(COMMENT_RESOURCE_NAME)

    user_file_path = write_csv("user_data.csv", user_data)
    comment_file_path = write_csv("comment_data.csv", comments_data)

    return {
        "message": "Ingestion for user data and comment data has been completed.",
        "userCount": len(user_data),
        "commentCount": len(comments_data),
        "user_csv_file_path": user_file_path,
        "comment_csv_file_path": comment_file_path
    }

@app.get("/summary")
def summary_endpoint():
    comments = read_csv("comment_data.csv")

    total_comments = len(comments)
    total_posts = Counter(comment["postId"] for comment in comments)
    
    top_posts = [
        { "postId": postId, "count" : count } 
        for postId, count in total_posts.most_common(5)
    ]

    domain_count = Counter(comment["email"].split("@")[1] 
                           for comment in comments)

    top_domains = [
        { "domain": domain, "count": count } 
        for domain, count in domain_count.most_common(5)
    ]

    return {
        "top_posts": top_posts,
        "domain_count": domain_count,
        "top_domains": top_domains
    }

@app.get("/topUserComments")
def top_user_comments():
    comments = read_csv("comment_data.csv")
    users = read_csv("user_data.csv")

    user_id_with_name = [{"userId": user["id"], "name": user["name"]} for user in users]
    filtered_comments = []

    # for comment in comments:
    #     if comment["id"] 
