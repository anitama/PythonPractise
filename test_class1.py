class TestCase1():
    count=0
    def __init__(self,name,age):
        print("constructor")
        self.name1=name
        self.age1=age
        print(self.name1,self.age1)

    def m1(self):
        print("m1",self.name1)


tc1=TestCase1("anita",30)
tc2=TestCase1("ani",40)
tc1.m1()
print("tc1",tc1.count)
tc1.count=3
print("tc1",tc1.count)
tc2.m1()
print("tc2",tc2.count)