class test(Exception):
    def __init__(self,name,mg,):
        self.name = name
        self.mg = mg

obj = test("Amit01","Name is Invalid")
print(obj.name)