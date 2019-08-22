#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#Return: The Hamming distance dH(s,t).

SEQ1 = "GAGCCTACTAACGGGAT"
SEQ2 = "CATCGTAATGACGGCCT"

counter = 0
total = 0

while counter < len(SEQ1):
	if SEQ1[counter] is not SEQ2[counter]:
		total += 1
	counter += 1

print(total)
