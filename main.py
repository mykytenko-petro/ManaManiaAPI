import settings
import api

def main():
    try:
        settings.assemble()
        api.uvicorn_server.run()

    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()