import requests
from bs4 import BeautifulSoup
from unicodedata import numeric
import re
import nltk
import string
import json
import regex
from parse_recipe import get_recipe, parse_ingredients

recipe = get_recipe('https://www.allrecipes.com/recipe/273864/greek-chicken-skewers/')
#print(recipe['ingredients'])

#print(parse_ingredients(recipe['ingredients']))
#Output: List
#of[amount, [measurement, [type of ingredient, rest]]]

def korean_substitutions():
    '''
    Input: no input
    Output: dictionary of substitutions
    '''
    korean_seasonings = {
        'seasonings': [
            'soy sauce',
            'Korean red pepper flaked',
            'sesame oil',
            'ginger'
        ]
    }
    korean_ingredients = {
        'green onions': [
            'parsley',
            'oregano',
            'cilantro',
            'thyme',
            'rosemary'
        ],
        'perilla leaves': [
            'mint',
            'basil',
            'parsley',
            'oregano',
            'cilantro',
            'thyme',
            'rosemary'
        ],
        'yuja (Korean citrus)': [
            'orange',
            'lemon',
            'lime'
        ],
        'napa cabbage': [
            'cabbage'
        ],
        'sesame seeds': [
            'seeds'
        ],
        'Korean red pepper flakes': [
            'red pepper flakes',
            'paprika',
            'cayenne pepper',
            'dried peppers',
            'chile powder',
            'cumin'
        ],
        'vinegar': [
            'rice wine vinegar'
        ],
        'teriyaki sauce': [
            'bulgogi sauce'
        ],
        'sesame oil': [
            'oil',
        ],
        'dried dates': [
            'dried cranberries',
        ],
        'plum extract': [
            'honey',
            'syrup',
            'maple syrup,'
        ],
        'corn syrup': [
            'rice syrup'
        ],
        'pine nuts': [
            'nut',
            'almonds'
        ],
        'bread crumbs': [
            'panko bread crumbs',
        ],
        'soy bean paste': [
            'miso paste',
        ],
        'gochujang (Korean red pepper paste)': [
            'paste',
            'chili paste'
        ],
        'mirin rice wine': [
            'wine'
        ],
        'salt': [
            'soy sauce'
        ],
        'rice cakes': [
            'gnocchi',
            'rigatoni',
            'pasta shells',
            'macaroni',
            'penne',
            'ziti'
        ],
        'buckwheat noodles': [
            'noodles',
            'spaghetti',
            'linguine',
            'fettuccine'
        ],
        'short-grain rice': [
            'rice',
            'orzo'
        ]
    }
    return korean_ingredients
#https://www.allrecipes.com/recipe/246866/rigatoni-alla-genovese/
#https://www.allrecipes.com/recipe/220869/easy-pressure-cooker-pot-roast/



def korean_replace(ingredients):
    '''
    Input: list of ingredients
    Output: dict containing ingredients and directions
    '''
    pass

#korean_replace(parse_ingredients(recipe['ingredients']))