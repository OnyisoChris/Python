#raw strings do not treat the backslash as a special character at all. Every character you put into a raw string stays the way you wrote it;
print('C:\\nowhere')
#after putting r'expression'
print (r'C:\\nowhere')