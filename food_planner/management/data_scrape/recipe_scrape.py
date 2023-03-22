from typing import Tuple, List
from dataclasses import dataclass
from bs4 import BeautifulSoup as bs
import requests

URL = "https://www.simplyrecipes.com/recipes-5090746"


@dataclass
class Scraper:
    """Collects recipe data from the given url"""

    url:str = URL

    def get_recipe_info(self) -> Tuple[List[str], List[str],List[str]]:
        """Collects the titles, the urls and the image sources of the recipes"""

        header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
            }
        r = requests.get(self.url, headers=header)
        soup = bs(r.content, "html.parser")
        section = soup.find("section")
        div = section.find("div", class_="loc fixedContent")

        data = div.find("div", class_="comp l-container mntl-taxonomysc-article-list-group mntl-block")

        # titles
        recipes = data.find_all("span", class_="card__title-text")
        recipes = [r.get_text() for r in recipes]
        
        #urls
        urls = [u['href'] for u in data.find_all('a', href=True)]
        urls = [u for u in urls if u != "#"]

        #image sources
        image_urls = [img["src"] for img in data.find_all("img",src=True)]

        return recipes, urls, image_urls
    


