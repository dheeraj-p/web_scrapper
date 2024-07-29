from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from scraper import ProductsScraper
from storage import LocalStorage, ImageDownloader
from notifier import ConsoleNotifier
from requests import api


app = FastAPI()
security = HTTPBearer()
static_token = "Bearer some_random_token"


def get_user(creds: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
    if creds.credentials == static_token:
        return "valid_username"

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
    )


@app.get("/scrape")
def scrape_pages(username: Annotated[str, Depends(get_user)], page_count: int = 1):
    # Hard coded for now, can be taken from environment variables
    storage = LocalStorage("products.json")
    notifier = ConsoleNotifier()
    image_downloader = ImageDownloader(api, "images")

    url = "https://dentalstall.com/shop/page/"
    ProductsScraper(api, url, page_count, storage, notifier, image_downloader).scrape()
    return {"status": "Success"}
