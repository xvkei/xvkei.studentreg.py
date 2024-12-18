import tkinter as tk
from functools import partial
root = tk.Tk()
root.title("Calculator")
root.geometry("500x600+400+100")
result_var = tk.StringVar(value="0")
tk.Label(root, textvariable=result_var, font=("Helvetica", 36), bd=15, bg="#CD5D67", fg="#410B13", anchor="e").grid(row=0, column=0, columnspan=4, sticky="nsew")
def on_button_click(char):
    if char == '=':
        try: result_var.set(eval(result_var.get().replace('x', '*').replace('÷', '/').replace('^', '**')))
        except: result_var.set("Error")
    elif char == 'C': result_var.set("0")
    else:
        current = result_var.get()
        result_var.set(char if current == "0" else current + char)
buttons = [('^', 1, 0), ('//', 1, 1), ('%', 1, 2), ('C', 1, 3), ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3), ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3), ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('x', 4, 3), ('.', 5, 0), ('0', 5, 1), ('=', 5, 2), ('÷', 5, 3)]
for (text, row, col) in buttons:
    tk.Button(root, text=text, font=("Helvetica", 24), width=5, height=2, bg="#410B13", fg="white", command=partial(on_button_click, text)).grid(row=row, column=col, sticky="nsew")
for i in range(4): root.grid_columnconfigure(i, weight=1); root.grid_rowconfigure(i + 1, weight=1)
root.mainloop()