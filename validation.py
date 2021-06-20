import sqlite3


import tkinter.messagebox

import tkinter.messagebox

import tkinter
from tkinter.ttk import Combobox

import tkinter.messagebox

from tkinter import *


class ValOBJ:
    def __init__(self, root, town1):
        self.root = root
        self.town1 = town1
        self.root.geometry("500x300")
        self.root.config(bg="white")
        self.root.title("Validation ...")
        self.root.resizable(False, False)
        self.validate="not validated"

        def action():
            t = town.get()
            print(town.get())
            if town.get() == "Select a job":
                tkinter.messagebox.showinfo("Warning Message ", "please choose town ! ")
            else:
                # ///////////////////////
                conn = sqlite3.connect('Electors.db')
                c = conn.cursor()
                # //////////////////////////////////////////////
                c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users' ''')
                # ////////////////////////////////////////////////
                if c.fetchone()[0] == 1:
                    query = "SELECT * FROM users "
                    c.execute(query)
                    data = c.fetchall()
                    for row in data:
                        print(str(email1.get()))
                        print(str(row[1]))
                        print(str(password2.get()))
                        print(str(row[2]))
                        print(str(phone3.get()))
                        print(str(row[4]))
                        print(str(town.get()))
                        print(str(row[3]))

                        if row[1] == str(email1.get()) and row[2] == str(password2.get()) and row[3] == str(town.get()) and row[4] == str(phone3.get()):
                            self.validate = "validated"
                            tkinter.messagebox.showinfo("Welcome", "validation accepted")
                        else:
                            tkinter.messagebox.showinfo("Welcome", "validation wrong")
                    print('Table exists.')
                else:
                    print('Table does not exist.')

                conn.commit()
                conn.close()
                # //////////////////////

                self.root.destroy()
                tk1 = Tk()

                from BlockChainElector.Liste_Electeurs import Liste_ElecteursOBJ
                Liste_ElecteursOBJ(tk1, self.town1, self.validate)

                tk1.mainloop()

        def abt():
            tkinter.messagebox.showinfo("Welcome", "Menu Options")


        n2 = Button(self.root, text="Ok", command=action, width=20, bg='green', fg='white', height=2)
        n2.place(x=160, y=200)

        # //////////////////////////
        self.root.email = StringVar()
        self.root.email.set("email : ")
        self.root.lab2019 = Label(self.root, textvariable=self.root.email)
        self.root.lab2019.place(x=20, y=50)


        va1 = StringVar()
        email1 = Entry(self.root, textvariable=va1)
        email1.place(x=100, y=50)

        password = StringVar()
        password.set("password : ")
        lab2020 = Label(self.root, textvariable=password)
        lab2020.place(x=20, y=80)

        va2 = StringVar()
        password2 = Entry(self.root, textvariable=va2)
        password2.place(x=100, y=80)

        phone = StringVar()
        phone.set("phone : ")
        lab2021 = Label(self.root, textvariable=phone)
        lab2021.place(x=20, y=110)

        va3 = StringVar()
        phone3 = Entry(self.root, textvariable=va3)
        phone3.place(x=100, y=110)
        job = StringVar()
        job.set("job : ")
        lab2022 = Label(self.root, textvariable=job)
        lab2022.place(x=20, y=140)

        # ////////////////////////////
        town_values = ["President", "vice president", "Writer", "assistant 1", "assistant 2", "Extra 1", "Extra 2"]

        town = Combobox(self.root, values=town_values, font=("bold", 15))
        town.place(x=100, y=140)
        town.set("Select a job")

        self.root.menu = Menu(self.root)
        root.config(menu=self.root.menu)

        self.root.subm1 = Menu(self.root.menu)
        self.root.menu.add_cascade(label="Option", menu=self.root.subm1)
        self.root.subm1.add_command(label="Liste des Electeurs", command=action)

        self.root.subm2 = Menu(self.root.menu)
        self.root.menu.add_cascade(label="Help", menu=self.root.subm2)
        self.root.subm2.add_command(label="About", command=abt)


if __name__ == '__main__':
    root = Tk()
    t1 = "Oum El Bouaghi-ville"
    application = ValOBJ(root, t1)

    root.mainloop()

# fen.mainloop()
