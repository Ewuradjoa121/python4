UserDict={}
print("welcome to The Athenaeum Library")
print("1. Create account")
print("2. Borrow a book ")
print("3. Exit")
choice=input("Enter option (1/2/3):")
if choice=="1":
    userID= input("Enter userID:")
    username=input("Enter Username:")
    address= input("Enter Address:")
    print(f"account for {username} created successfully!")
elif choice=="2":
    userID=input("Enter your User ID:")
    if userID in UserDict:
        book= input("Enter Book name or ID:")
        UserDict[userID]["Book"]=book
    else:
        print("User ID not found create an account!")
elif choice=="3":
    print("Goodbye")
else:
    print("invalid choice ")
