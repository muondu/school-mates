# app.py

import json
a = input("Enter the 1 name:  ")
b = input("Enter the 2 name:  ")
c = input("Enter the 3 name:  ")
d = input("Enter the 4 name:  ")
e = input("Enter the 5 name:  ")

appDict = {
  'name1': a,
  'name2': b,
  'name3': c,
  'name4': d
}
with open('app.json', 'w') as fp:
    json.dump(appDict, fp)
with open('app.json') as f:
    data = json.load(f)

print(data)








