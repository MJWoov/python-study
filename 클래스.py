class FourCal():
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


a = FourCal()
a.setdata(3,4)
print(a.add())
print(a.div())
print(a.sub())
print(a.mul())
b= FourCal()
b.setdata(5,2)
b.mul()
