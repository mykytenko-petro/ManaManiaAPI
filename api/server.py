import os

import uvicorn

from .fastapi_setup import app

uvicorn_server = uvicorn.Server(
    config=uvicorn.Config(
        app=app,
        host="0.0.0.0",
        port=int(os.environ["port"])
    )
)