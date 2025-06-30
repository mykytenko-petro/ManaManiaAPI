import requests

def main():
    response = requests.post(
        url="http://127.0.0.1:2232/mongodb_test?id=2232"
    ).json()

    print(response)

if __name__ == "__main__":
    main()