#Assume variable a holds 21 and variable b holds 10, then:-
a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - value of c is ", c)

c += a 
print ("Line 2 - value of c is ", c)

c *= a 
print ("Line 3 - value of c is ", c)

c /= a 
print ("Line 4 - value of c is ", c)

c = 2
c %= a 
print ("Line 5 - value of c is ", c)

c **= a 
print ("Line 6 - value of c is ", c)

c //= a
print ("Line 7 - value of c is ", c)

#Results
#Line 1 - Value of c is 31
#Line 2 - Value of c is 52
#Line 3 - Value of c is 1092
#Line 4 - Value of c is 52.0
#Line 5 - Value of c is 2
#Line 6 - Value of c is 2097152
#Line 7 - Value of c is 99864