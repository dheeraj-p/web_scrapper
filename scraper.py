from storage import StorageEngine, ImageDownloader
from product import Product
from notifier import Notifier, Notification
from bs4 import BeautifulSoup
from requests import api


class ProductsScraper:
    def __init__(
        self,
        http: api,
        url: str,
        total_pages: int,
        storage: StorageEngine,
        notifier: Notifier,
        image_downloader: ImageDownloader,
    ):
        self.http = http
        self.url = url
        self.total_pages = total_pages
        self.storage = storage
        self.notifier = notifier
        self.image_downloader = image_downloader

    def scrape(self):
        products = []
        for page in range(1, self.total_pages + 1):
            products += self._scrape_page(page)

        self.storage.save_bulk(products)
        self.notifier.nofity(Notification(len(products), len(products)))

    def _scrape_page(self, page_num: int):
        res = self.http.get("{}{}".format(self.url, page_num))
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
            image_path = self.image_downloader.download(image)
            product_id = thumbnail_elem.attrs["href"].split("/")[-2]

            products.append(Product(product_id, title, image_path, price))

        return products
