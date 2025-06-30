import time

import requests
import webbrowser

def main():
    device_id = 2232

    oauth_url = requests.get(url=f"http://127.0.0.1:2232/google_login?device_id={device_id}").json()["url"]
    webbrowser.open(url=oauth_url, new=1)

    while True:
        response = requests.get(url=f"http://127.0.0.1:2232/get_google_id_token?device_id={device_id}").json()

        if "id_token" in response:
            print(response["id_token"])
            break
        else:
            print("please wait")

        time.sleep(2)

if __name__ == "__main__":
    main()