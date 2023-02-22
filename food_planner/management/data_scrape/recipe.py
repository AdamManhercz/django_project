"""Collect food recipes"""

import requests
import os
from django.conf import settings
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

    return data, soup


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

def get_images(recipes:list, soup:list) -> list:

    recipes = [recipe.lower().replace(" ", "_") for recipe in recipes]
    
    img_src = []

    for i, recipe in enumerate(recipes):
        try:
            img_url = soup.select("img")[i]["data-src"]
            
        except KeyError:
            img_url = soup.select("img")[i]["src"]
        
        response = requests.get(img_url)
        file_path = f"C:/Users/norat/Desktop/project/media/{recipe}.jpg"
        img_src.append(file_path)

        if response.status_code:
            with open(file_path, "wb") as f:

                f.write(response.content)

    return img_src

def get_csv(recipes: list, urls: list, images:list):
    """Save the scraped data in csv"""

    df = pd.DataFrame({"recipes": recipes, "urls": urls, "images":images})

    df.to_csv("../project/recipes.csv")


if __name__ == "__main__":
    data,soup = get_data(URL)

    recipes = get_recipes(data)
    urls = get_urls(data)
    img_src = get_images(recipes, soup)

    get_csv(recipes, urls, img_src)
