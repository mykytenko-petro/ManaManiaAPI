def main():
    try:
        from manifest import assemble
        assemble()

        import api

        api.uvicorn_server.run()

    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()