from tkinter import *  # importing tkinter for gui
import tkinter.messagebox  # importing messagebox for showing pop-up messages


class SearchStudent:
    def __init__(self, student):
        self.student_data = student  # initializing with reference to the student data

    def search_student(self, keyword):
        for student in self.student_data.allstudents:  # iterating through all students
            if student[2] == keyword.strip():  # checking if the student id matches the keyword
                return student  # returning the student details if found
        return None  # returning none if no match is found

    def verify_login(self, idnum):
        for student in self.student_data.allstudents:  # iterating through all students
            if student[2] == idnum.strip():  # checking if the student id matches the input id
                return student  # returning the student details if found
        return False  # returning false if no match is found

    def show_search_ui(self, search_frame):
        for widget in search_frame.winfo_children():  # clearing any existing widgets in the search frame
            widget.destroy()

        # creating a frame to center the search form
        form_frame = Frame(search_frame, bg="#FB9F89", padx=20, pady=20)
        form_frame.place(relx=0.5, rely=0.5, anchor="center")  # placing the frame in the center

        # adding a title label for the search form
        Label(form_frame, text="Search Student", font=("Tahoma", 16, "bold"), bg="#FB9F89").grid(row=0, column=0, columnspan=2, pady=10)

        # adding a label and input field for entering the student id
        Label(form_frame, text="Enter Student ID", font=("Tahoma", 12), bg="#FB9F89", anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_id = Entry(form_frame, width=30, font=("Tahoma", 12))  # creating an entry field for id input
        self.entry_id.grid(row=1, column=1, padx=10, pady=5)

        # adding a label to display search results or error messages
        self.lbl_result = Label(form_frame, text="", font=("Tahoma", 12), bg="#FB9F89", fg="red", wraplength=400, justify="left")
        self.lbl_result.grid(row=2, column=0, columnspan=2, pady=10)

        # adding a search button to trigger the search operation
        search_btn = Button(form_frame, text="Search", font=("Tahoma", 12), bg="skyblue", command=self.handle_search)
        search_btn.grid(row=3, column=0, columnspan=2, pady=10)

    def handle_search(self):
        student_id = self.entry_id.get().strip()  # getting the id input from the user and removing extra spaces
        if not student_id:  # checking if the input field is empty
            self.lbl_result.config(text="Please enter a student ID.")  # displaying an error message
            return

        result = self.search_student(student_id)  # searching for the student using the input id
        if result:  # if a student is found
            # formatting the student's details into a string
            student_details = (
                f"Name: {result[0]}\n"
                f"Age: {result[1]}\n"
                f"Student ID: {result[2]}\n"
                f"Email: {result[3]}\n"
                f"Phone: {result[4]}"
            )
            self.lbl_result.config(text=student_details, fg="black")  # displaying the student's details
        else:  # if no student is found
            self.lbl_result.config(text="Student not found. Please check the ID and try again.", fg="red")  # showing error
