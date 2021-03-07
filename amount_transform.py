from pprint import pprint
import re
from parse_recipe import parse_ingredients, num, get_recipe, reconstruct_ingredient
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

ignore = ['minute','second','hour','minutes','seconds','hours','degree','degrees']

def amount_transform(recipe, servings):
    ratio = servings / recipe['servings'] 
    new_ingredients = [amount_transform_ingredient(p, ratio) for p in recipe['parsed_ingredients']]
    recipe['directions'] = [amount_transform_direction(d, ratio) for d in recipe['directions']]
    recipe['parsed_ingredients'] = new_ingredients
    recipe['ingredients'] = [reconstruct_ingredient(x) for x in new_ingredients]
    recipe['servings'] = servings
    return recipe


def amount_transform_ingredient(ingredient, ratio):
    ingredient['amount'] *= ratio
    return ingredient


def amount_transform_direction(direction, ratio):
    tokens = nltk.pos_tag(nltk.word_tokenize(direction))
    s = ' '.join([f'{num(x[0])*ratio}' if num(x[0]) and tokens[i+1][0] not in ignore \
                                        else x[0] for i,x in enumerate(tokens)])
    return re.sub(r'\s+([.,:;-])', r'\1', s)

# recipe = get_recipe('https://www.allrecipes.com/recipe/273864/greek-chicken-skewers/')
# print(amount_transform(recipe, 1))
