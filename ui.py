import tkinter


class UserInterface:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.config(padx=20, pady=20)
        self.window.title("Pass Man GUI")

        self.canvas = tkinter.Canvas(width=200, height=200)
        self.canvas.grid(row=1, column=1)
        logo_image = tkinter.PhotoImage(file="logo.png")
        self.logo = self.canvas.create_image(100, 100, image=logo_image)

        self.window.mainloop()
