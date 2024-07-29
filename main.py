from fastapi import FastAPI
from scrapper import ProductsScrapper
from storage import LocalStorage, ImageDownloader
from notifier import ConsoleNotifier
from requests import api


app = FastAPI()


@app.get("/scrap")
def scrap_pages(page_count: int = 1):
    # Hard coded for now, can be taken from environment variables
    storage = LocalStorage("products.json")
    notifier = ConsoleNotifier()
    image_downloader = ImageDownloader(api, "images")

    url = "https://dentalstall.com/shop/page/"
    ProductsScrapper(api, url, page_count, storage, notifier, image_downloader).scrap()
    return {"status": "Success"}
