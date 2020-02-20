#%%

def divide(a, b):
    return a / b


try:
    divide("", "asdf")
except:
    print("something went wrong")
    
#%%
    
#divide(4, 0)
#divide("asdf", "potato")
    
try:
    divide(4, 0)
except (ZeroDivisionError, ValueError):
    print("don't use 0 as a divisor")
except TypeError:
    print("put numeric types on dividend and divisor")
    
#%%
    
prefixes = {"34"}
    
def validate(phone_number):
    
    if type(phone_number) != str:
        raise TypeError("expected phone as a string")
    
    if len(phone_number) > 25:
        raise ValueError("phone too long")
    
    
#validate("892734987234987234987239847")
validate(928374982734)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    