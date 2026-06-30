import pyfiglet

text_art = pyfiglet.figlet_format("Magico Apps\nATM")
print(text_art)

user_password = int(input("Enter your PIN: "))
password = 1234
balance = 5000

if(user_password == password):
    print("(1)Withdraw")
    print("(2)Check Balance")
    user_choice = int(input("Enter the number of choice: "))

    if user_choice == 2:
        print(f"Your current bank account balance is {balance}$")
    elif user_choice == 1:
        amount = int(input("Please enter the withdrawal amount: "))
        if amount <= balance and amount > 0:
            balance = balance - amount
            print(f"Transaction successful. Your remaining balance is {balance}$")
        else:
            print("Insufficient funds")


else:
    print("Wrong Password")