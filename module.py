import module1

from module1 import add
from module1 import*

import module2

a=module2.Math()
print(module2.PI)

import sys

print(sys.path)
sys.path.append("C:/Users/user/Documents/GitHub/python-study") #폴더를 파이썬 설치 파일위치에 추가하여 어디서든 import 가능하게.

set pythonpath  = C:/Users/user/Documents/GitHub/python-study