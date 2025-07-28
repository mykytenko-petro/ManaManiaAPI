import os

import dotenv

def assemble():
    DOTENV_PATH = os.path.abspath(os.path.join(__file__, "..", ".env"))

    if os.path.exists(path= DOTENV_PATH):
        print("succesfully loaded .env")
        
        dotenv.load_dotenv(dotenv_path= DOTENV_PATH)