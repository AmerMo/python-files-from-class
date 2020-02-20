#%%

## OPENING FILES

file  = open("/Users/giulia/text_file.txt")

for line in file:
    print(line)
    
file.close()

#%%

## USING WITH

with open("/Users/giulia/text_file.txt") as file:
    
    for line in file:
        print(line)
        

#%%
        
text = "text to put inside our file"

with open("text_file.txt", "w") as file:
    file.write(text)
    
#%%
    
filename = "dummy_data.csv"
    
def from_csv(file_path):
    parsed_csv = []
    
    with open(file_path) as file:
        for line in file:
            line_cells = line.split(",")
            parsed_csv.append(line_cells)
            
    return parsed_csv
    
def to_csv(list_of_lists):
    
    with open("output.csv", "w") as file:
        for line in list_of_lists:
            line_as_string = ",".join(line) + "\n"
            file.write(line_as_string)
 
    
to_csv([["hello", "hola"], ["goodbye", "adios"]])  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    