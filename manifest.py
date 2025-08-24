import os

import dotenv


def assemble() -> None:
    DOTENV_PATH: str = os.path.abspath(path=os.path.join(__file__, "..", ".env"))

    if os.path.exists(path= DOTENV_PATH):
        print("succesfully loaded .env")
        
        dotenv.load_dotenv(dotenv_path= DOTENV_PATH)