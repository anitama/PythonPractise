class TestCase2():
    companyName="BETSOL"
    def __init__(self,empname,empage):
        self.empname1=empname
        self.empage1=empage
        self.project="Avaya"
        self.manager="XYZ"
        self.companyName
        self.a=10

    def m1(self):
        print("EMP name is :",self.empname1)
        print("EMP age is : ",self.empage1)

    def m2(self):
        print("Company is : ",TestCase2.companyName)
        print("Project is :",self.project)
        print("Manager is ",self.manager)

    @classmethod
    def m3(cls):
        cls.x=20
        cls.add="HSR"
        TestCase2.p=99000
        TestCase2.companyName = "AVAYA 2"

    @staticmethod
    def m4():
        TestCase2.hink="Mobile"
        TestCase2.companyName="AVAYA 2"


tc1=TestCase2("Anita",30)
tc1.m1()
tc1.m2()
tc1.b=100
TestCase2.m3()
TestCase2.m4()
print(tc1.__dict__)
print(TestCase2.__dict__)