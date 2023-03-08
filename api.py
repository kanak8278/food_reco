import requests
import pandas as pd
from pprint import pprint

# df = pd.read_csv('task1.csv')
# col = "Ingredient Name"
# ingredient_names = df[col].tolist()

super_class = []
conceptnet_link = []
notes = []
conceptnet_base_url = "http://api.conceptnet.io/"

ingredient = "bacon"
obj = requests.get(conceptnet_base_url + 'c/en/' + ingredient).json()
edges = obj['edges']
idx = 0
while idx == 0 or 'nextPage' in obj['view']:
    obj = requests.get(conceptnet_base_url + obj['view']['nextPage']).json()
    edges.extend(obj['edges'])
    idx+=1
    if idx>=10:
        break
    
connections =  ['IsA']

for edge in edges:
    edge_rel = edge['rel']['label']
    edge_end = edge['end']['label']
    edge_sense = []

    if 'sense_label' in edge['end'].keys():
        edge_sense = edge['end']['sense_label'].strip().split(',')
        
    if edge_rel in connections and not edge_end == ingredient \
        and edge_end not in super_class and len(edge_sense)>1 and edge_sense[1].strip() == 'food':
        
        print(edge_rel)
        print(edge_end)
        if edge_sense is not None:
            print(edge_sense)
        print()
        super_class.append(edge_end)
    

    