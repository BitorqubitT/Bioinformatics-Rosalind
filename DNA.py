#Given: A DNA string s of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting the respective number of times that
#the symbols 'A', 'C', 'G', and 'T' occur in s.

X = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

a, c, g, t = 0,0,0,0

for i in X:
    if i is "A":
        a += 1
    elif i is "C":
        c += 1
    elif i is "G":
        g += 1
    elif i is "T":
        t += 1

print(a, c, g, t)
