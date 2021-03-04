import json

with open('lists.json') as f:
  data = json.load(f)
with open('veg_transforms.json') as f:
  data2 = json.load(f)

PRIMARY_METHODS = data['PRIMARY_METHODS']
OTHER_METHODS = data['OTHER_METHODS']
TOOLS = data['TOOLS']
VEG_SUBS = data2
# MEAT = data['MEAT']
# FISH = data['FISH']