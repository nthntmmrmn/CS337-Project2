import argparse
from pprint import pprint
from parse_recipe import get_recipe, get_tools, get_methods, parse_ingredients
from veg_transform import veg_transform
from amount_transform import amount_transform
from healthy_transform import healthy_transform
from lactose_free_transform import lactose_free_transform
from cuisine_transform import cuisine_transform_korean, cuisine_transform_italian

# Example command
# python recipe.py --recipe "https://www.allrecipes.com/recipe/273864/greek-chicken-skewers/" --transformation vegetarian healthy --servings 2 --parse 1

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--recipe", type=str, help="AllRecipes URL")
ap.add_argument("-t", "--transformation", nargs='+', type=str, help="Optional: Type of transformation(s) to apply (healthy, vegetarian, korean, or/and lactose-free). Default: None. These transformations will be applied in the order of the arguments.")
ap.add_argument("-s", "--servings", type=int, help="Optional: Number of servings. Default: default recipe serving size")
ap.add_argument("-p", "--parse", type=int, default=0, help="Optional: 1 to show the parsing results, 0 to not show. Default: 0")
args = vars(ap.parse_args())

# TODO: add other transformation functions:
transformations = {'vegetarian': veg_transform, 'healthy': healthy_transform, 'lactose-free': lactose_free_transform, 'korean': cuisine_transform_korean, 'italian': cuisine_transform_italian}

if args['servings'] and args['servings'] <= 0:
    print('Serving size must be greater than zero.')
elif not args['recipe']:
    print('Please provide a recipe URL as the --recipe argument.')
elif args['transformation'] and any(t not in list(transformations.keys()) for t in args["transformation"]):
    print(f'Invalid transformation in {args["transformation"]}. Run `python recipe.py --help` for more info.')
elif args['recipe'] and args['transformation']:
    recipe = get_recipe(args['recipe'])
    print(f'Recipe name: {recipe["name"]}')
    print(f'Servings requested: {args["servings"] if args["servings"] else recipe["servings"]}\n')
    for t in args["transformation"]:
        print(f'***Applying {t} transformation***')
        recipe = transformations[t](recipe)
    recipe = amount_transform(recipe, args["servings"] if args["servings"] else recipe["servings"])
    print('***Printing recipe information***')
    print('\nINGREDIENTS:')
    for i in recipe['ingredients']:
        print(f'\t- {i}')
    print('\nDIRECTIONS:')
    for i,d in enumerate(recipe['directions']):
        print(f'\t{i+1}. {d}')
    if args['parse']:
        print('\n***Printing recipe parse***')
        tools = get_tools(recipe['directions'])
        print(f'\nTOOLS: {tools}')
        methods = get_methods(recipe['directions'])
        print(f'\nPRIMARY METHODS: {methods["primary"]}')
        print(f'\nOTHER METHODS: {methods["secondary"]}')
        print('\nPARSED INGREDIENTS:')
        for p in recipe['parsed_ingredients']:
            for key in list(p.keys()):
                print(f'\t{key}: {p[key]}')
            print('\n')
elif args['recipe'] and not args['transformation']:
    recipe = get_recipe(args['recipe'])
    print(f'Recipe name: {recipe["name"]}')
    print('\nNo transformation applied.\n***Printing recipe information***')
    print('\nINGREDIENTS:')
    for i in recipe['ingredients']:
        print(f'\t- {i}')
    print('\nDIRECTIONS:')
    for i,d in enumerate(recipe['directions']):
        print(f'\t{i+1}. {d}')
    if args['parse']:
        print('\n***Printing recipe parse***')
        tools = get_tools(recipe['directions'])
        print(f'\nTOOLS: {tools}')
        methods = get_methods(recipe['directions'])
        print(f'\nPRIMARY METHODS: {methods["primary"]}')
        print(f'\nOTHER METHODS: {methods["secondary"]}')
        pi = parse_ingredients(recipe['ingredients'])
        print('\nPARSED INGREDIENTS:')
        for p in recipe['parsed_ingredients']:
            for key in list(p.keys()):
                print(f'\t{key}: {p[key]}')
            print('\n')

