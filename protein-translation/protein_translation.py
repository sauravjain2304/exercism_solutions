PROTEIN_NAMES = {
    "AUG":	"Methionine",
    "UUU": "Phenylalanine",
    "UUC":	"Phenylalanine",
    "UUA": "Leucine", 
    "UUG":	"Leucine",
    "UCU":	"Serine", 
    "UCC":	"Serine", 
    "UCA":	"Serine", 
    "UCG":	"Serine",
    "UAU": "Tyrosine",
     "UAC": "Tyrosine",
    "UGU": "Cysteine", 
    "UGC":	"Cysteine",
    "UGG":	"Tryptophan",
    "UAA": "STOP", 
    "UAG": "STOP", 
    "UGA"	: "STOP"
}
def proteins(strand):
  result = []    
  for i in range(0, len(strand), 3):
    codon = strand[i:i+3]
    if PROTEIN_NAMES[codon] == "STOP":
      return result
    result.append(PROTEIN_NAMES[codon])
  return result