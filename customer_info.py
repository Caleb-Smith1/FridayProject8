import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Customer Information Form")
root.geometry("400x500")

tk.Label(root, text="Name").pack(pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.pack()

tk.Label(root, text="Birthday (YYYY-MM-DD)").pack(pady=5)
entry_birthday = tk.Entry(root, width=40)
entry_birthday.pack()

tk.Label(root, text="Email").pack(pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.pack()

tk.Label(root, text="Phone").pack(pady=5)
entry_phone = tk.Entry(root, width=40)
entry_phone.pack()

tk.Label(root, text="Address").pack(pady=5)
entry_address = tk.Text(root, width=30, height=4)
entry_address.pack()

tk.Label(root, text="Preferred Contact Method").pack(pady=5)
contact_options = ["Email", "Phone", "Mail"]
contact_var = tk.StringVar(value=contact_options[0])
dropdown = ttk.Combobox(root, textvariable=contact_var, values=contact_options, state="readonly")
dropdown.pack()

root.mainloop()