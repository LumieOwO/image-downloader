import os
from constants import URLS
class Get_and_make_folder:
    def __init__(
            self,
            ) -> None:
        self.folder_names = self.extract_folder_names()
        self.create_folder()
    
    def extract_folder_names(self) -> list:
        folder_names = []*self.get_urls_count()
        for folder_name in URLS:
            folder_names.append(folder_name.strip("URL"))

        return folder_names
    
    def create_folder(self) -> None:
        for name in self.folder_names:
            if not os.path.exists(name):
                os.mkdir(name)

    def get_urls_count(self) -> int:
        num = 0
        for url in URLS:
            num += 1
        return num
