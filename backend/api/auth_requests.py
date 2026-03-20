import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class API:
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def get_top_k_users_by_posts(self, k: int) -> list[dict]:
        response = requests.get(
            f"{BASE_URL}/users",
            headers=self.headers,
            timeout=10
        )

        if response.status_code != 200:
            raise Exception(f"Request failed to get users: {response.status_code}")
        
        users = response.json()
        user_map = {}

        if not users:
            return []

        for user in users:
            user_map[user["id"]] = user["name"]

        post_map = {}
        result = []

        page = 1
        limit = 10

        while True:
            response = requests.get(
                f"{BASE_URL}/posts",
                headers=self.headers,
                params={"_page": page, "_limit": limit}
            )

            if response.status_code != 200:
                raise Exception(f"Request failed to get posts: {response.status_code}")
            
            posts = response.json()

            if not posts:
                break

            for post in posts:
                post_map[post["userId"]] = post_map.get(post["userId"], 0) + 1

            page += 1
        
        for user_id, user_name in user_map.items():
            result.append({
                "userId": user_id,
                "name": user_name,
                "postCount": post_map.get(user_id, 0)
            })

        result.sort(key=lambda x: x["postCount"], reverse=True)

        return result[:k]


if __name__ == "__main__":
    api = API("dummy")
    result = api.get_top_k_users_by_posts(5)
    print(result)
        