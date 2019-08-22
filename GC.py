#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#Return: The ID of the string having the highest GC-content,
#followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers

FILE = open("ROSAGC.txt", "r")

# Read file and write to dictionary.
def read_write(file):
    dna = {}
    with FILE as openfile:
        for line in openfile:
            # If line starts with >, we use it as the key.
            if line[0] is ">":
                dna[line] = "empty"
                key = line
            # If the key is empty we add a value.
            elif dna.get(key) is "empty":
                dna[key] = line.strip('\n')
            # If key and value exist, we add to the old value.
            else:
                dna[key] = dna.get(key) + line.strip('\n')
    return dna

# Check length of string and occurency of c and g.
def gc_content(dna):
    length = len(dna)
    total = dna.count("C") + dna.count("G")
    final = total / (length/100)
    return final

def main():
    dna = read_write(FILE)
    Winner = [("start", 0)]

    for key in dna:
        gccontent = gc_content(dna.get(key))
        if gccontent > Winner[0][1]:
            Winner[0] = (key.strip('>'), gccontent)

    print(Winner[0][0].strip('\n'), "\n", Winner[0][1])


if __name__ == "__main__":
    main()
