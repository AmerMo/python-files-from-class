#%%

#  DICTIONARIES

beatles = {
  "John": "sings",
  "Paul": "plays bass",
  "Ringo": "plays drums",
  "George": "plays guitar"
}


#%%

beatles["John"] = "sings and plays guitar"

#%%

beatles.pop("Ringo")

#%%

for beatle in beatles.keys():
    print(beatle)
    

print(beatles.values())


#%%


for name in beatles:
    
    print(name + " " + beatles[name])


#%%
    
print(beatles)


beatles["John"] = "sings and plays"

print(beatles)


#%%


# SETS


#beatles = {"John", "Paul", "George", "Ringo"}


numbers = set([1,2,2,2,2,3,4])
#
#numbers.add(5)
#
#numbers.remove(5)
#
#numbers.remove(5)

#numbers.discard(5)

#numbers.discard(5)

another = {2, 3}

#%%

for number in numbers:
    print(number)

#%%
    
# EXERCISE SESSION 8
    
    
text = """
Echidnas sometimes known as spiny anteaters, belong to the family Tachyglossidae in the monotreme order of egg-laying mammals. The four extant species of Echidnas and the platypus are the only living mammals that lay eggs and the only surviving members of the order Monotremata.[2] The diet of some species consists of ants and termites, but they are not closely related to the true anteaters of the Americas, which are xenarthrans, along with sloths and armadillos. Echidnas live in Australia and New Guinea.

Echidnas evolved between 20 and 50 million years ago, descending from a platypus-like monotreme.[3] This ancestor was aquatic, but echidnas adapted to life on land.[3]
"""
    
def create_frequencies_dictionary(words):
    list_of_words = words.split()
    frequencies = {}
    
    for word in list_of_words:
        if word in frequencies:
            frequencies[word] = frequencies[word] + 1
        else:
            frequencies[word] = 1
            
    return frequencies

def print_frequencies(frequencies_dictionary):
    
    longest = 0
    
    for word in frequencies_dictionary:
        if len(word) > longest:
            longest = len(word)
    
    for word in frequencies_dictionary:
        
        number_of_spaces = longest - len(word)
        
        print(word + (" " * number_of_spaces) + " |" + ("*" * frequencies_dictionary[word]))
 
    
dictionary = create_frequencies_dictionary(text)   
print_frequencies(dictionary)
    
    
    
    
    
    
    
    
    
    




