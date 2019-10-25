a = 60          #60 = 0011 1100
b = 13          #13 = 0000 1101
print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

c = a & b;      #12 = 0000 1100
print ("result of AND is ", c, ':',bin(c))

c = a | b;      #61 = 0011 1101
print ("result of OR is ", c,':',bin(c))

c = a ^ b;      # 49 = 0011 0001
print ("result of EXOR is ", c,':',bin(c))

c = ~a;         # -61 = 1100 0011
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;     # 240 = 1111 0000
print ("result of LEFT SHIFT is ",c,':',bin(c))

c = a >> 2;     # 15 = 0000 1111
print("result of RIGHT SHIFT is ", c,':',bin(c))

# result
# a= 60 : 0b111100 b= 13 : 0b1101
# result of AND is 12 : 0b1100
# result of OR is 61 : 0b111101
# result of EXOR is 49 : 0b110001
# result of COMPLEMENT is -61 : -0b111101
# result of LEFT SHIFT is 240 : 0b11110000
# result of RIGHT SHIFT is 15 : 0b111