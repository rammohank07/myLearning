import tkinter


def main():
    w = tkinter.Tk()
    w.geometry("500x400")
    w.config(bg='light green')

    l1 = tkinter.Label(w, text="UserName", bg="yellow", font=("Arial", 15), fg="red")
    l2 = tkinter.Label(w, text="Password", bg="yellow", font=("Arial", 15), fg="red")
    l1.place(x=100, y=100)
    l2.place(x=100, y=150)

    e1 = tkinter.Entry(w, width=10, font=("Arial", 15), fg="blue")
    e2 = tkinter.Entry(w, width=10, font=("Arial", 15), fg="blue", show="$")
    e1.place(x=200, y=100)
    e2.place(x=200, y=150)

    def signin():
        username = e1.get()
        password = e2.get()
        print(f"Username: {username}, Password: {password}")  # placeholder for actual auth logic

    b1 = tkinter.Button(w, text="Signin", font=("Arial", 15), fg="red", command=signin)
    b1.place(x=150, y=200)

    w.mainloop()


main()
