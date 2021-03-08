def to_rna(dna_strand):
  rna_strand = ""
  dna_dict = {"C": "G", "G": "C", "T": "A", "A": "U"}
  for element in dna_strand:
    rna_strand += dna_dict[element]
  return rna_strand
print(to_rna("AGCTTCGA"))  
