from fastapi import FastAPI
import urllib.request
import json
from fastapi.middleware.cors import CORSMiddleware
from functools import wraps

app = FastAPI(
    title="Werkix News API",
    description="Homework assignment for news fetching API",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Joel Kumwenda",
        "url": "https://github.com/jkumwenda/werkix-api",
        "email": "jkumwenda@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

apikey = "637e5e27d4fd6d46a4bb3716dfa0a225"


def cache_response(func):
    response = None

    @wraps(func)
    async def wrapper(*args, **kwargs):
        nonlocal response
        if not response:
            response = await func(*args, **kwargs)
        return response

    return wrapper


@app.get("/")
@cache_response
async def news(number_of_aticles: int = None, keyword: str = None, title_description_content: str = None):
    url = f"https://gnews.io/api/v4/search?q={keyword}&token={apikey}&max={number_of_aticles}&in={title_description_content}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]
    return articles
