def dna_to_rna(dna):
    return dna.replace('T', 'U')

dna_to_rna("TTTT")  #"UUUU"
dna_to_rna("GCAT")  #"GCAU"
dna_to_rna("GACCGCCGCC")    #"GACCGCCGCC"