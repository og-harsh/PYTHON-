import tkinter as tk

root = tk.Tk()
root.title("Radiobutton Example")
root.geometry("300x200")

choice = tk.IntVar()

tk.Label(root, text="Select your course").pack()

tk.Radiobutton(root, text="MCA",
               variable=choice, value=1).pack()

tk.Radiobutton(root, text="MBA",
               variable=choice, value=2).pack()

def show():
    print("Selected option:", choice.get())

tk.Button(root, text="Submit", command=show).pack()

root.mainloop()