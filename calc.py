import tkinter as tk

def calculate(op):
    try:
        n1, n2 = int(txtbox1.get()), int(txtbox2.get())
        result = {
            "+": n1 + n2, "-": n1 - n2, "x": n1 * n2,
            "÷": n1 / n2 if n2 != 0 else "Undefined", "//": n1 // n2 if n2 else "Err",
            "^": n1 ** n2, "%": n1 % n2 if n2 else "Err"
        }[op]
        number_result.config(text=str(result))
    except ValueError:
        number_result.config(text="Invalid input!")

def create_button(text, op):
    button = tk.Button(button_frame, text=text, font=("Arial", 20),
                       command=get_command(op), width=5)
    button.grid(row=0, column={"+" : 0, "-" : 1, "x" : 2, "÷" : 3, "//" : 4, "^" : 5, "%" : 6}[text], padx=5)

def get_command(op):
    def command():
        calculate(op)
    return command

win = tk.Tk()
win.title("Calculator")
win.geometry("700x350+610+290")
win.configure(bg="#070707")

tk.Label(win, text="Python GUI: Basic Calculator V1", font=("Arial", 24), bg="#070707", fg="white").pack(pady=10)
input_frame = tk.Frame(win, bg="#070707")
input_frame.pack(pady=10)

tk.Label(input_frame, text="First Number:", font=("Arial", 16), bg="#070707", fg="white").grid(row=0)
txtbox1 = tk.Entry(input_frame, width=10, font=("Arial", 16))
txtbox1.grid(row=0, column=1, padx=10)
tk.Label(input_frame, text="Second Number:", font=("Arial", 16), bg="#070707", fg="white").grid(row=1)
txtbox2 = tk.Entry(input_frame, width=10, font=("Arial", 16))
txtbox2.grid(row=1, column=1, padx=10)

result_frame = tk.Frame(win, bg="#070707")
result_frame.pack(pady=20)
tk.Label(result_frame, text="Result:", font=("Arial", 16), bg="#070707", fg="white").grid(row=0)
number_result = tk.Label(result_frame, text="__", font=("Arial", 16), bg="#070707", fg="white")
number_result.grid(row=0, column=1)

button_frame = tk.Frame(win, bg="#070707")
button_frame.pack(pady=20)
for op in ["+", "-", "x", "÷", "//", "^", "%"]:
    create_button(op, op)

win.mainloop()
