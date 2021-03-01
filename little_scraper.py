import string
import requests
from bs4 import BeautifulSoup
import nltk
import re
import numpy as np

# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'}
# r = requests.get('https://naturalhealthtechniques.com/list-of-meats-and-poultry/', headers=headers)
# r = requests.get('https://en.wikipedia.org/wiki/List_of_types_of_seafood')
# soup = BeautifulSoup(r.text, 'html.parser')
# # print(soup)
# a = soup.find_all('li')
# b = [c.text.lower() for c in a]
# print('\', \''.join(b))

meat = ['bear', 'beef', 'beef heart', 'beef liver', 'beef tongue', 'bone soup', 'buffalo', 'bison', 'calf liver', 'calf', 'caribou', 'goat', 'ham', 'horse', 'kangaroo', 'lamb', 'marrow soup', 'moose', 'mutton', 'opossum', 'organ meats', 'pork', 'pork, bacon', 'rabbit', 'snake', 'squirrel', 'sweetbreads', 'tripe', 'turtle', 'veal', 'venison', 'chicken', 'chicken liver', 'cornish game hen', 'duck', 'duck liver', 'emu', 'gizzards', 'goose', 'goose liver', 'grouse', 'guinea hen', 'liver', 'organs', 'ostrich', 'partridge', 'pheasant', 'quail', 'squab', 'turkey']
FISH = ['anchovies', 'barracuda', 'basa', 'bass','striped bass', 'black cod','sablefish', 'blowfish', 'bluefish', 'bombay duck', 'bream', 'brill', 'butter fish', 'catfish', 'cod','pacific cod','atlantic cod', 'dogfish', 'dorade', 'eel', 'flounder', 'grouper', 'haddock', 'hake', 'halibut', 'herring', 'ilish', 'john dory', 'lamprey', 'lingcod', 'mackerel', 'mahi mahi', 'monkfish', 'mullet', 'orange roughy', 'parrotfish', 'patagonian toothfish','chilean sea bass', 'perch', 'pike', 'pilchard', 'pollock', 'pomfret', 'pompano', 'sablefish', 'salmon', 'sanddab','pacific sanddab', 'sardine', 'sea bass', 'shad','alewife','american shad', 'shark', 'skate', 'smelt', 'snakehead', 'snapper','rockfish','rock cod', 'pacific snapper', 'sole', 'sprat', 'sturgeon', 'surimi', 'swordfish', 'tilapia', 'tilefish', 'trout','rainbow trout', 'tuna', 'turbot', 'wahoo', 'whitefish', 'whiting', 'witch','righteye flounder', 'purified water', 'caviar','sturgeon roe', 'ikura','salmon roe', 'kazunoko','herring roe', 'lumpfish roe', 'masago','capelin roe', 'shad roe', 'tobiko','flying-fish roe', 'crabs', 'craw fish','cray fish', 'lobsters', 'shrimps','prawns', 'cockle', 'cuttlefish', 'clam', 'loco', 'mussel', 'octopus', 'oyster', 'periwinkle', 'scallop', 'squid', 'conch','snails', 'nautilus', 'sea cucumber', 'uni','sea urchin roe', 'anchovy', 'barramundi', 'billfish', 'carp', 'catfish', 'cod', 'eel', 'flatfish', 'flounder', 'herring', 'mackerel', 'salmon', 'sardine', 'shark', 'sturgeon', 'swordfish', 'tilapia', 'trout', 'tuna', 'whitebait', 'abalone', 'cockles', 'conch', 'crab meat', 'crayfish', 'geoduck', 'krill', 'lobster', 'mussels', 'oysters', 'scallops', 'shrimp', 'sea urchins', 'crustaceans', 'molluscs', 'seaweed', 'jellyfish', 'octopus', 'sea cucumber', 'squid', 'whale', 'sea vegetables', 'algae']

