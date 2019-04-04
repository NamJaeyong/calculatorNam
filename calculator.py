from module import *



while True:
   
   print("1.Add")
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divide")
   print("5.Stop")

   choice = input("골라(1/2/3/4/5):")

   if choice == "5":
      break
   
   if choice not in ['1','2','3','4']:
      print ("적당히 해라")
      continue

   num1 = int(input("Num1:"))
   num2 = int(input("Num2:"))
   

   if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

   elif choice == '2':
    print(num1,"-",num2,"=", sub(num1,num2))

   elif choice == '3':
    print(num1,"*",num2,"=", mul(num1,num2))

   elif choice == '4':
    if num2 == int("0"):
         print("문과 티내냐?")
         break
    else:
      print(num1,"/",num2,"=", div(num1,num2))

       


   
