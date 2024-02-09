from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse

app = FastAPI()


class Article(BaseModel):
    article_no: int
    currency: str
    description: str


class Provider(BaseModel):
    provider_no: int
    name: str


class Price(BaseModel):
    article_no: int
    provider_no: int
    price: int


articles_db = {}
providers_db = {}
prices_db = {}


@app.post("/articles/", response_model=Article)
def create_article(article: Article):
    articles_db[article.article_no] = article
    return article


@app.get("/articles/{article_no}", response_model=Article)
def read_article(article_no: int):
    article = articles_db.get(article_no)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@app.post("/providers/", response_model=Provider)
def create_provider(provider: Provider):
    providers_db[provider.provider_no] = provider
    return provider


@app.post("/prices/", response_model=Price)
def create_price(price: Price):
    if (
        price.article_no not in articles_db
        or price.provider_no not in providers_db
    ):
        raise HTTPException(
            status_code=404, detail="Article or Provider not found"
        )

    prices_db[(price.article_no, price.provider_no)] = price
    return price


@app.get("/prices/", response_model=List[Price])
def read_prices():
    return list(prices_db.values())


@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>We are up and running!</h1>"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