FISH1 = ['fish','tuna','salmon','trout','pollock','sea bream','sea bass','cod','haddock','john dory','turbot','plaice','basa','mackerel','sardine','red mullet','tilapia','gurnard','ling','swordfish','']
FISH = ['anchovies', 'barracuda', 'basa', 'bass','striped bass', 'black cod','sablefish', 'blowfish', 'bluefish', 'bombay duck', 'bream', 'brill', 'butter fish', 'catfish', 'cod','pacific cod','atlantic cod', 'dogfish', 'dorade', 'eel', 'flounder', 'grouper', 'haddock', 'hake', 'halibut', 'herring', 'ilish', 'john dory', 'lamprey', 'lingcod', 'mackerel', 'mahi mahi', 'monkfish', 'mullet', 'orange roughy', 'parrotfish', 'patagonian toothfish','chilean sea bass', 'perch', 'pike', 'pilchard', 'pollock', 'pomfret', 'pompano', 'sablefish', 'salmon', 'sanddab','pacific sanddab', 'sardine', 'sea bass', 'shad','alewife','american shad', 'shark', 'skate', 'smelt', 'snakehead', 'snapper','rockfish','rock cod', 'pacific snapper', 'sole', 'sprat', 'sturgeon', 'surimi', 'swordfish', 'tilapia', 'tilefish', 'trout','rainbow trout', 'tuna', 'turbot', 'wahoo', 'whitefish', 'whiting', 'witch','righteye flounder', 'purified water', 'caviar','sturgeon roe', 'ikura','salmon roe', 'kazunoko','herring roe', 'lumpfish roe', 'masago','capelin roe', 'shad roe', 'tobiko','flying-fish roe', 'crabs', 'craw fish','cray fish', 'lobsters', 'shrimps','prawns', 'cockle', 'cuttlefish', 'clam', 'loco', 'mussel', 'octopus', 'oyster', 'periwinkle', 'scallop', 'squid', 'conch','snails', 'nautilus', 'sea cucumber', 'uni','sea urchin roe', 'anchovy', 'barramundi', 'billfish', 'carp', 'catfish', 'cod', 'eel', 'flatfish', 'flounder', 'herring', 'mackerel', 'salmon', 'sardine', 'shark', 'sturgeon', 'swordfish', 'tilapia', 'trout', 'tuna', 'whitebait', 'abalone', 'cockles', 'conch', 'crab meat', 'crayfish', 'geoduck', 'krill', 'lobster', 'mussels', 'oysters', 'scallops', 'shrimp', 'sea urchins', 'crustaceans', 'molluscs', 'seaweed', 'jellyfish', 'octopus', 'sea cucumber', 'squid', 'whale', 'sea vegetables', 'algae']
fish2 = FISH1 + FISH
print('\', \''.join(np.unique(fish2)))
FISH = ['abalone', 'alewife', 'algae', 'american shad', 'anchovies', 'anchovy', 'atlantic cod', 'barracuda', 'barramundi', 'basa', 'bass', 'billfish', 'black cod', 'blowfish', 'bluefish', 'bombay duck', 'bream', 'brill', 'butter fish', 'capelin roe', 'carp', 'catfish', 'caviar', 'chilean sea bass', 'clam', 'cockle', 'cockles', 'cod', 'conch', 'crab meat', 'crabs', 'craw fish', 'cray fish', 'crayfish', 'crustaceans', 'cuttlefish', 'dogfish', 'dorade', 'eel', 'fish', 'flatfish', 'flounder', 'flying-fish roe', 'geoduck', 'grouper', 'gurnard', 'haddock', 'hake', 'halibut', 'herring', 'herring roe', 'ikura', 'ilish', 'jellyfish', 'john dory', 'kazunoko', 'krill', 'lamprey', 'ling', 'lingcod', 'lobster', 'lobsters', 'loco', 'lumpfish roe', 'mackerel', 'mahi mahi', 'masago', 'molluscs', 'monkfish', 'mullet', 'mussel', 'mussels', 'nautilus', 'octopus', 'orange roughy', 'oyster', 'oysters', 'pacific cod', 'pacific sanddab', 'pacific snapper', 'parrotfish', 'patagonian toothfish', 'perch', 'periwinkle', 'pike', 'pilchard', 'plaice', 'pollock', 'pomfret', 'pompano', 'prawns', 'purified water', 'rainbow trout', 'red mullet', 'righteye flounder', 'rock cod', 'rockfish', 'sablefish', 'salmon', 'salmon roe', 'sanddab', 'sardine', 'scallop', 'scallops', 'sea bass', 'sea bream', 'sea cucumber', 'sea urchin roe', 'sea urchins', 'sea vegetables', 'seaweed', 'shad', 'shad roe', 'shark', 'shrimp', 'shrimps', 'skate', 'smelt', 'snails', 'snakehead', 'snapper', 'sole', 'sprat', 'squid', 'striped bass', 'sturgeon', 'sturgeon roe', 'surimi', 'swordfish', 'tilapia', 'tilefish', 'tobiko', 'trout', 'tuna', 'turbot', 'uni', 'wahoo', 'whale', 'whitebait', 'whitefish', 'whiting', 'witch']
subs = ['tofu','tempeh','soyrizo','seitan','jackfruit','gardein chick\'n','beyond meat','impossible meat','falafel']
alts = ['soy milk','almond milk']