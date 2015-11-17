#!/usr/bin/python

a = 4589374958
b = 3845347985

a1 = 45893
a2 = 74958

b1 = 38453
b2 = 47985

a1b1 = a1*b1
a2b2 = a2*b2

result = a1b1*10^10 + a2b2 + (a1b1 + a2b2 - (a1 -a2)*(b1-b2))*10^5
print result
print a*b

