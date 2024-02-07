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

def kwargs(**kwargs):
    return

def myself(name,age=0): #매개변수 초기값설정
    return
#def myself(name=0,age) -> 오류발생.초기값 설정한 매개변수는 뒤에 와야함.

#전역변수와 지역변수 차이. 
a=1
def vartest(a):
    a = a+1
    
vartest(a)
print(a)

#함수가 외부값 변화시키게 하는 방법 
a = vartest(a)
#global은 안쓰는게좋음

#lambda예약어
add= lambda a,b : a+b
result =add(3,5)
print(result)