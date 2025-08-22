import time

import requests
import webbrowser


def main():
    device_id = 2232
    API_URL = "http://127.0.0.1:2232"

    oauth_url = requests.get(url=f"{API_URL}/google_login?device_id={device_id}").json()["url"]
    webbrowser.open(url=oauth_url, new=1)

    token_response = {}

    while not ("id_token" in token_response):
        token_response = requests.get(url=f"{API_URL}/get_google_session?device_id={device_id}").json()

        print("please wait")

        time.sleep(2)

    token_response = token_response["id_token"]

    result = requests.post(
        url=f"{API_URL}/user_auth",
        json={
            "email": token_response["email"],
            "sub": token_response["sub"]
        },
    ).json()

    print(result)

if __name__ == "__main__":
    main()