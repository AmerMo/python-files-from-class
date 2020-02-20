#%%

import csv
import json

#%%

## reading csv files

with open("output.csv") as f:
    reader = csv.reader(f)
    
    for line in reader:
        print(line[1])
        
#%%
        
## writing files
        
        	
lines = [
  ["asdf", "qwer"],
  ["hello", "world"]
]


with open("written_csv.csv", "w") as f:
    writer = csv.writer(f)
    
    for line in lines: 
        writer.writerow(line)
        
#%%
    
## Writing dictionaries

beatles = [
    {"name": "John", "instrument": "voice"},
    {"name": "Paul", "instrument": "guitar"},
    {"name": "George", "instrument": "bass"},
    {"name": "Ringo", "instrument": "drums"}
]

with open("beatles.csv", "w") as my_file:
    writer = csv.DictWriter(my_file, ["name", "instrument"])
    writer.writeheader()
    for beatle in beatles:
        writer.writerow(beatle)
        
#%%
        
#%% reading files with column names
        
with open("beatles.csv") as my_file:
    reader = csv.DictReader(my_file)
    for beatle in reader:
        print(beatle["name"] + " -> " + beatle["instrument"])

#%%

with open("potato.json") as file:
    users = json.load(file)
    
    print(users[0]["user"])


















