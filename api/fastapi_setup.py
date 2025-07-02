import fastapi

from .routes import (
    test_router,
    google_auth_router,
    user_router
)

app = fastapi.FastAPI()

app.include_router(test_router)
app.include_router(google_auth_router)
app.include_router(user_router)