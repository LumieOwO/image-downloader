import requests
import random
import time
import constants
class Request_images:
    def __init__(
            self,
            URL
            ) -> None:
        self.URLS = URL
        self.websites = self.get_all_website_urls()
        self.request_from_url()

    def request_from_url(self) -> None:
        while 1:
            time.sleep(constants.SLEEP_TIME)
            url = random.choice(self.websites)
            folder_name = url.replace(constants.BASEAPIURL,"")
            image_url = requests.request(
                method="GET",
                url=url,
            ).json()["image"]
            filename = image_url.split("/")[-1]
            print(image_url)
            image = requests.request(
                method="GET",
                url=image_url,
            )
            with open(f"{folder_name}//{filename}","wb") as f:
                    f.write(image.content)

    def get_urls_count(self) -> int:
        num = 0
        for url in self.URLS:
            num += 1
        return num
    
    def get_all_website_urls(self) -> list:
        urls = []*self.get_urls_count()
        for i in self.URLS:
            urls.append(self.URLS[i])
        return urls



