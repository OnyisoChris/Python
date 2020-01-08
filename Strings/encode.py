#String encode() Method
#The encode() method returns an encoded version of the string. Default encoding is the current default string encoding. The errors may be given to set a different error handling scheme.
#Syntax
#str.encode(encoding='UTF-8',errors='strict')
#Parameters
#encoding - This is the encodings to be used. For a list of all encoding schemes please visit: Standard Encodings.
# errors - This may be given to set a different error handling scheme. The default for errors is 'strict', meaning that encoding errors raise a UnicodeError.
# Other possible values are 'ignore','replace','xmlcharrefreplace','backslashreplace' and any other name registered via codecs.register_error()..

import base64
str = 'this is python programming....wow!!!'
str=base64.b64encode(str.encode('utf-8',errors='strict'))
print ("Encoded String: ", str)