from big_lists import LACTOSE_FREE_SUBS
from pprint import pprint
import re
from parse_recipe import desc_plus_ingredient, measurements, parse_ingredients, get_recipe, reconstruct_ingredient

def lactose_free_transform(recipe):
    x = [lactose_free_transform_ingredient(p) for p in recipe['parsed_ingredients']]
    new_ingredients = [i[0] for i in x]
    repl_pairs = [(i[1],i[2]) for i in x if i[1]!=i[2]]
    new_directions = [lactose_free_transform_direction(d, repl_pairs) for d in recipe['directions']]
    recipe['parsed_ingredients'] = new_ingredients
    recipe['ingredients'] = [reconstruct_ingredient(x) for x in new_ingredients]
    recipe['directions'] = new_directions
    return recipe


def lactose_free_transform_ingredient(ingredient):
    m = ingredient['measurement']
    t = ingredient['type']
    d = ingredient['desc']
    dt = desc_plus_ingredient(ingredient)
    for key in list(LACTOSE_FREE_SUBS["Substitutions"].keys()):
        r = re.findall('|'.join(LACTOSE_FREE_SUBS["Substitutions"][key]["Replacers"]), dt)
        if r:
            ingredient['type'] = key
            ingredient['desc'] = LACTOSE_FREE_SUBS["Substitutions"][key]["Desc"]
            ingredient['amount'] *= LACTOSE_FREE_SUBS["Substitutions"][key]["Ratio"]
            if not m or m in measurements:
                ingredient['measurement'] = LACTOSE_FREE_SUBS["Substitutions"][key]["Amount"]
            break
    return ingredient, t, ingredient['type']


def lactose_free_transform_direction(direction, replacements):
    for pair in replacements:
        direction = re.sub(pair[0], pair[1], direction)
    return direction
