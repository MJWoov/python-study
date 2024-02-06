def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def add_many(*args):
    result=0
    for i in args:
        result+=i
    return result

print(add_many(1,32,42,412))