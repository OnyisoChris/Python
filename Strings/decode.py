#String decode() Method
#The decode() method decodes the string using the codec registered for encoding. It defaults to the default string encoding.
# Syntax
# str.decode(encoding='UTF-8', errors='strict')
#Parameters
# encoding - This is the encodings to be used. For a list of all encoding schemes please visit: Standard Encodings.
# errors - This may be given to set a different error handling scheme. The default for errors is 'strict', meaning that encoding errors raise a UnicodeError.
# Other possible values are 'ignore','replace','xmlcharrefreplace','backslashreplace' and any other name registered via codecs.register_error()..

import base64
str = "this is string example....wow!!!";
str = str.encode('base64','strict');
print ("Encoded String: " + str)
print ("Decoded String: " + str.decode('base64','strict'))
