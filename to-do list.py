import tkinter as tk
from tkinter import messagebox


class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()

    def delete_task(self):
        try:
            selection = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selection)
            del self.tasks[selection]
            self.save_tasks()
        except IndexError:
            messagebox.showinfo("Error", "No task selected")

    def update_task(self):
        try:
            selection = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task:
                self.task_listbox.delete(selection)
                self.task_listbox.insert(selection, new_task)
                self.tasks[selection] = new_task
                self.task_entry.delete(0, tk.END)
                self.save_tasks()
        except IndexError:
            messagebox.showinfo("Error", "No task selected")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")


def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
