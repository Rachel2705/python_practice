def validate_dna(sequence):
    is_valid = True

    for base in sequence:
        if base not in "ATGC":
            print("Invalid base found:", base)
            is_valid = False

    return is_valid

sequences = [
     "ATGCGTACGTTAG",
     "ATGCBTACGTTAG",
     "GGGCCCATA",
     "TTAXCGTA"
]

for dna in sequences:
    print("checking sequence:", dna)
    
    result = validate_dna(dna)

    if result:
        print("valid DNA sequence")
    else:
        print("Invalid DNA sequence")
    
    print()
