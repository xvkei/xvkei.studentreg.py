class StudentInfo:
    def __init__(self):  
        self.name = ''  # initialize name as an empty string
        self.age = ''  # initialize age as an empty string
        self.idnum = ''  # initialize id number as an empty string
        self.email = ''  # initialize email as an empty string
        self.phone = ''  # initialize phone as an empty string
        self.allstudents = []  # initialize an empty list to store all students
        self.read_file()  # call read_file method to load student data from file

    def setName(self, name):
        self.name = name  # set the name of the student

    def setAge(self, age):
        self.age = age  # set the age of the student

    def setIDNum(self, idnum):
        self.idnum = idnum  # set the id number of the student

    def setEmail(self, email):
        self.email = email  # set the email of the student

    def setPhoneNum(self, phone):
        self.phone = phone  # set the phone number of the student

    def getName(self):
        return self.name  # return the name of the student

    def getAge(self):
        return self.age  # return the age of the student

    def getIDNum(self):
        return self.idnum  # return the id number of the student

    def getEmail(self):
        return self.email  # return the email of the student

    def getPhoneNum(self):
        return self.phone  # return the phone number of the student

    def __str__(self):
        # return a formatted string with student details
        return f'\nName: {self.name}\nAge: {self.age}\nID Number: {self.idnum}\nEmail Address: {self.email}\nPhone Number: {self.phone}\n'

    def read_file(self):
        try:
            with open("student_data.txt", "r") as file:  # open the file in read mode
                lines = file.readlines()  # read all lines from the file
                for line in lines:  # iterate through each line
                    student_data = line.strip().split(", ")  # split the line into a list of student details
                    self.allstudents.append(student_data)  # add the student data list to allstudents
                print("All students loaded. Login to continue.")  # print success message
        except FileNotFoundError:  # handle the case where the file does not exist
            print("No existing student data found.")  # print file not found message