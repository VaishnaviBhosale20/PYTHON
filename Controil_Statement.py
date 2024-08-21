#CONTROL STATEMENTS:-
a=int(input("Enter first number:- "))
b=int(input("Enter second number:- "))

if a==b :
    print("if statement")

elif a > b :
    print("elif statement")

else :
    print("else statement")
        # OUTPUT:-
        # Enter first number:- 90
        # Enter second number:- 99
        # else statement

#WHILE LOOP
i=1
while i!=3 :
    print("While loop 2 times")
    i+=1

#FOR LOOP
list1 = ["hello","every", "one"]
for i in range(5) :
    print("for loop 5 times")

        # OUTPUT:-
        # Enter first number:- 89
        # Enter second number:- 90
        # else statement
        # While loop
        # While loop
        # for loop
        # for loop
        # for loop
        # for loop
        # for loop
        # for loop
        # for loop
        # for loop

# having an empty if statement like this, would raise an error without the pass statement

#CONTINUE , BREAK
x=int(input("Enter first number:- "))
y=int(input("Enter second number:- "))
while x > y :
    continue
    print("continue statement")
    y+=2

while y > x :
    print("break statement")
    break
    print("break statement")  #it will not print

