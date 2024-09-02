"""
fertisch
"""
import json


def adjust_recipe(recipes, person_count):
    factor = person_count / recipes['servings']
    adjusted_ingredients = {ingredient: amount * factor for ingredient, amount in recipes['ingredients'].items()}
    recipes['ingredients'] = adjusted_ingredients
    recipes['servings'] = person_count
    return recipes


def load_recipe(recipes):
    return json.loads(recipes)


if __name__ == '__main__':
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')
    recipe = load_recipe(recipe_json)
    adjusted_recipe = adjust_recipe(recipe, 2)
