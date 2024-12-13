from fastapi import FastAPI
import httpx

app = FastAPI()

# Базовий URL JSONPlaceholder API
BASE_URL = "https://jsonplaceholder.typicode.com"

# 1. GET-запит: Отримання списку постів
@app.get("/posts")
async def get_posts():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/posts")
    return response.json()

# 2. POST-запит: Додавання нового посту
@app.post("/posts")
async def create_post(post: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/posts", json=post)
    return response.json()

# 3. PUT-запит: Оновлення посту
@app.put("/posts/{post_id}")
async def update_post(post_id: int, post: dict):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL}/posts/{post_id}", json=post)
    return response.json()

# 4. PATCH-запит: Часткове оновлення посту
@app.patch("/posts/{post_id}")
async def patch_post(post_id: int, post: dict):
    async with httpx.AsyncClient() as client:
        response = await client.patch(f"{BASE_URL}/posts/{post_id}", json=post)
    return response.json()

# 5. DELETE-запит: Видалення посту
@app.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/posts/{post_id}")
    return {"status": response.status_code, "detail": "Post deleted" if response.status_code == 200 else "Failed"}

# 6. Опціональний: Перевірка сервера
@app.get("/")
def root():
    return {"message": "FastAPI JSONPlaceholder API Project"}
