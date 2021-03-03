import json
import Levenshtein

with open('healthy_transforms.json') as f:
    transforms = json.load(f)


def healthy_transform(ingredient):
    a = ingredient['amount']
    m = ingredient['measurement']
    t = ingredient['type']
    d = ingredient['desc']
    p = ingredient['prep']

    # Altering Descriptors for ingredients
    descriptions = transforms['Descriptions']
    for item in descriptions:
        for i in descriptions[item]:
            if 'ingredient' in list(i.keys()) and 'description' in list(i.keys()) and (t.lower() in i['ingredient'] or i['ingredient'] in t.lower())and (d.lower() in i['description'] or i['description'] in d.lower()):
                if i['append'] == 'false':
                    d = item
                else:
                    d = item + ' ' + d
            elif 'ingredient' in list(i.keys()) and (t.lower() in i['ingredient'] or i['ingredient'] in t.lower()) and 'description' not in list(i.keys()):
                if i['append'] == 'false':
                    d = item
                else:
                    d = item + ' ' + d
            elif d != '' and 'description' in list(i.keys()) and (d.lower() in i['description'] or i['description'] in d.lower()) and 'ingredient' not in list(i.keys()):
                if i['append'] == 'false':
                    d = item
                else:
                    d = item + ' ' + d

    # Substituting ingredients for other ingredients
    substitutions = transforms['Substitutions']
    for item in substitutions:
        if t.lower() in substitutions[item]['Replacers']:
            t = item
            try:
                d = substitutions[item]['Desc']
            except:
                pass
            a = a*substitutions[item]['Ratio']

    return{'amount': a, 'measurement': m, 'type': t, 'desc': d, 'prep': p}
