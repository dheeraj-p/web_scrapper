## Python Web Scraper

### Prerequisites

- Python 3.12 or higher
- Create a virtual environment using:

```sh
$ python3 -m venv .venv
```

- Activate the virtual environment
- Install dependencies:

```sh
$ pip install -r requirements.txt
```

### To Run

To run the app in development mode, use following command:

```sh
$ fastapi dev main.py
```

### Usage

The API for scrapping webpage is available on route `/scrape`. API is protected by a plain static authentication token:

```
Bearer some_random_token
```

Use following curl command for hitting the API:

```sh
curl --request GET \
  --url 'http://127.0.0.1:8000/scrape?page_count=2' \
  --header 'Authorization: Bearer Bearer some_random_token'
```
