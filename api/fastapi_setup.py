import fastapi

from .routes import router

app = fastapi.FastAPI()

app.include_router(router)