import os

import uvicorn

from .fastapi_setup import app

uvicorn_server = uvicorn.Server(
    config=uvicorn.Config(
        app=app,
        host="0.0.0.0" if os.environ["IS_DEPLOY"] == "TRUE" else "127.0.0.1",
        port=int(os.environ["PORT"])
    )
)