from BlockChainMember import *
from tkinter.ttk import Combobox
import PIL.Image
import PIL.ImageTk
import tkinter.messagebox
from tkinter import *
from BlockChainResults import *

from BlockChainMember import *
import tkinter
from tkinter.ttk import Combobox
import PIL.Image
import PIL.ImageTk
import tkinter.messagebox

from tkinter import *
from BlockChainMember import *
import tkinter
from tkinter.ttk import Combobox
import PIL.Image
import PIL.ImageTk
import tkinter.messagebox

from tkinter import *

from BlockChainResults import *
from BlockChainResults import *


class MainOBJ:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500")
        self.root.config(bg="white")
        self.root.title("BlockChain application ...")
        self.root.resizable(False, False)
        self.root.imge = PIL.Image.open('logo1.jpg')
        self.root.photo = PIL.ImageTk.PhotoImage(self.root.imge)
        self.root.lab = Label(self.root, image=self.root.photo)

        self.root.lab.place(x=530, y=20)
        # lab.pack()
        text_ = StringVar()
        text_.set(" Liste des Electeurs :")

        def action3():
            t = town.get()
            print(town.get())
            if town.get() == "Select a town":
                tkinter.messagebox.showinfo("Warning Message ", "please choose town ! ")
            else:
                if town.get() == "authority":

                    self.root.destroy()
                    tk1 = Tk()
                    from BlockChainResults.Total_Report import Total_ReportOBJ
                    Total_ReportOBJ(tk1, t)

                    tk1.mainloop()
                else:
                    self.root.destroy()
                    tk1 = Tk()
                    from BlockChainResults.Liste_Report import Liste_ReportOBJ
                    Liste_ReportOBJ(tk1, t)

                    tk1.mainloop()

        def action30():
            t = town.get()
            self.root.destroy()
            tk1 = Tk()
            from BlockChainResults.Results_Details1 import R_D1OBJ
            R_D1OBJ(tk1, t)

            tk1.mainloop()

        def action31():
            t = town.get()
            self.root.destroy()
            tk1 = Tk()

            from BlockChainResults.Results_Details2 import R_D2OBJ
            R_D2OBJ(tk1, t)

            tk1.mainloop()

        def action32():
            t = town.get()
            self.root.destroy()
            tk1 = Tk()

            from BlockChainResults.Results_Details3 import R_D3OBJ
            R_D3OBJ(tk1, t)

            tk1.mainloop()

        def action33():
            t = town.get()
            self.root.destroy()
            tk1 = Tk()

            from BlockChainResults.Results_Details4 import R_D4OBJ
            R_D4OBJ(tk1, t)

            tk1.mainloop()

        def action():
            t = town.get()
            print(town.get())
            if town.get() == "Select a town":
                tkinter.messagebox.showinfo("Warning Message ", "please choose town ! ")
            else:

                self.root.destroy()
                tk1 = Tk()
                val = "not validate"
                from BlockChainElector.Liste_Electeurs import Liste_ElecteursOBJ
                Liste_ElecteursOBJ(tk1, t)

                tk1.mainloop()

        def abt():
            tkinter.messagebox.showinfo("Welcome", "Menu Options")

        def action2():
            t = town.get()

            if town.get() == "Select a town":
                tkinter.messagebox.showinfo("Warning Message ", "please choose town ! ")
            else:
                self.root.destroy()
                tk1 = Tk()

                from BlockChainMember.Liste_Voting_Center_Member import Liste_Voting_Center_MemberOBJ
                Liste_Voting_Center_MemberOBJ(tk1, t)
                tk1.mainloop()

        n2 = Button(self.root, text="Liste des Electeurs", command=action, width=36, bg='green', fg='white', height=2,
                    font=("bold", 15))
        n2.place(x=80, y=80)

        n22 = Button(self.root, text="Liste des Bureaux", command=action2, width=36, bg='green', fg='white', height=2,
                     font=("bold", 15))
        n22.place(x=80, y=160)

        n222 = Button(self.root, text="Resultats de Vote", command=action3, width=36, bg='green', fg='white', height=2,
                      font=("bold", 15))
        n222.place(x=80, y=240)

        town_values = ["authority", "Oum El Bouaghi-ville", "Bir Kechba", "Mekhalfa", "Sedjra", "F'Kirina", "Ras F'Kirina",
                       "Laïoun",
                       "Merigueb", "Ras Medfoun", "Tagouft Kébira", "Tagouft Seghira", "Fid Meslou", "Village Sidi Ghriss", "Ali Ouidir",
                       "Bir Terch",
                       "Draa Laghbar", "Fid Souar", "Lahteb", "Laskria", "Aïn Seïd", "Bir Sahli", "Dahnoune",
                       "El Hamra",
                       "Lemoujah", "Stoh"]

        town = Combobox(self.root, values=town_values, font=("bold", 15))
        town.place(x=155, y=320)
        town.set("Select a town")

        self.root.menu = Menu(self.root)
        root.config(menu=self.root.menu)

        self.root.subm1 = Menu(self.root.menu)
        self.root.menu.add_cascade(label="Option", menu=self.root.subm1)
        self.root.subm1.add_command(label="Liste des Electeurs", command=action)
        self.root.subm1.add_command(label="Liste des Bureaux", command=action2)
        self.root.subm1.add_command(label="Resultats de Vote", command=action3)
        self.root.subm1.add_command(label="Resultats elctors", command=action30)
        self.root.subm1.add_command(label="Resultats centers", command=action31)
        self.root.subm1.add_command(label="Resultats reports", command=action32)
        self.root.subm1.add_command(label="Detail reports", command=action33)

        self.root.subm2 = Menu(self.root.menu)
        self.root.menu.add_cascade(label="Help", menu=self.root.subm2)
        self.root.subm2.add_command(label="About", command=abt)


if __name__ == '__main__':
    root = Tk()
    application = MainOBJ(root)

    root.mainloop()

# fen.mainloop()
