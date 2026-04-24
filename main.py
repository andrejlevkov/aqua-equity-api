from fastapi import FastAPI
from routes import user_router, post_router

app = FastAPI(title="Blog API")

app.include_router(user_router.router)
app.include_router(post_router.router)