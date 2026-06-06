sequences = [
    "ATGCGTACGTTAG",
    "GGGCCCATA",
    "TTACGTA",
    "ATATATAT"
]

lengths = []

total_bases = 0

for dna in sequences:
    lengths.append(len(dna))
    print("sequence:", dna)
    print("length:", len(dna))
    print()

    total_bases = total_bases + len(dna)

total_sequences = len(sequences)
average_length = total_bases / total_sequences
shortest_length = min(lengths)
longest_length = max(lengths)

print("Total sequences:", total_sequences)
print("Total bases:", total_bases)
print("Average length:", average_length)
print("Shortest length:", shortest_length)
print("Longest length:", longest_length)