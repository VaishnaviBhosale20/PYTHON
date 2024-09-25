# MULTILEVEL INHERITANCE
class level1:
    def base(self):
        print("Base Class")
class level2(level1):
    def IntermediateClass(self):
        print("Intermediatory Class")
class level3(level2):
    def childclass(self):
        print("Child Class")
ob = level3()
print(ob.childclass())
print(ob.IntermediateClass())
print(ob.base())

# OUTPUT:
# Child Class
# None
# Intermediatory Class
# None
# Base Class
# None