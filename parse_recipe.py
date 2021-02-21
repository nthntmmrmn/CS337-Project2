import requests
from bs4 import BeautifulSoup
from unicodedata import numeric
import re
import nltk
import string

def num(n):
    '''
    Input: string
    Output: float if string is unicode fraction or number, 0 otherwise
    '''
    try: return numeric(n)
    except: 
        try: return float(n)
        except: return 0

def parse_ingredient(ing):
    '''
    Input: ingredient string
    Output: [amount, measurement, type of ingredient, rest]
    '''
    measurements = ['teaspoon','tablespoon','cup','quart','ounce','gallon','pint','pound','dash','pinch']
    regex = re.compile('('+'(?=s| |$)|'.join(measurements)+')(?!(?s:.*)(!?('+'(?=s|es|ies| |$)|'.join(measurements)+')))\s(.*)')
    r = re.search(regex, ing)
    words = ing.split() if r else ing[0:re.search('[^0-9\u00BC-\u00BE\u2150-\u215E\s]+', ing).end()].split()
    return [sum([num(x) for x in words]), [r.group(1), get_type_of_ingredient(r.group(4))] \
         if r else ['', get_type_of_ingredient(re.search('[0-9\u00BC-\u00BE\u2150-\u215E\s]+(.*)', ing).group(1))]]

def get_ingredients(soup):
    '''
    Input: BeautifulSoup-parsed document
    Output: List of [amount, [measurement, [type of ingredient, rest]]]
    '''
    ingredients = [i.text.strip() for i in soup.find_all("span", class_="ingredients-item-name")]
    flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))
    return [list(flatten(parse_ingredient(x))) for x in ingredients]

def get_type_of_ingredient(text):
    '''
    Input: ingredient string minus amount and measurement
    Output: [type of ingredient, rest of string]
    '''
    pos = ['NN','JJ','VBN','NNS',',','VBG','NNS','VBD']
    tokens = nltk.pos_tag(nltk.word_tokenize(text))
    stop = next((i for i,v in enumerate(tokens) if v[1] not in pos), len(tokens))
    type_ing = ' '.join([v[0] for v in tokens[:stop]])
    rest = ' '.join([v[0] for v in tokens[stop:]])
    return [re.sub(r'\s+([,:;-])', r'\1', type_ing).strip(string.punctuation),
            re.sub(r'\s+([,:;-])', r'\1', rest)]

def get_directions(soup):
    '''
    Input: BeautifulSoup-parsed document
    Output: List of directions as strings
    '''
    return [i.text.strip() for i in soup.find_all("div", class_="paragraph")]

def get_html(url):
    '''
    Input: string url to an AllRecipes.com recipe page
    Output: BeautifulSoup-parsed document
    '''
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')

def get_recipe(url):
    '''
    Input: string url to an AllRecipes.com recipe page
    Output: dict containing ingredients and directions
    '''
    r = get_html(url)
    return {'ingredients': get_ingredients(r), 'directions': get_directions(r)}

## Example:
# recipe = get_recipe('https://www.allrecipes.com/recipe/273864/greek-chicken-skewers/')
# print(recipe['ingredients'])
# print(recipe['directions'])