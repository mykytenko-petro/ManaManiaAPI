import fastapi

from .routes import (
    test_router,
    google_auth_router,
    user_router
)

app = fastapi.FastAPI()

app.include_router(router=test_router)
app.include_router(router=google_auth_router)
app.include_router(router=user_router)