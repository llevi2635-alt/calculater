def add (a,b):
    return a+b
def sub (a,b):
    return a-b
def mult (a,b):
    return a*b
def divide (a,b):
    try :
        return a/b
    except ZeroDivisionError as zd :
        return zd 
