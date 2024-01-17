# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# Datu tipi, mekle float - https://www.w3schools.com/python/python_datatypes.asp
# Pārbaudēm izmanto if...else - https://www.w3schools.com/python/python_conditions.asp
# Cipari https://www.w3schools.com/python/python_numbers.asp


balance = 0


while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")


    choice = input("Enter your choice (1-4): ")


  
    if choice == '1':
        deposit = (float(input("Enter the amount to deposit:")))
        if deposit > 0:
          balance += deposit
          print("Deposit successful. New balance:", balance)
        else:
          print("Error, cannot deposit.") 


  
  
    elif choice == '2' :
      withdraw = (float(input("Enter the amount to withdraw:")))
      if withdraw > balance:
          print("Insufficient balance. Cannot withdraw.")
      elif withdraw < 0:
          print("Error, cannot withdraw")
      else:
          balance -= withdraw
          print("Withdraw successful. New balance:", balance)
          print(balance)
          pass


  
  
    elif choice == '3':
        print("Current balance:", balance)
        pass


  
  
    elif choice == '4':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
