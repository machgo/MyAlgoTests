#!/usr/local/bin/python3
print("knuth")
# i = i + m - (l-1)
#
data = "abacbbababcabcabbab"
pattern = "ababc"

# build table of shift amounts
shifts = [0] * (len(pattern) + 1)
shift = 0
for pos in range(len(pattern)):
    while shift <= pos and pattern[pos] != pattern[pos-shift]:
        shift += shifts[pos-shift]
    shifts[pos+1] = shift

# do the actual search
startPos = 0
matchLen = 0
for c in data:
    while matchLen == len(pattern) or matchLen >= 0 and pattern[matchLen] != c:
        startPos += shifts[matchLen]
        matchLen -= shifts[matchLen]
    matchLen += 1

print(shifts)
