
#USERNAMES
user1 = {
    'name': 'dean',
    'age': '25',
    'nationality': 'British'
}


the_users_age = int(user1['age'])
print("You are currently: " + str(the_users_age))
int(the_users_age)

while True:
    time_amount = input("How many years would you like to go back in time?: ")

    print("WAIT")
    try:
        if time_amount.isdigit():
            pass
        if time_amount.isdigit() > the_users_age:
            print("\n\nYou can't go back THAT far, you weren't even born!\n\n")
            pass
        if time_amount.isdigit() > the_users_age:
            pass
        if time_amount.isdigit() > 0:
            break
        elif type(time_amount) == str:
            print("Enter a numeric value")
            pass
    except ValueError:
        print("\n\nPlease make sure you are entering a number!\n\n")
        pass


the_users_age = the_users_age - int(time_amount)
the_users_age = str(the_users_age)
time_amount = str(time_amount)


input("Press ENTER to start the time machine...")
print("You use the time machine..\n\n")
input("Press ENTER to step out of the time machine...")

print("You are now " + time_amount + " years younger at the age of " + the_users_age)








