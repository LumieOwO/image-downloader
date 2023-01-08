from check_urls import check_urls
from constants import URLS
from get_and_make_folder import Get_and_make_folder
from request_images import Request_images

class Main:
    def __init__(
            self,
            URLS
            ) -> None:
        self.URLS = URLS
        self.main()

    def main(self) -> None:
        self.check_websites()
        self.create_folders()
        self.request_images()

    def request_images(self) -> None:
        Request_images(
            URL=self.URLS
        )

    def create_folders(self) -> None:
        Get_and_make_folder(
        )

    def check_websites(self) -> None:
        check_urls(
            URLS=self.URLS
        )



if __name__ == "__main__":
    main = Main(
        URLS=URLS
    )