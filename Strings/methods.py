#1. String capitalize() Method - returns a copy of the string with only its first character capitalized.
#Example
str = "this is python programming....wow!!!"
print ("str.capitalize() : ", str.capitalize())

#Result
#str.capitalize() : This is python programming....wow!!!

#2. String center() Method - Returns centered in a string of length width. Padding is done using the specified fillchar. Default filler is a space.
#syntax;
#str.center(width[, fillchar])
#Parameters
#width - This is the total width of the string.
#fillchar - This is the filler character.
#This method returns a string that is at least width characters wide, created by padding the string with the character fillchar (default is a space).

str = "this is python programming....wow!!!"
print ("str.center(40, 'c') : ", str.center(40, 'c')) 
#Result
#str.center(40, 'a') : ccthis is python programming....wow!!!cc

#String count() Method - The count() method returns the number of occurrences of substring sub in the range [start, end]. 
#Optional arguments start and end are interpreted as in slice notation.
#Syntax 
# str.count(sub, start= 0,end=len(string))
#Parameters
# sub - This is the substring to be searched.
# start - Search starts from this index. First character starts from 0 index. By default search starts from 0 index.
# end - Search ends from this index. First character starts from 0 index. By default search ends at the last index.

str = "this is python programming....wow!!!"
sub='i'
print ("str.count('i') : ", str.count(sub))
sub='exam'
print("str.count('exam', 10, 40) : ", str.count('exam', 10, 40))

#The other methods have been explained in other codes. 