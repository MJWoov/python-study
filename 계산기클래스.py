class FourCal():
    mod = 1     #클래스변수
    def __init__(self,first,second):   #생성자
        self.first =first
        self.second = second
        
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        return self.first+self.second
    def mul(self):
        return self.first*self.second
    def sub(self):
        return self.first-self.second
    def div(self):
        return self.first//self.second

class MoreFourCal(FourCal):         #상속
    def pow(self):
        return self.first**self.second

class SafeFourCal(FourCal):         #메서드오버라이딩
    def div(self):
        if self.second ==0:
            return 0
        else : return self.first//self.second


a = FourCal(3,4)
print(a.add())
print(a.div())
print(a.sub())
print(a.mul())
print(a.mod)
b= FourCal(3,4)
b.mul()
print(b.mod)
c=MoreFourCal(5,7)
print(c.pow())
d = SafeFourCal(3,0)
print(d.div())