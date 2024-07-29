from fastapi import FastAPI
from scrapper import ProductsScrapper
from storage import LocalStorage


app = FastAPI()


@app.get("/")
def read_hello_world():
    storage = LocalStorage("products.json")
    url = "https://dentalstall.com/shop/page/"
    p = ProductsScrapper(url, 5, storage)
    p.scrap()
    return "Success"
