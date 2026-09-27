# EXPENSE TRACKER PROJECT

expenses=[] #List of  all expenses in dictionary
print("Welcome to expense tracker")

while True:
    print("===TO DO===")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. View Total Expense")
    print("4. Exit")

    choice=int(input("Please enter your choice:"))

#1. Add Expense
    if(choice == 1):
        date= input("Select the date of expense :")
        category= input("Select the type of expence : ")
        description=input("Give more details of the expense :")
        amount=float(input("Enter the amount :"))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount

        }
        expenses.append(expense)
        print("\nExpense is added successfully")

#2. VIEW ALL EXPENSES
    elif (choice == 2):
        if(len(expenses)==0):
            print("NO expense added")
        else:
             print("===Your Expense===")
             count=1
             for expenditure in expenses:
                 print(f"Expenditure Number{count}->{expenditure["date"]},{expenditure["category"]},{expenditure["description"]},{expenditure["amount"]}")
                 count= count+1

#3. VIEW TOTAL EXPENSE
    elif(choice==3):
        total=0
        for expenditure in expenses:
            total=total+expenditure["amount"]

        print("\nTotal expenditure=",total)

#4.EXIT
    elif(choice==4):
        print("Thanking You")
        break

    else:
        print("INVALID INPUT")



     


                  
             



