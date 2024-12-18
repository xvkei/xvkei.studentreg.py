import os  # Import os for clearing the terminal

class MainMenu:
    def __init__(self, add_student_manager, search_manager, print_all_manager):
        self.add_student_manager = add_student_manager
        self.search_manager = search_manager
        self.print_all_manager = print_all_manager

    def show_menu(self):
        print("\nPlease choose from the following options:")
        print("[1] - View your information")
        print("[2] - View other's student information")
        print("[3] - Register a new student")
        print("[4] - Exit")
        return input("Enter your choice: ")

    def show_view_other_menu(self):
        print("\nDo you want to:")
        print("[1] - Display all student information")
        print("[2] - Search for a specific student by ID")
        return input("Enter your choice: ")

    def show_main_menu(self, current_student):
        while True:  # Loop until the user decides to exit
            os.system("cls" if os.name == "nt" else "clear")  # Clear the terminal at the beginning
            print("\nPlease choose from the following options:")
            print("[1] - View your information")
            print("[2] - View other's student information")
            print("[3] - Register a new student")
            print("[4] - Exit")
            
            choice = input("Enter your choice: ")

            if choice == '1':
                # Access student information using indices
                print(f"Your Information:\nName: {current_student[0]}\nAge: {current_student[1]}\nStudent ID: {current_student[2]}\nEmail: {current_student[3]}\nPhone: {current_student[4] if len(current_student) > 4 else 'N/A'}")

            elif choice == '2':
                sub_choice = input("\nDo you want to:\n[1] - Display all student information\n[2] - Search for a specific student by ID\nEnter your choice: ")

                if sub_choice == '1':
                    self.print_all_manager.print_all_students()

                elif sub_choice == '2':
                    search_id = input("Enter the student's ID number: ")
                    student = self.search_manager.search_student(search_id)  
                    
                    if student:
                        # Print the student's information if found, using indices
                        print("\nStudent Information:")
                        print(f"Name: {student[0]}")
                        print(f"Age: {student[1]}")
                        print(f"Student ID: {student[2]}")
                        print(f"Email: {student[3]}")
                        print(f"Phone: {student[4] if len(student) > 4 else 'N/A'}")
                    else:
                        print("Student not found.")
                    
                else:
                    print("Invalid choice. Returning to the main menu.")

            elif choice == '3':
                self.add_student_manager.input_add_student()  

            elif choice == '4':
                print("Thank you for using the system. Goodbye!")
                return  # Exit the method to end the program

            else:
                print("Invalid choice. Please try again.")

            # Ask if the user wants to go back to the menu
            go_back = input("Do you want to go back to the menu? [y/n]: ")
            if go_back.lower() == 'y':
                os.system("cls" if os.name == "nt" else "clear")  # Clear terminal when going back to the main menu
            else:
                print("Thank you for using the system. Goodbye!")
                break  # Exit