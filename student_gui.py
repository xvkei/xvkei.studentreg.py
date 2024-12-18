from tkinter import *  # importing tkinter for gui
from tkinter import filedialog  # importing filedialog for file operations
from functools import partial  # importing partial to pass arguments to functions
from student import StudentInfo  # importing student information module
from add_student import AddStudent  # importing add student module
from search_student import SearchStudent  # importing search student module
from print_all_student import PrintAllStudent  # importing print all students module

# creating instances of modules for managing student information
stu = StudentInfo()
addstud = AddStudent(stu)
searchstud = SearchStudent(stu)
print_all_stud = PrintAllStudent(stu)

# setting a callback to refresh the table when a new student is added
addstud.set_update_view_callback(print_all_stud.refresh_table)

# initializing logged-in user as none
logged_in_user = None

# creating main application window
win = Tk()
win.title("Student System")  # setting window title
# setting window size and centering it on the screen
win.geometry(f"1200x800+{(win.winfo_screenwidth() - 1200) // 2}+{(win.winfo_screenheight() - 800) // 2}")

# defining menu button texts
btn_txt = ["My Info", "Search Student", "Register Student", "View Student", "Logout"]

# function to confirm login
def login_confirm():
    global logged_in_user  # using global variable for logged-in user
    user_id = txt_user.get().strip()  # getting user input and removing extra spaces
    logged_in_user = searchstud.verify_login(user_id)  # verifying login

    if logged_in_user:  # if login is successful
        login_frame.pack_forget()  # hide login frame
        main_frame.pack(fill="both", expand=True)  # show main frame

        # ensuring only home frame is displayed initially
        for frame in container:
            if frame.winfo_ismapped():
                frame.pack_forget()
        container[0].pack(side="right", fill="both", expand=True)

        refresh_home_page()  # refresh home page with user details
    else:  # if login fails
        lbl_login_error.config(text="Invalid Student ID. Please try again.")  # show error message
        txt_user.delete(0, END)  # clear input field

# function to switch between frames
def open_frame(frame_open, close):
    for frame in close:  # hiding all frames in the 'close' list
        if frame.winfo_ismapped():
            frame.pack_forget()
    frame_open.pack(side="right", fill="both", expand=True)  # showing the required frame

# function to log out the user
def logout_confirm():
    global logged_in_user  # resetting logged-in user to none
    logged_in_user = None
    txt_user.delete(0, END)  # clearing the input field
    lbl_login_error.config(text="")  # clearing error message

    # hiding all container frames
    for frame in container:
        if frame.winfo_ismapped():
            frame.pack_forget()

    main_frame.pack_forget()  # hiding main frame
    login_frame.pack(fill="both", expand=True)  # showing login frame

# function to refresh home page with user details
def refresh_home_page():
    for widget in container[0].winfo_children():  # clearing all widgets in the home container
        widget.destroy()

    if logged_in_user:  # if user is logged in
        # displaying welcome message
        Label(container[0], text="Welcome to Your Profile!", font=("Tahoma", 24, "bold"), fg="white", bg="#1E1E24").pack(pady=20)

        # creating profile section
        profile_frame = Frame(container[0], bg="#FB9F89", padx=20, pady=20, relief="ridge", borderwidth=2)
        profile_frame.pack(pady=20, padx=10)

        # creating details section
        details_frame = Frame(profile_frame, bg="#FB9F89")
        details_frame.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        # displaying user details (name, age, id, email, phone)
        labels = ["Name:", "Age:", "Student ID:", "Email:", "Phone:"]
        values = [
            logged_in_user[0],
            logged_in_user[1],
            logged_in_user[2],
            logged_in_user[3],
            logged_in_user[4],
        ]

        for i, (label_text, value) in enumerate(zip(labels, values)):
            Label(details_frame, text=label_text, font=("Tahoma", 12, "bold"), bg="#FB9F89").grid(row=i, column=0, sticky="e", pady=5)
            Label(details_frame, text=value, font=("Tahoma", 12), bg="#FB9F89").grid(row=i, column=1, sticky="w", pady=5)

# creating login frame
login_frame = Frame(win, bg="black")
login_frame.pack(fill="both", expand=True)

# creating login form
login_form = Frame(login_frame, bg="white", padx=20, pady=20)
login_form.place(relx=0.5, rely=0.5, anchor="center")
Label(login_form, text="Please enter your Student ID", font=("Tahoma", 18, "bold"), bg="white").pack()

# user id input field
txt_user = Entry(login_form, width=30, font=("Tahoma", 15))
txt_user.pack(pady=5)

# error message label
lbl_login_error = Label(login_form, text="", font=("Tahoma", 10), fg="red", bg="white")
lbl_login_error.pack(pady=5)

# login and exit buttons
login_btn = Button(login_form, text="Login", bg="skyblue", width=15, font=("Tahoma", 15, "bold"), command=login_confirm)
login_btn.pack(pady=5)
exit_btn = Button(login_form, text="Exit", bg="skyblue", width=15, font=("Tahoma", 15, "bold"), command=win.quit)
exit_btn.pack(pady=5)

# creating main frame and menu
main_frame = Frame(win, bg="#1E1E24")

menu_contain = Frame(main_frame, bg="#C4AF9A")
menu_contain.pack(side="left", fill="y")

content_frame = Frame(main_frame, bg="#1E1E24")
content_frame.pack(side="right", fill="both", expand=True)

# creating containers for each section
container = [Frame(content_frame, bg="#1E1E24") for _ in range(len(btn_txt) - 1)]

# defining functions for each button
func = [
    partial(open_frame, container[0], container[1:]),
    partial(open_frame, container[1], container[:1] + container[2:]),
    partial(open_frame, container[2], container[:2] + container[3:]),
    partial(open_frame, container[3], container[:3]),
    logout_confirm
]

# mouse hover effect on menu buttons
def on_enter(e):
    e.widget['bg'] = '#C4AF9A'

def on_leave(e):
    e.widget['bg'] = '#C4AF9F'

# creating menu buttons
for i, text in enumerate(btn_txt):
    btn = Button(
        menu_contain,
        text=text,
        bg="#C4AF9A",
        width=20,
        font=("Tahoma", 16, "italic"),
        command=func[i],
        relief="groove",
        bd=2
    )
    btn.pack(pady=10)
    btn.bind("<Enter>", on_enter)  # change color on hover
    btn.bind("<Leave>", on_leave)  # reset color when not hovering

# initializing individual ui sections
searchstud.show_search_ui(container[1])
addstud.show_reg_ui(container[2])
print_all_stud.print_all_students_gui(container[3])

# starting the main event loop
win.mainloop()