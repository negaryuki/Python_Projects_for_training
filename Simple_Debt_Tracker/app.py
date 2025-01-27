import tkinter as tk
from tkinter import messagebox
import json

class DebtTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Debt Tracker App")
        
        # Initialize debt data
        self.debts = self.load_data()

        # UI elements
        self.create_ui()

    def create_ui(self):
        # Add name input
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Add amount input
        tk.Label(self.root, text="Amount:").grid(row=1, column=0, padx=10, pady=5)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=5)

        # Add add debt button
        self.add_button = tk.Button(self.root, text="Add Debt", command=self.add_debt)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Display debt list
        self.debt_list = tk.Listbox(self.root, width=50)
        self.debt_list.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Add delete button
        self.delete_button = tk.Button(self.root, text="Delete Selected Debt", command=self.delete_selected)
        self.delete_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.update_list()

    def add_debt(self):
        name = self.name_entry.get()
        try:
            amount = float(self.amount_entry.get())
            if not name:
                raise ValueError("Name cannot be empty.")

            self.debts.append({"name": name, "amount": amount})
            self.save_data()
            self.update_list()

            self.name_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def delete_selected(self):
        selected_index = self.debt_list.curselection()
        if selected_index:
            self.debts.pop(selected_index[0])
            self.save_data()
            self.update_list()
        else:
            messagebox.showwarning("Warning", "No item selected to delete.")

    def update_list(self):
        self.debt_list.delete(0, tk.END)
        for debt in self.debts:
            self.debt_list.insert(tk.END, f"{debt['name']} - ${debt['amount']:.2f}")

    def load_data(self):
        try:
            with open("debts.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        with open("debts.json", "w") as file:
            json.dump(self.debts, file, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = DebtTrackerApp(root)
    root.mainloop()
