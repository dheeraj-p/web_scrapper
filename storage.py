from product import Product, ProductEncoder
from requests import api
import json
import os


class StorageEngine:
    def save_bulk(self, products: list[Product]) -> bool:
        pass


class ImageDownloader:
    def __init__(self, http_client: api, directory: str):
        self.http = http_client
        self.dir = directory

    def _create_directory(self):
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

    def download(self, image_url: str) -> str:
        res = self.http.get(image_url)

        file_name = image_url.split("/")[-1]
        file_path = "{}/{}".format(self.dir, file_name)

        self._create_directory()
        file = open(file_path, "wb")
        file.write(res.content)
        return file_path


class LocalStorage(StorageEngine):
    def __init__(self, file_path: str):
        super().__init__()
        self.file_path = file_path

    def save_bulk(self, products: list[Product]) -> bool:
        content = json.dumps(products, cls=ProductEncoder)
        file = open(self.file_path, "w")
        file.write(content)
        file.close()
        return True
