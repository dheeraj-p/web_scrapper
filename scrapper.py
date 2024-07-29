from storage import StorageEngine
from product import Product
from notifier import Notifier, Notification
from bs4 import BeautifulSoup
import requests


class ProductsScrapper:
    def __init__(
        self,
        url: str,
        total_pages: int,
        storage: StorageEngine,
        notifier: Notifier,
    ):
        self.url = url
        self.total_pages = total_pages
        self.storage = storage
        self.notifier = notifier

    def scrap(self):
        products = []
        for page in range(1, self.total_pages + 1):
            products += self._scrap_page(page)

        self.storage.save_bulk(products)
        self.notifier.nofity(Notification(len(products), len(products)))

    def _scrap_page(self, page_num: int):
        res = requests.get("{}{}".format(self.url, page_num))
        soup = BeautifulSoup(res.text, "html.parser")

        product_elems = soup.select("#mf-shop-content ul.products > li")

        products = []
        for product_elem in product_elems:
            price_elem = product_elem.select_one(".mf-product-price-box > .price bdi")
            thumbnail_elem = product_elem.select_one(".mf-product-thumbnail > a")
            price = float(price_elem.text[1:])
            image_elem = thumbnail_elem.find("img")
            title = image_elem.attrs["alt"]
            image = image_elem.attrs["data-lazy-src"]
            product_id = thumbnail_elem.attrs["href"].split("/")[-2]

            products.append(Product(product_id, title, image, price))

        return products
