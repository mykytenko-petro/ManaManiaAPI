import os

import uvicorn

import settings
import api

def main():
    try:
        settings.assemble()

        uvicorn.run(
            app="api:app",
            host=os.environ["host"],
            port=2232
        )

    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()