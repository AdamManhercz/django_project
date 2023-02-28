import requests
from typing import Tuple, List
from dataclasses import dataclass

API_ID="ecd36886"
API_KEY="b1a0598e2630ee2483c15a0e5aca9f44"

query = "lunch"
_from = "from=1"
to = "to=61"
meal_type = "mealType=lunch"
          
URL = f"https://api.edamam.com/search?q={query}&{meal_type}&{_from}&{to}&app_id={API_ID}&app_key={API_KEY}"

@dataclass
class EdamamApi:

    url:str = URL

    def get_recipe_api(self) -> Tuple[List[str], List[str],List[str]]:

        data = requests.get(self.url).json()

        recipes = []
        urls = []
        images = []

        # Couldn't do with list comprehension - "list indices must be integers or slices, not str"
        for i in range(0,60):
            
            hits = data["hits"]
            recipe = hits[i]['recipe']

            title = recipe['label']
            recipes.append(title)
           
            url = recipe["url"]
            urls.append(url)

            image = recipe["image"]
            images.append(image)

        return recipes , urls, images

