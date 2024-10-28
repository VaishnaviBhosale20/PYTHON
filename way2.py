# Function to take multiple arguments
def add(datatype, *args):
    if datatype == 'int':
        answer = 0

    if datatype == 'str':
        answer = ''

    for x in args:
        answer = answer + x
    print(answer)

add('int', 5, 6)
add('str', 'hello ', 'Everyone')

# OUTPUT:-
# 11
# hello Everyone