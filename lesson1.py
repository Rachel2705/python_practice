dna = 'ATGCGTACGTTAG'

length = len(dna)

a_count = dna.count('A')
t_count = dna.count('T')
g_count = dna.count('G')
c_count = dna.count('C')

gc_content = (g_count + c_count) / length * 100

print("DNA sequence:", dna)
print("Length:", length)
print("A count:", a_count)
print("T count:", t_count)
print("G count:", g_count)
print("C count:", c_count)
print("GC content:", round(gc_content, 2), "%")