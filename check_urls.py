import requests
def check_urls(
    URLS
) -> None:
    try:
        for URL_KEY in URLS:
            temp = requests.get(
                url=URLS[URL_KEY],
            )
            if temp.status_code == 200:
                pass
            else:
                print(f"{URLS[URL_KEY]} down")
    except Exception as E:
        print("internet down")
        exit()