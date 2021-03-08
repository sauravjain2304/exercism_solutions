def convert(number):
  a = ""
  if number%3 == 0:
    
    # print("pling")
    a = a + "Pling"
    
  if number%5 == 0:
    
    #print("plang")
    a = a + "Plang"
      
  if number%7 == 0:
    
    # print("plong")
    a =a + "Plong"

  if a == "":
    
    # print(number)
    a = f"{number}"
    
  return a  
convert(73)
