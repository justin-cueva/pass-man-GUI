import tkinter


class UserInterface:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.config(padx=20, pady=20)
        self.window.title("Pass Man GUI")

        # LOGO IMAGE
        self.canvas = tkinter.Canvas(width=200, height=200)
        self.canvas.grid(row=0, column=1)
        logo_image = tkinter.PhotoImage(file="logo.png")
        self.logo = self.canvas.create_image(100, 100, image=logo_image)

        # LABELS
        self.website_label = tkinter.Label(text="Website:")
        self.website_label.grid(row=1, column=0)
        self.email_username_label = tkinter.Label(text="Email/Username:")
        self.email_username_label.grid(row=2, column=0)
        self.password_label = tkinter.Label(text="Password:")
        self.password_label.grid(row=3, column=0)

        # INPUTS
        self.website_input = tkinter.Entry(width=35)
        self.website_input.grid(row=1, column=1, columnspan=2)
        self.email_username_input = tkinter.Entry(width=35)
        self.email_username_input.grid(row=2, column=1, columnspan=2)
        self.password_input = tkinter.Entry(width=21)
        self.password_input.grid(row=3, column=1, columnspan=1, sticky="ew")

        # BUTTONS

        self.window.mainloop()
