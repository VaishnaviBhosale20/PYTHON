# Multiple Inheritance
class level1:
    def fun1(self):
        print("This is Level 1 first function")

class level2:
    def fun2(self):
        print("This is level 1 second function")
    
class level3(level1,level2) :
    def fun3(self):
        print("This is level 2")

obj = level3()
print(obj.fun1())
print(obj.fun2())
print(obj.fun3())



# OUTPUT:-
# This is Level 1 first function
# None
# This is level 1 second function
# None
# This is level 2
# None