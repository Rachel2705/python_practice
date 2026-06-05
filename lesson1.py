dna = 'ATGCGTACGTTAG'

def calculate_gc_content(sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    gc_content = (g_count + c_count) / len(sequence) * 100
    return gc_content

def get_reverse_complement(sequence):
    complement = sequence.replace("A", "t")
    complement = complement.replace("T", "a")
    complement = complement.replace("G", "c")
    complement = complement.replace("C", "g")
    complement = complement.upper()

    reverse_complement = complement[::-1]
    return reverse_complement

length = len(dna)

a_count = dna.count('A')
t_count = dna.count('T')
g_count = dna.count('G')
c_count = dna.count('C')

gc_content = calculate_gc_content(dna)

print("DNA sequence:", dna)
print("Length:", length)
print("A count:", a_count)
print("T count:", t_count)
print("G count:", g_count)
print("C count:", c_count)
print("GC content:", round(gc_content, 2), "%")

complement = dna.replace("A", "t")
complement = complement.replace("T", "a")
complement = complement.replace("G", "c")
complement = complement.replace("C", "g")
complement = complement.upper()

reverse_complement = complement[::-1]
print("complement:", complement)
print("Reverse complement:", reverse_complement)