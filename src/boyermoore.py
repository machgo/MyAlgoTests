#!/usr/local/bin/python3
print("boyermoore")
# i = i + m - (l-1)
#
data = "adkflkadjg alsfjaodifjgaoidgjfogijdfiogjaoidfjgoiajgoa"
pattern = "fogo"
lastocc = {}
#for v in sorted(vertexes, key=lambda vertex: vertex.number):
    #print v
i = 0
for c in pattern:
    lastocc.update({c:i})
    i+=1
print(lastocc)

i = 0 
while i < len(data)-len(pattern):
    j = len(pattern)
    while j > 0 and pattern[j-1] == data[i+j-1]:
        j -= 1
    if j > 0:
        badCharShift = badChar.get(haystack[i+j-1], len(needle))
        goodSuffixShift = goodSuffix[len(needle)-j]
        if badCharShift > goodSuffixShift:
            i += badCharShift
        else:
            i += goodSuffixShift
    i+=1
