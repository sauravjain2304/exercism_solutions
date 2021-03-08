def calculate():
  print('+')
  print('-')
  print('*')
  print('/')
  operation = input("Select an operator:n")
  print("Enter two numbers")
  number_1 = int(input())
  number_2 = int(input())

  if operation == '+':
    print(number_1 + number_2)

  elif operation == '-': 
    print(number_1 - number_2)

  elif operation == '*': 
    print(number_1 * number_2)

  elif operation == '/': 
    print(number_1 / number_2)

  else:
    print('Invalid Input')
calculate()



#   for element in dna_strand:
#     if element == "C":
#       rna_strand += "G"
#     elif element == "G":
#       rna_strand += "C"
#     elif element == "T":
#       rna_strand += "A"
#     elif element == "A":
#       rna_strand += "U"
#   return rna_strand
# print(to_rna("AGCTTCGA"))  
  
    # if element == dna_dict["C"]:
    #   rna_strand += "G"
    # elif element == dna_dict["G"]:
    #   rna_strand += "C"
    # elif element == dna_dict["T"]:
    #   rna_strand += "A"
    # elif element == dna_dict["A"]:
    #   rna_strand += "U"
  