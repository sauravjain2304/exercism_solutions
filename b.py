def cal(num1,num2):
  choice = input("Enter choice(1/2/3/4):")  
  num1 = int(input("Enter first number: "))  
  num2 = int(input("Enter second number: "))  
  
  if choice == '1':  
   print(num1,"+",num2,"=")  
  
  elif choice == '2':  
   print(num1,"-",num2,"=")  
  
  elif choice == '3':  
   print(num1,"*",num2,"=")  
  
  elif choice == '4':  
   print(num1,"/",num2,"=")  
  
  else:  
   print("Invalid input") 

cal(3,6)   