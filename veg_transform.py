from big_lists import VEG_SUBS
from pprint import pprint
import re
from parse_recipe import desc_plus_ingredient, measurements, parse_ingredients, get_recipe, reconstruct_ingredient

def veg_transform(recipe):
    x = [veg_transform_ingredient(p) for p in recipe['parsed_ingredients']]
    new_ingredients = [i[0] for i in x]
    repl_pairs = [(i[1],i[2]) for i in x if i[1]!=i[2]]
    new_directions = [veg_transform_direction(d, repl_pairs) for d in recipe['directions']]
    recipe['parsed_ingredients'] = new_ingredients
    recipe['ingredients'] = [reconstruct_ingredient(x) for x in new_ingredients]
    recipe['directions'] = new_directions
    return recipe


def veg_transform_ingredient(ingredient):
    m = ingredient['measurement']
    t = ingredient['type']
    d = ingredient['desc']
    dt = desc_plus_ingredient(ingredient)
    for key in list(VEG_SUBS["Substitutions"].keys()):
        r = re.findall('|'.join(VEG_SUBS["Substitutions"][key]["Replacers"]), dt)
        if r:
            ingredient['type'] = key
            ingredient['desc'] = VEG_SUBS["Substitutions"][key]["Desc"]
            ingredient['amount'] *= VEG_SUBS["Substitutions"][key]["Ratio"]
            if not m or m in measurements:
                ingredient['measurement'] = VEG_SUBS["Substitutions"][key]["Amount"]
            break
    return ingredient, t, ingredient['type']


def veg_transform_direction(direction, replacements):
    for pair in replacements:
        direction = re.sub(pair[0], pair[1], direction)
    return direction