class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name} is created.")

    # Destructor
    def __del__(self):
        print(f"Person {self.name} is destroyed.")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("SHYAM", 30)
person1.display_info()

person2 = Person("RAM", 25)
person2.display_info()

del person1

del person2

# OUTPUT:-
# Person SHYAM is created.
# Name: SHYAM, Age: 30
# Person RAM is created.
# Name: RAM, Age: 25
# Person SHYAM is destroyed.
# Person RAM is destroyed.