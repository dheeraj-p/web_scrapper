from json import JSONEncoder
from typing import Any


class Product:
    def __init__(self, id: str, title: str, image_path: str, price: float):
        self.id = id
        self.title = title
        self.image_path = image_path
        self.price = price


class ProductEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        return o.__dict__
