
aquapark_name = 'Adaland'
age_limit = 18
passed_message = 'Enjoy the aquapark. You can purchase tickets here: https://bilet.adaland.com/en'

print(f"Welcome to {aquapark_name} aquapark!")

user_input = input("Please, enter your age: ")
print(f"User input is: {user_input}")

if int(user_input) >= age_limit:
    print(passed_message)
else:
    adult_present = input('Is an adult with you? yes or no: ')
    if adult_present.lower() == 'yes':
        print(passed_message)
    else:
        print('Sorry, you must be 18 or come with an adult to visit the aquapark.')