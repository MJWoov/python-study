print(''' 
Hello World
''')
print(" It's ")
escapecode = " \n,\t,\\,\',\" "
print(escapecode)

a='Python'

print(len(a))

print(a[-1])
print(a[:4])

###문자열포매팅
#바로대입
print("I eat %d apples" %3)
print('I eat %s apples' %"five")
#변수대입
num =3
print('I eat %d apples' %num)

print("%10s"%"hi") #10칸 오른쪽정렬
print("%0.4f" %0.123456) #소수점 표시

###format함수
print('I eat {0} apples'.format(3))
print('I eat {0} apples'.format("three"))
print('I eat {num} apples for {day} days'.format(num=3,day=5))

print("{0:>10}".format("hi")) #오른쪽정렬
print("{0:<10}".format("hi")) #왼쪽정렬
print("{0:^10}".format("hi")) #가운데정렬
print("{0:=^10}".format("hi")) #공백채우기
print("{0:10.4f}".format(3.14235)) #소수점

##f문자열포매팅
name = 'A' 
age = 10 
y=3.141592
print(f"my name is {name}, {age+1} years old.")
print(f'{"hi":<10}') # 왼쪽 정렬
print(f'{"hi":^10}') # 가운데정렬
print(f'{"hi":=^10}') #공백채우기(=)
print(f'{y:0.4f}') #소수점
