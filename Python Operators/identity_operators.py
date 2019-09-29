a = 20
b = 20
print('Line 1','a=',a,':',id(a),'b=',b,':',id(b))

if (a is b ):
    print("Line 2 - a and b have same identity")
else:
    print ("Line 2 - a and b do not have same identity")

if ( id(a) == id(b) ):
    print("Line 3 - a and b have same identity")
else:
    print("Line 3 - a and b do not have same identity")

b = 30
print ('line 4','a=',a,':',id(a), 'b=',b,':',id(b))

if ( a is not b ):
    print ("Line 5 - a and b do not have same identity")
else:
    print ("Line 5 - a and b have same identity")


#Result
#Line 1 a= 20 : 1594701888 b= 20 : 1594701888
#Line 2 - a and b have same identity
#Line 3 - a and b have same identity
#Line 4 a= 20 : 1594701888 b= 30 : 1594702048
#Line 5 - a and b do not have same identity