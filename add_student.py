from tkinter import *  # importing tkinter for gui
from functools import partial  # importing partial for function arguments
import tkinter.messagebox  # importing messagebox for popup messages

class AddStudent:
    def __init__(self, student_data):
        self.student_data = student_data  # storing reference to the student data
        self.update_view_callback = None  # initializing callback function for refreshing views

    # method to set a callback function
    def set_update_view_callback(self, callback):
        self.update_view_callback = callback  # setting the callback function

    # method to add a student to the system
    def add_student(self, name, age, idnum, email, phone):
        self.student_data.setName(name)  # setting the student's name
        self.student_data.setAge(age)  # setting the student's age
        self.student_data.setIDNum(idnum)  # setting the student's id
        self.student_data.setEmail(email)  # setting the student's email
        self.student_data.setPhoneNum(phone)  # setting the student's phone number

        # creating a list to represent the student
        student_written = [name, age, idnum, email, phone]

        # adding the student to the allstudents list
        self.student_data.allstudents.append(student_written)
        print(f"Added student {student_written[0]} to the list.")  # logging success

        # formatting student details as a string for file storage
        student_string = f"{name}, {age}, {idnum}, {email}, {phone}\n"
        self.write_to_file(student_string)  # writing student data to file

        if self.update_view_callback:  # if a view update callback is set
            self.update_view_callback()  # refresh the view

    # method to write student data to a file
    def write_to_file(self, student_string):
        try:
            with open("student_data.txt", "a") as file:  # opening the file in append mode
                file.write(student_string)  # writing the student data to the file
            print("Data saved successfully.")  # logging success
        except IOError as e:  # handling file errors
            print(f"An error occurred while saving data: {e}")  # logging error

    # method to display the registration ui
    def show_reg_ui(self, reg_frame):
        for widget in reg_frame.winfo_children():  # clearing any existing widgets in the frame
            widget.destroy()

        # creating a form frame for registration
        form_frame = Frame(reg_frame, bg="#FB9F89", padx=20, pady=20)
        form_frame.place(relx=0.5, rely=0.5, anchor="center")  # centering the form

        # adding a title label
        Label(form_frame, text="Register New Student", font=("Tahoma", 16, "bold"), fg="black", bg="#FB9F89").grid(row=0, column=0, columnspan=2, pady=10)

        # adding an error label for validation messages
        self.lblErrors = Label(form_frame, text="", font=("Tahoma", 12), fg="red", bg="#FB9F89")
        self.lblErrors.grid(row=1, column=0, columnspan=2, pady=(0, 10))

        # defining fields for registration
        self.reg_txt = ["Name", "Age", "Student ID", "Email", "Phone"]
        self.reg_entry = []  # list to store input fields

        # creating labels and entry widgets for each field
        for i, field in enumerate(self.reg_txt):
            Label(form_frame, text=field, font=("Tahoma", 12), bg="#FB9F89", anchor="w").grid(row=i + 2, column=0, padx=10, pady=5, sticky="w")
            entry = Entry(form_frame, width=30, font=("Tahoma", 12))  # creating entry widget
            entry.grid(row=i + 2, column=1, padx=10, pady=5)  # placing entry widget
            self.reg_entry.append(entry)  # storing reference to the entry widget

        # creating a register button
        reg_btn = Button(form_frame, text="Register", font=("Tahoma", 12), bg="skyblue", command=self.check_entries)
        reg_btn.grid(row=len(self.reg_txt) + 2, column=0, columnspan=2, pady=10)

    # method to validate input fields
    def check_entries(self):
        errors = []  # list to store validation errors
        for i, entry in enumerate(self.reg_entry):
            if not entry.get().strip():  # checking if input is empty
                errors.append(f"- {self.reg_txt[i]} is required")  # adding error message

        if errors:  # if there are validation errors
            self.lblErrors.config(text="\n".join(errors))  # displaying errors
        else:
            # adding the student if inputs are valid
            self.add_student(
                self.reg_entry[0].get(),  # name
                self.reg_entry[1].get(),  # age
                self.reg_entry[2].get(),  # student id
                self.reg_entry[3].get(),  # email
                self.reg_entry[4].get()   # phone
            )
            tkinter.messagebox.showinfo("Success", "Student registered successfully!")  # showing success popup

            # clearing all input fields
            for entry in self.reg_entry:
                entry.delete(0, END)

            # clearing the error message
            self.lblErrors.config(text="")