import requests
from bs4 import BeautifulSoup
from unicodedata import numeric
import re
import nltk
import string
import json
import regex
#from parse_recipe import get_recipe, parse_ingredients, reconstruct_ingredient
from parse_recipe import desc_plus_ingredient, measurements, parse_ingredients, get_recipe, reconstruct_ingredient

with open('cuisine_transform.json') as f:
    korean_transforms = json.load(f)

# transforms ingredients to Korean ingredients
def cuisine_transform_parsed_ingredients_helper1(ingredient):
    """
    Input: list of original ingredients
    Output: dict containing new transformed ingredients (with amount, measurements, type, etc.)
    """

    a = ingredient['amount']
    m = ingredient['measurement']
    t = ingredient['type']
    d = ingredient['desc']
    p = ingredient['prep']

    # Substituting ingredients for other ingredients
    substitutions = korean_transforms['substitutes']
    for item in substitutions:
        if t.lower() in substitutions[item]['Replacers']:
            t = item
            try:
                d = substitutions[item]['Desc']
            except:
                pass
            a = a*substitutions[item]['Ratio']

    return{'amount': a, 'measurement': m, 'type': t, 'desc': d, 'prep': p}


def cuisine_transform_parsed_ingredients_helper2(parsed_ingredients):
    """
    Input: list of parsed ingredients
    Output: list of tuples of (ingredient to be replaced, new ingredient)
    """
    new_pi = []
    for each in parsed_ingredients:
        if swap_parsed_ingredient_list_helper(each) is not None:
            new_pi.append(cuisine_transform_parsed_ingredients_helper1(each))
    return new_pi


def cuisine_transform_parsed_ingredients(recipe):
    '''
    Input: list of original ingredients
    Output: list new ingredients
    '''
    pi = parse_ingredients(recipe['ingredients'])
    return cuisine_transform_parsed_ingredients_helper2(pi)


def swap_parsed_ingredient_list_helper(new_ingredient):
    """
    Input: Dictionary of an ingredient
    Output: Returns tuple of (ingredient to be replaced, new ingredient)
    """
    a = new_ingredient['amount']
    m = new_ingredient['measurement']
    t = new_ingredient['type']
    d = new_ingredient['desc']
    p = new_ingredient['prep']

    substitutions = korean_transforms['substitutes']

    for item in substitutions:
        if t.lower() in substitutions[item]['Replacers']:
            # old ingredient
            to_be_replaced = d + " " + t
            # new ingredient
            t = item
            replaced = substitutions[t]['Replacers']
            for idx in range(len(replaced)):
                if t == replaced[idx]:
                    r = replaced[idx]
            try:
                d = substitutions[item]['Desc']
                t = d + " " + t
            except:
                pass
            a = a*substitutions[item]['Ratio']

            return (to_be_replaced, t)


def swap_ingredient_list(recipe):
    """
    Input: dictionary of recipe
    Output: list of tuples: (ingredient to be replaced, new ingredient)
    """
    parsed_ingredients = parse_ingredients(recipe['ingredients'])
    changedIngredients = []
    for each in parsed_ingredients:
        if swap_parsed_ingredient_list_helper(each) is not None:
            changedIngredients.append(swap_parsed_ingredient_list_helper(each))
    return changedIngredients


def cuisine_transform_ingredient_helper(ingredient, replacements):
    for pair in replacements:
        ingredient = re.sub(pair[0], " " + pair[1], ingredient)
    return ingredient


def cuisine_transform_direction_helper(direction, replacements):
    for pair in replacements:
        direction = re.sub(pair[0], " " + pair[1], direction)
    return direction


def cuisine_transform_ing_and_dir(recipe):
    """
    Input: list of original ingredients
    Output: list new ingredients
    """
    new_ing = []
    ingredients = recipe['ingredients']
    for each in ingredients:
        new_ing.append(cuisine_transform_ingredient_helper(each, swap_ingredient_list(recipe)))

    new_dir = []
    directions = recipe['directions']
    for line in directions:
        new_dir.append(cuisine_transform_direction_helper(line, swap_ingredient_list(recipe)))

    return new_ing, new_dir


def swap_ingredient_list1(recipe):
    """
    Input: list of parsed ingredients
    Output: list of tuples of (ingredient to be replaced, new ingredient)
    """
    parsed_ingredients = parse_ingredients(recipe['ingredients'])
    changedIngredients = []
    for each in parsed_ingredients:
        if swap_parsed_ingredient_list_helper(each) is not None:
            changedIngredients.append(swap_parsed_ingredient_list_helper(each))
    return changedIngredients


def cuisine_transform_recipe(recipe):
    """
    Input: Dictionary (original) recipe
    Output: Dictionary (transformed) recipe
    """
    ing_dir = cuisine_transform_ing_and_dir(recipe)
    recipe['ingredients'] = ing_dir[0]
    recipe['parsed_ingredients'] = cuisine_transform_parsed_ingredients(recipe)
    recipe['directions'] = ing_dir[1]
    return recipe




# to call for recipe after cuisine transformation, call function: cuisine_transform_recipe(recipe)

#og_recipe = get_recipe('https://www.allrecipes.com/recipe/273864/greek-chicken-skewers/')
#print("RESULT : ", cuisine_transform_recipe(og_recipe))
