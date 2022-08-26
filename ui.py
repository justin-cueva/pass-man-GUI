import random
import tkinter
from tkinter import messagebox
import pyperclip
import json


class UserInterface:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.config(padx=50, pady=50)
        self.window.title("Pass Man GUI")

        # LOGO IMAGE
        self.canvas = tkinter.Canvas(width=200, height=200)
        self.canvas.grid(row=0, column=1)
        logo_image = tkinter.PhotoImage(file="logo.png")
        self.logo = self.canvas.create_image(100, 100, image=logo_image)

        # LABELS
        label_width = 15
        self.website_label = tkinter.Label(text="Website:", width=label_width)
        self.website_label.grid(row=1, column=0)
        self.email_username_label = tkinter.Label(text="Email/Username:", width=label_width)
        self.email_username_label.grid(row=2, column=0)
        self.password_label = tkinter.Label(text="Password:", width=label_width)
        self.password_label.grid(row=3, column=0)

        # INPUTS
        self.website_input = tkinter.Entry()
        self.website_input.focus_set()
        self.website_input.grid(row=1, column=1, columnspan=2, sticky="ew")
        self.email_username_input = tkinter.Entry(width=30)
        self.email_username_input.insert(0, "justincueva02@gmail.com")
        self.email_username_input.grid(row=2, column=1, columnspan=2, sticky="ew")
        self.password_input = tkinter.Entry()
        self.password_input.grid(row=3, column=1, columnspan=1, sticky="ew")

        # BUTTONS
        self.generate_password_button = tkinter.Button(text="Generate Password", command=self.generate_password,
                                                       font=("Arial", 12, "normal"))
        self.generate_password_button.grid(row=3, column=2, sticky="nesw")
        self.add_button = tkinter.Button(text="Add", command=self.save)
        self.add_button.grid(row=4, column=1, columnspan=2, sticky="nesw")
        self.search_button =tkinter.Button(text="Search", command=self.search_passwords)
        self.search_button.grid(row=1, column=2, sticky="ew")

        self.window.mainloop()

    def search_passwords(self):
        searched = self.website_input.get()
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                try:
                    email_searched = data[f"{searched}"]["email"]
                    pas_searched = data[f"{searched}"]["password"]
                except KeyError:
                    messagebox.showinfo(title="Oops", message=f"we have no data for the website: {searched}")
                else:
                    messagebox.showinfo(title=searched, message=f"email: {email_searched}\n"
                                                                f"password: {pas_searched}")
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message=f"we have no data for the website: {searched}")

    def generate_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = []

        for char in range(nr_letters):
            password_list.append(random.choice(letters))

        for char in range(nr_symbols):
            password_list += random.choice(symbols)

        for char in range(nr_numbers):
            password_list += random.choice(numbers)

        random.shuffle(password_list)

        password = ""
        for char in password_list:
            password += char

        pyperclip.copy(password)
        self.password_input.delete(0, tkinter.END)
        self.password_input.insert(0, password)

    def save(self):
        website = self.website_input.get()
        email = self.email_username_input.get()
        password = self.password_input.get()

        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        if len(website) == 0 or len(password) == 0 or len(email) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure that you haven't left any fields empty")
        else:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as new_data_file:
                    # Creating new data file
                    json.dump(new_data, new_data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                self.website_input.delete(0, tkinter.END)
                self.password_input.delete(0, tkinter.END)
