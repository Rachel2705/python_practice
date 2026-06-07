def calculate_gc_content(sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    gc_content = (g_count + c_count) / len(sequence) * 100
    return gc_content

with open("sequences.txt", "r") as file:
    sequences = file.readlines()

total_bases = 0
lengths = []

for dna in sequences:
    dna = dna.strip()

    print("sequence:", dna)
    print("Length:", len(dna))

    gc_content = calculate_gc_content(dna)
    print("GC content:", round(gc_content, 2), "%")
    print()

    total_bases = total_bases + len(dna)
    lengths.append(len(dna))

total_sequences = len(sequences)
average_length = total_bases / total_sequences
shortest_length = min(lengths)
longest_length = max(lengths)

print("Total sequences:", total_sequences)
print("Total bases:", total_bases)
print("Average length:", average_length)
print("Shortest length:", shortest_length)
print("Longest length:", longest_length)