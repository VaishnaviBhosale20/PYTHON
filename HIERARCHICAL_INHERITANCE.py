#Hierarchical Inheritance
class level1:
    def fun1(self):
        print("This is Level 1")

class level2(level1):
    def fun2(self):
        print("This is level 2 first function")
    
class level3(level1) :
    def fun3(self):
        print("This is level 2 second function")

obj = level3()
print(obj.fun1())
print(obj.fun3())

ob = level2()
print(ob.fun2())

# OUTPUT:-
# This is Level 1
# None
# This is level 2 second function
# None
# This is level 2 first function
# 
# LEVEL1 --LEVEL 2
#        --LEVEL3