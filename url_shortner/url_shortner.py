from tkinter import *
from tkinter import messagebox
from datetime import datetime
import pyshorteners


class UrlShortner:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x200')
        self.root.maxsize(500, 200)
        self.root.minsize(500, 200)
        self.root.title('URL Shortener')
        self.root['bg'] = "white"

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):

        self.title = Label(self.root, text="URL Shortener", font=('verdana', 15, 'bold'), bg="white", fg="purple")
        self.title.place(x=180, y=5)
        self.date = Label(self.root, text=datetime.now().date(), fg="purple", font=('verdana', 10, 'bold'))
        self.date.place(x=400, y=5)


        Label(self.root, text="Paste Your URL Here ..", font=('verdana', 10, 'bold'), fg="purple").place(x=50, y=50)
        self.url = Entry(self.root, width=50, bg="lightgrey", relief=GROOVE, borderwidth=2, border=2)
        self.url.place(x=50, y=80)


        self.button = Button(self.root, relief=GROOVE, text="Create", font=('verdana', 8, 'bold'), bg="purple",
                             fg="white", command=self.create_short_url)
        self.button.place(x=360, y=78)


        self.output = Entry(self.root, font=('verdana', 10, 'bold'), fg="purple", width=30, relief=GROOVE,
                            borderwidth=2, border=2)
        self.output.place(x=80, y=120)

    def create_short_url(self):

        if self.url.get() == "":
            messagebox.showerror("Error", "Please Paste an URL")
        else:

            original_url = self.url.get()
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(original_url)


            self.output.delete(0, END)
            self.output.insert(END, short_url)


if __name__ == '__main__':
    UrlShortner()
