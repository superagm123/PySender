import tkinter as tk
from Frames import EmailFrame
from Styles import Styles


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('PySender')
        self.geometry('1200x950')
        self.minsize(800, 950)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        Styles()

        email_frame = EmailFrame(self)
        email_frame.grid(row=0, column=0, sticky='NSEW')


if __name__ == '__main__':
    app = App()
    app.mainloop()