#Assume variable a holds 21 and variable b holds 10, then;
a = 21
b = 10
if ( a == b):
    print ("Line 1 - a is equal to b")
else:
    print ("Line 1 - a is not equal to b")
if ( a != b ):
    print ("Line 2 - a is not equal to b")
else:
    print ("Line 2 - a is equal to b")
if ( a < b ):
    print ("Line 3 - a is less than b")
else:
    print ("Line 3 - a is not less than b")
if ( a > b):
    print ("Line 4 - a is greater than b")
else:
    print ("Line 4 - a is not greater than b")
a,b=b,a #values of a and b swapped. a becomes 10, b becomes 21
if ( a >= b ):
    print ("Line 5 - a is either greater than or eqaul to b")
else:
    print ("Line 5 - a is neither greater than nor equal to b")
if ( a <= b):
    print ("Line 6 - a is either less than or equal to b")
else:
    print ("Line 6 - a is neither less than nor equal b")

#when you execute the above program, it produces the following result:-
#Line 1 - a is not equal to b
#Line 2 - a is not equal to b
#Line 3 - a is not less than b
#Line 4 - a is greater than b
#Line 5 - b is either greater than or equal to b
#Line 6 - a is either less than or equal to b