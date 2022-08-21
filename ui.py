import tkinter


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
        self.website_input = tkinter.Entry(width=30)
        self.website_input.grid(row=1, column=1, columnspan=2, sticky="ew")
        self.email_username_input = tkinter.Entry(width=30)
        self.email_username_input.grid(row=2, column=1, columnspan=2, sticky="ew")
        self.password_input = tkinter.Entry()
        self.password_input.grid(row=3, column=1, columnspan=1, sticky="ew")

        # BUTTONS
        self.generate_password_button = tkinter.Button(text="Generate Password", font=("Arial", 12, "normal"))
        self.generate_password_button.grid(row=3, column=2, sticky="nesw")
        self.add_button = tkinter.Button(text="Add")
        self.add_button.grid(row=4, column=1, columnspan=2, sticky="nesw")

        self.window.mainloop()
