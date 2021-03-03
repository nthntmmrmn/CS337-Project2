import parse_recipe
from pprint import pprint
from nick_transform import healthy_transform

if __name__ == "__main__":
    # ## Example:
    # Get base recipe (uncomment one)
    # recipe = parse_recipe.get_recipe(
    #    'https://www.allrecipes.com/recipe/173505/big-bs-collard-greens/')
    # recipe = parse_recipe.get_recipe(
    #    'https://www.allrecipes.com/recipe/273864/greek-chicken-skewers/')
    # recipe = parse_recipe.get_recipe(
    #    'https://www.allrecipes.com/recipe/278180/greek-yogurt-blueberry-lemon-pancakes/')
    # recipe = parse_recipe.get_recipe(
    #    'https://www.allrecipes.com/recipe/280509/stuffed-french-onion-chicken-meatballs')

    r = 'https://www.allrecipes.com/recipe/280509/stuffed-french-onion-chicken-meatballs'
    recipe = parse_recipe.get_recipe(r)

    # Print name, ingredients, recipe
    # pprint(recipe['name'])
    # pprint(recipe['ingredients'])
    # pprint(recipe['directions'])

    # Parse tools and methods
    tools = parse_recipe.get_tools(recipe['directions'])
    # pprint(tools)
    methods = parse_recipe.get_methods(recipe['directions'])
    # pprint(methods)

    # Parse ingredients
    pi = parse_recipe.parse_ingredients(recipe['ingredients'])
    transformed_ingredients = []
    for i in pi:
        transformed_ingredients.append(healthy_transform(i))

    for i in transformed_ingredients:
        print(i)
