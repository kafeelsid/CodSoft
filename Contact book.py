import tkinter as tk
from tkinter import messagebox
import sqlite3

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book App")
        
        self.conn = sqlite3.connect("contacts.db")
        self.c = self.conn.cursor()
        self.create_table()

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(master, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(master, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(master, width=30)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.search_label = tk.Label(master, text="Search:")
        self.search_label.grid(row=6, column=0, padx=10, pady=5)
        self.search_entry = tk.Entry(master, width=20)
        self.search_entry.grid(row=6, column=1, padx=10, pady=5)
        self.search_button = tk.Button(master, text="Search", command=self.search_contact)
        self.search_button.grid(row=6, column=2, padx=5, pady=5)

        self.contact_listbox = tk.Listbox(master, width=50)
        self.contact_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            phone TEXT NOT NULL,
                            email TEXT,
                            address TEXT
                          )''')
        self.conn.commit()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            self.c.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                           (name, phone, email, address))
            self.conn.commit()
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone number are required.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        self.c.execute("SELECT name, phone FROM contacts")
        contacts = self.c.fetchall()
        for contact in contacts:
            self.contact_listbox.insert(tk.END, f"{contact[0]} - {contact[1]}")

    def search_contact(self):
        search_term = self.search_entry.get()
        self.contact_listbox.delete(0, tk.END)
        self.c.execute("SELECT name, phone FROM contacts WHERE name LIKE ? OR phone LIKE ?",
                       ('%' + search_term + '%', '%' + search_term + '%'))
        contacts = self.c.fetchall()
        for contact in contacts:
            self.contact_listbox.insert(tk.END, f"{contact[0]} - {contact[1]}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
