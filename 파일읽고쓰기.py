f=open("C:/doit/새파일.txt",'w')
f.close

f=open('C:/doit/새파일.txt','w')
for i in range(1,11):
    data = '%d번째 줄입니다.\n'%i
    f.write(data)
f.close()   
 
f = open("C:/doit/새파일.txt",'r') 
while True:
    line = f.readline() 
    if not line:
        break
    print(line)
    
f.close()

f = open("C:/doit/새파일.txt",'r') 
lines = f.readlines()
for line in lines:
    print(line)

f.close()

f = open("C:/doit/새파일.txt",'r') 
print(f.read())
f.close()

f = open("C:/doit/새파일.txt",'a') 
for i in range(11,20):
    f.write('%d번째 줄입니다.\n'%i)
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
    
#sys모듈
import sys
args = sys.argv[1:]
for i in args:
    print(i)