from tkinter import *  # importing tkinter for gui
from tkinter import ttk  # importing ttk for advanced widgets like treeview


class PrintAllStudent:
    def __init__(self, student_info):
        self.student_info = student_info  # reference to the student information object
        self.student_table = None  # initializing the table widget

    def refresh_table(self):
        if self.student_table:  # check if the table exists
            for row in self.student_table.get_children():  # iterate through all rows in the table
                self.student_table.delete(row)  # delete each row

            for student in self.student_info.allstudents:  # loop through all students
                if len(student) == 5:  # ensure the student entry has exactly 5 elements
                    name, age, id_num, email, phone = student  # unpack student details
                    self.student_table.insert("", "end", values=(name, age, id_num, email, phone))  # insert row into table
                else:  # if the student entry is invalid
                    print(f"Skipping invalid entry: {student}")  # log the invalid entry

    def print_all_students_gui(self, print_frame):
        for widget in print_frame.winfo_children():  # remove any existing widgets in the frame
            widget.destroy()

        # create a label for the table title
        title_label = Label(print_frame, text="All Students Information", font=("Tahoma", 16, "bold"), fg="white", bg="#1E1E24")
        title_label.pack(pady=10)  # add some padding around the title

        # create a frame to hold the table and scrollbars
        table_frame = Frame(print_frame)
        table_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)  # add padding around the frame

        # create vertical and horizontal scrollbars for the table
        scrollbar_y = Scrollbar(table_frame, orient=VERTICAL)  # vertical scrollbar
        scrollbar_x = Scrollbar(table_frame, orient=HORIZONTAL)  # horizontal scrollbar

        # create the treeview table for displaying students
        student_table = ttk.Treeview(
            table_frame,
            columns=("Name", "Age", "ID Number", "Email", "Phone"),  # define the table columns
            show="headings",  # show only the headings, not the default column
            yscrollcommand=scrollbar_y.set,  # link vertical scrollbar to table
            xscrollcommand=scrollbar_x.set   # link horizontal scrollbar to table
        )

        self.student_table = student_table  # store a reference to the table widget

        # define the column headings for the table
        student_table.heading("Name", text="Name")
        student_table.heading("Age", text="Age")
        student_table.heading("ID Number", text="ID Number")
        student_table.heading("Email", text="Email")
        student_table.heading("Phone", text="Phone")

        # set the width and alignment of each column
        student_table.column("Name", width=150, anchor="center")
        student_table.column("Age", width=50, anchor="center")
        student_table.column("ID Number", width=100, anchor="center")
        student_table.column("Email", width=200, anchor="center")
        student_table.column("Phone", width=150, anchor="center")

        # configure the scrollbars to work with the table
        scrollbar_y.config(command=student_table.yview)  # connect vertical scrollbar
        scrollbar_x.config(command=student_table.xview)  # connect horizontal scrollbar
        scrollbar_y.pack(side=RIGHT, fill=Y)  # place vertical scrollbar on the right
        scrollbar_x.pack(side=BOTTOM, fill=X)  # place horizontal scrollbar at the bottom
        student_table.pack(fill=BOTH, expand=True)  # fill the frame with the table

        self.refresh_table()  # refresh the table to display current student data