#Given: A DNA string s of length at most 1000 bp.
#Return: The reverse complement s^c of s.

DNA = "AAAACCCGGT"

def reverse_complement(dna):
    dna = []
    c_dna = []
    dna[:0] = DNA[::-1]

    for i in dna:
        if i is "C":
            c_dna.append("G")
        elif i is "G":
            c_dna.append("C")
        elif i is "A":
            c_dna.append("T")
        elif i is "T":
            c_dna.append("A")

    cs_dna = ''.join(c_dna)
    return cs_dna

print(reverse_complement(DNA))


