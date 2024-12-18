from student import *  # import all classes and functions from the student module
from search_student import *  # import all classes and functions from the search_student module
from print_all_student import *  # import all classes and functions from the print_all_student module
from add_student import *  # import all classes and functions from the add_student module
from main_menu import MainMenu  # import the MainMenu class from the main_menu module
import os  # import os module for operating system-specific commands

# create an instance of the StudentInfo class to manage student data
stu = StudentInfo()

# create an instance of the AddStudent class and pass the student data object
addstud = AddStudent(stu)

# create an instance of the SearchStudent class and pass the student data object
search = SearchStudent(stu)

# create an instance of the PrintAllStudent class and pass the student data object
printAll = PrintAllStudent(stu)

# create an instance of the MainMenu class and pass the add, search, and print functionalities
menu = MainMenu(addstud, search, printAll)

# initialize the number of login attempts
attempts = 0

# loop to handle login attempts, allowing a maximum of 4 tries
while attempts < 4:
    # clear the terminal screen based on the operating system
    os.system("cls" if os.name == "nt" else "clear")

    # display the login title
    print('=' * 10, "Login - Student Info. System", '=' * 10)

    # prompt the user to enter their student id
    login_check = input('Enter your Student ID: ')

    # verify the login by checking if the student id exists
    user = search.verify_login(login_check)

    if user:  # if the login is successful
        # display a welcome message with the user's name
        print(f"Welcome, Admin {user[0]}")

        # wait for the user to press enter to continue
        input("Press enter to continue...")

        # clear the screen before showing the main menu
        os.system("cls" if os.name == "nt" else "clear")

        # show the main menu, passing the user details
        menu.show_main_menu(user)

        # exit the loop as the login was successful
        break
    else:  # if the login fails
        # increment the number of failed attempts
        attempts += 1

        # display an error message and the remaining attempts
        print(f'The student with the ID number {login_check} does not exist.\nAttempts left: {4 - attempts}')