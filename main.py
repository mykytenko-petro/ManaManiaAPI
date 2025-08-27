import traceback
import sys


def main() -> None:
    try:
        from manifest import assemble
        assemble()

        import api

        api.uvicorn_server.run()

    except KeyboardInterrupt:
        pass

    except:
       traceback.print_exception(sys.exception()) 

if __name__ == "__main__":
    main()