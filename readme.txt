CS 337 Project 2: Recipe Parser & Interactive Cookbook

Python version: 3.6
Dependencies:
    - requests
    - bs4
    - nltk
    - numpy

How to install dependencies:
	- install virtualenv 
		pip install virtualenv
	- create a new environment
		python3.6 -m venv virtualenv
	- activate your virtual environment
		source virtualenv/bin/activate
	- install dependencies
		pip install -r requirements.txt

How to use:
    - Run `recipe.py` with the appropriate arguments. See description of arguments below.

recipe.py arguments:
    --recipe [REQUIRED] [TYPE: STRING]
        URL to a recipe on AllRecipes.com. Must be surrounded by quotation marks.
    --transformation [OPTIONAL] [TYPE: STRING(S)] [DEFAULT: None]
        Type of transformation(s) to apply (healthy, vegetarian, korean, or/and lactose-free). 
        These transformations will be applied in the order of the arguments.
        *Note*: "lactose-free" must be surrounded by quotation marks.
    --servings [OPTIONAL] [TYPE: INT] [DEFAULT: Default recipe serving size on the AllRecipes.com recipe page]
        Number of servings.
    --parse [OPTIONAL] [TYPE: INT] [DEFAULT: 0]
        1 to print the parsing results, 0 to not show.

Output:
    - Recipe name
    - Number of servings
    - List of ingredients (after transformation(s) applied, if any)
    - List of directions (after transformation(s) applied, if any)
    - [if parse] List of tools, primary methods, other methods, and parsed ingredients.

Requirements completed:
    - Ingredients
        Ingredient name ✔️
        Quantity ✔️
        Measurement ✔️
    - Tools ✔️
    - Methods
        Primary cooking method ✔️
    - Steps ✔️
    - Transformations
        Vegetarian ✔️
        Healthy ✔️
        Style of cuisine (Korean) ✔️

Optional requirements completed:
    - Ingredients
        Descriptor ✔️
        Preparation ✔️
    - Methods
        Other cooking methods used ✔️
    - Transformations
        Additional style of cuisine (Italian) ✔️
        Double amount or cut it by half ✔️
        Lactose-free ✔️