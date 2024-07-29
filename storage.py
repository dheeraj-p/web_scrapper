from product import Product, ProductEncoder
import json


class StorageEngine:
    def save_bulk(self, products: list[Product]):
        pass


class LocalStorage(StorageEngine):
    def __init__(self, file_path: str):
        super().__init__()
        self.file_path = file_path

    def save_bulk(self, products: list[Product]) -> bool:
        content = json.dumps(products, cls=ProductEncoder)
        file = open(self.file_path, "w")
        file.write(content)
        file.close()
