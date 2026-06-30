import pyfiglet

text_art = pyfiglet.figlet_format("Magico Apps\nPython job")
print(text_art)

python_student = input("Are you proficient in Python? (yes/no): ").lower()
years_of_experience = int(input("How many years of experience or projects do you have?: "))
quiz3 = input("Are you a computer science graduate or have you completed an intensive training camp? (yes/no): ").lower()


if (python_student == "yes" or python_student=="y") and ((years_of_experience >= 2) or (quiz3 == "yes" or quiz3 == "y")):
    print("Congratulations! You have been accepted to the next stage of interviews.")
else:
    print("Sorry, your current qualifications do not match the job requirements.")