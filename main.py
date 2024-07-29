from fastapi import FastAPI
from scrapper import ProductsScrapper
from storage import LocalStorage
from notifier import ConsoleNotifier


app = FastAPI()


@app.get("/")
def read_hello_world():
    storage = LocalStorage("products.json")
    notifier = ConsoleNotifier()
    url = "https://dentalstall.com/shop/page/"

    ProductsScrapper(url, 5, storage, notifier).scrap()
    return "Success"
