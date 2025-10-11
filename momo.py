print("MTN MOMO")
print("1. send money")
print("2. buy airtime")
print("3. check balance")
print("4. Exit ")
Chocie= input("Enter your number:")
if Chocie == "1":
   number= input("enter receiver  number:")
   amount= input ("enter amount:")
   print ( f"sending GHS {amount} to {number}")
   print(" transfer successful")
elif Chocie == "2":
    number= input(" Enter amount of money for airtime:")
    amount= input(" enter  receiver number:")
    print(f"Buying GHS{amount}airtime for {number}")
    print(" Airtime successful")
elif Chocie == "3":
    print ( " Your current balance is GHS 1,000,000,000,000,000,000")
else:
    print("thank you for using MTN momo  dear valued customer ")
   
   