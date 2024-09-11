import tkinter as tk

window = tk.Tk()

window.geometry("800x500")
window.title("My First GUI")

label = tk.Label(window, text="Hello World!", font=('Arial', 18))
label.pack()

window.mainloop()