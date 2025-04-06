import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import re

def submit_data():
    name = entry_name.get().strip()
    birthday = entry_birthday.get().strip()
    email = entry_email.get().strip()
    phone = entry_phone.get().strip()
    address = entry_address.get("1.0", tk.END).strip()
    contact_method = contact_var.get()

    if not (name and birthday and email and phone and address):
        messagebox.showwarning("Missing Info", "Please fill out all fields.")
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Invalid Email", "Enter a valid email address.")
        return

    conn = sqlite3.connect("customer_info.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO customers (name, birthday, email, phone, address, contact_method)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, birthday, email, phone, address, contact_method))
    conn.commit()
    conn.close()

    entry_name.delete(0, tk.END)
    entry_birthday.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete("1.0", tk.END)
    contact_var.set(contact_options[0])

    messagebox.showinfo("Success", "Customer info submitted successfully.")
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

tk.Button(root, text="Submit", command=submit_data, bg="green", fg="white").pack(pady=20)

root.mainloop()