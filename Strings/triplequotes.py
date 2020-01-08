para_str = """this is a long string that is made up of 
several lines and non-printable characters such as 
TAB ( \t ) and they will show up that  way when displayed.
NEWLINEs within the string, whether explicitly given like 
this within the brackets [ \n ], or just a NEWLINE within 
the variable assignment will also show up.
"""
print (para_str)

#Raw strings do not treat the backlash as a special character at all. Every character you put into a raw string stays the way you wrote it.
print ('C:\\nowhere')

#Result is
# C:\nowhere

#Now we make us of raw string, we would put expression in r'expression' as follows;
print (r'C:\\nowhere')

#Result is
# C:\\nowhere
