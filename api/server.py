import os

import uvicorn

from .fastapi_setup import app

uvicorn_server = uvicorn.Server(
    config=uvicorn.Config(
        app=app,
        host=os.environ["host"],
        port=int(os.environ["port"])
    )
)