"""Collect food recipes"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = "https://www.simplyrecipes.com/recipes-5090746"


def get_data(url: str):
    """Collects the recipes"""

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    r = requests.get(url, headers=header)
    soup = bs(r.content, "html.parser")
    section = soup.find("section")

    data = section.find("div", class_="loc fixedContent")

    return data


def get_recipes(data: str) -> list:
    """Scrapes the foods"""

    recipes = data.findAll("span", class_="card__title-text")
    recipes = [r.get_text() for r in recipes]

    return recipes


def get_urls(data: str) -> list:
    """Scrapes the urls"""

    urls = [d["href"] for d in data.find_all("a", href=True)]
    urls = [u for u in urls if u != "#"]

    return urls


def get_csv(recipes: list, urls: list):
    """Save the scraped data in csv"""

    df = pd.DataFrame({"recipes": recipes, "urls": urls})

    df.to_csv("../project/recipe.csv")


if __name__ == "__main__":
    data = get_data(URL)

    recipes = get_recipes(data)
    urls = get_urls(data)

    get_csv(recipes, urls)
