from cProfile import label
from cgitb import text
from faulthandler import disable
from logging import PlaceHolder, root
from sqlite3 import Row
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from math import e, pi
from tkinter import *
from tkinter import ttk
from abc import ABCMeta
from abc import ABCMeta,abstractmethod
from datetime import datetime
import email
from hashlib import new
from mimetypes import init
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
class Voiture():
    def __init__(self,immat,marque,cerburant,model,puis):
        self._immat=immat
        self._marque=marque
        self._cerburant=cerburant
        self._model=model
        self._puis=puis
    @property
    def immat(self):
        return self._immat
    @immat.setter
    def immat(self,new):
        self._immat=new
    @property
    def marque(self):
        return self._marque
    @marque.setter
    def marque(self,new):
        self._marque=new
    @property
    def cerburant(self):
        return self._cerburant
    @cerburant.setter
    def cerburant(self,new):
        self._cerburant=new
    @property
    def model(self):
        return self._model
    @model.setter
    def model(self,new):
        self._model=new
    @property
    def puis(self):
        return self._puis
    @puis.setter
    def puis(self,new):
        self._puis=new
    def __str__(self) -> str:
        return f"{self.immat},{self.marque},{self.cerburant},{self.puis}"
class VoitureVip(Voiture):
    def __init__(self, immat, marque, cerburant, model, puis,type):
        super().__init__(immat, marque, cerburant, model, puis)
        self.__type=type
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,new):
        self.__type=new
    def __str__(self) -> str:
        return f"{super().__str__()},{self.type}"
class VoitureCitadinne(Voiture):
    def __init__(self, immat, marque, cerburant, model, puis,gamme):
        super().__init__(immat, marque, cerburant, model, puis)
        self.__gamme=gamme
    @property
    def gamme(self):
        return self.__gamme
    @gamme.setter
    def gamme(self,new):
        self.__gamme=new
    def __str__(self) -> str:
        return f"{super().__str__()},{self.gamme}"
class ListVoiture:
    def __init__(self,list):
        self.__list=list
    @property
    def list(self):
        return self.__list
    @list.setter
    def list(self,new):
        self.__list=new
    def ajou(self,obj):
        self.list.append(obj)
    def suppr(self,immat):
        self.list.remove(immat)
    def mod(self,immat,newimmat,newmark,newcar,newmod,newpuis,newtype):
        for i in self.list:
            if i.immat==immat:
                i.immat(newimmat)
                i.marque(newmark)
                i.cerburant(newcar)
                i.model(newmod)
                i.puis(newpuis)
                if isinstance(i, VoitureCitadinne):
                    i.gamme(newtype)
                if isinstance(i,VoitureVip):
                    i.type(newtype)
class personne:
    def __init__(self,cin,nom,pre):
        self.__cin=cin
        self.__nom=nom
        self.__pre=pre
    @property
    def cin(self):
        return self.__cin
    @cin.setter
    def cin(self,new):
        self.__cin=new
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,new):
        self.__nom=new
    @property
    def pre(self):
        return self.__pre
    @pre.setter
    def pre(self,new):
        self.__pre=new
    def __str__(self):
        return f"{self.cin},{self.nom},{self.pre}"
class Client(personne):
    def __init__(self,cin,nom,prenom,numpermis,tele):
        super().__init__(cin, nom, prenom)
        self._numpermis=numpermis
        self._tele=tele   
    @property
    def numpermis(self):
        return self._numpermis
    @numpermis.setter
    def numpermis(self,new):
        self._numpermis=new
    @property
    def tele(self):
        return self._tele
    @tele.setter
    def tele(self,new):
        self._tele=new
        pass
    def __str__(self) -> str:
        return f"{super().__str__()},{self.numpermis},{self.tele}"
class Listclt:
    def __init__(self,list):
        self.__list=list
    @property
    def list(self):
        return self.__list
    @list.setter
    def list(self,new):
        self.__list=new
    def ajou(self,obj):
        self.list.append(obj)
    def suppr(self,cin):
        self.list.remove(cin)
    def mod(self,cin,newcin,newnom,newprenom,newtele,newnump):
        for i in self.list:
            if i.cin==cin:
                i.cin(newcin)
                i.nom(newnom)
                i.prenom(newprenom)
                i.tele(newtele)
                i.numpermis(newnump)
class Location():
    auto=0
    def __init__(self,duree,prix,clt,voitur):
        self.__duree=duree
        self.__prix=prix
        self.__clt=clt
        self.__voitur=voitur
        self.__date=datetime.today()
        self.__idloca=Location.auto
        Location.auto+=1
    @property
    def duree(self):
        return self.__duree
    @duree.setter
    def duree(self,new):
        self.__duree=new
    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self,new):
        self.__prix=new
    @property
    def clt(self):
        return self.__clt
    @clt.setter
    def clt(self,new):
        self.__clt=new
    @property
    def voitur(self):
        return self.__voitur
    @voitur.setter
    def voitur(self,new):
        self.__voitur=new
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self,new):
        self.__date=new
    @property
    def idloca(self):
        return self.__idloca
    @idloca.setter
    def idloca(self,new):
        self.__idloca=new
    def __str__(self):
        return f"{self.idloca},{self.clt},{self.date},{self.duree},{self.prix},{self.voitur}"
class Utilisateur:
    def __init__(self,login,mdps,email):
        self.__login=login
        self.__mdps=mdps
        self.__email=email
    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self,new):
        self.__login=new
    @property
    def mdps(self):
        return self.__mdps
    @mdps.setter
    def mdps(self,new):
        self.__mdps=new
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,new):
        self.__email=new
    def __str__(self):
        return f"{self.login},{self.mdps},{self.email}"
class ListeUtilisateurs:
    def __init__(self,list):
        self.__list=list
    @property
    def list(self):
        return self.__list
    @list.setter
    def list(self,new):
        self.__list=new
    def autont(self,login,mdps):
        nb=0
        for i in self.list:
            if i.login==login and i.mdps==mdps:
                return True
        else:return False
    def ajou(self,obj):
        self.list.append(obj)
    def supp(self,login):
        for i in self.list:
            if i.login==login:
                self.list.remove(i)
    def mod(self,login,newlogin,newmdps,newemail):
        for i in self.list:
            if i.login==login:
                i.login(newlogin)
                i.mdps(newmdps)
                i.email(newemail)
                break
    def __str__(self) :
        nb=""
        for i in self.list:
            print(i)
class ListeLocations:
    def __init__(self,list):
        self.__list=list
    @property
    def list(self):
        return self.__list
    @list.setter
    def list(self,new):
        self.__list=new
    def AfficherListeLocation(self):
        for i in self.list:
            print(i)
    def AfficherListeLocationCitadine(self):
         for i in self.list:
            if i.voitur.isinstance(VoitureCitadinne):
                print(i)
    def AfficherListeLocationVip(self):
         for i in self.list:
            if i.voitur.isinstance(VoitureVip):
                print(i)
    def AfficherLocationMarque(self,marque):
         for i in self.list:
             i.voitur.marque==marque
             print(i)
    def AfficherLocationImma(self,immat):
        for i in self.list:
             i.voitur.immat==immat
             print(i)
    def AfficherLocationClient(self,cin):
        for i in self.list:
             i.clt.cin==cin
             print(i)
    def AjouterLocation(self,obj):
        self.list.append(obj)
    def SupprimerLocation(self,obj):
        for i in self.list:
            if i==obj:
                self.list.remove(i)
    def FiltrerLocationDate(self,datte):
         for i in self.list:
             i.date==datetime.date(datte)
             print(i)
l=[]
util1=Utilisateur("nourddine","123456","soso@gmail.com")
util2=Utilisateur("hayat","123456","nono@gmail.com")
util3=Utilisateur("ayoub","123123","toto@gmail.com")
util4=Utilisateur("iliass","123123","popo@gmail.com")
util5=Utilisateur("moad","123123","hoho@gmail.com")
l.append(util1)
l.append(util2)
l.append(util3)
l.append(util4)
l.append(util5)
listo=ListeUtilisateurs(l)
lclt=[]
clt1=Client("LE1234","nourddine","benyahya",10099,"+212607081298")
clt2=Client("FD7895","aziz","rgrogi",12346,"+212607081298")
clt3=Client("VF1687","khalid","ahmadi",81375,"+212607081298")
clt4=Client("WE8181","moussa","akrami",51544,"+212607081298")
clt5=Client("GB9781","ibrahim","alawi",25455,"+212607081298")
clt6=Client("WF6728","otman","benkhalid",79826,"+212607081298")
lclt.append(clt1)
lclt.append(clt2)
lclt.append(clt3)
lclt.append(clt4)
lclt.append(clt5)
lclt.append(clt6)
listclt1=Listclt(lclt)
lvt=[]
vtr1=VoitureCitadinne("123456","DACIA","binzin","2009","500","A")
vtr2=VoitureCitadinne("789241","KONGO","mazout","2008","250","B")
vtr3=VoitureCitadinne("328429","JIP","lisans","2010","500","C")
vtr4=VoitureVip("644865","DACIA","binzin","2009","500","4*4")
vtr5=VoitureVip("995856","KONGO","mazout","2008","250","minibus")
vtr6=VoitureVip("687898","JIP","lisans","2010","500","SUV")
vtr7=VoitureVip("168478","JIP","lisans","2022","100","limousine")
lvt.append(vtr1)
lvt.append(vtr2)
lvt.append(vtr3)
lvt.append(vtr4)
lvt.append(vtr5)
lvt.append(vtr6)
lvt.append(vtr7)
listvtr=ListVoiture(lvt)
ll=[]
lo1=Location("5 jours","2500dh",clt1,vtr1)
lo2=Location("2 jours","3000dh",clt2,vtr2)
lo3=Location("5 jours","2500dh",clt3,vtr3)
lo4=Location("2 jours","3000dh",clt4,vtr4)
lo5=Location("5 jours","2500dh",clt5,vtr5)
lo6=Location("2 jours","3000dh",clt6,vtr6)
ll.append(lo1)
ll.append(lo2)
ll.append(lo3)
ll.append(lo4)
ll.append(lo5)
ll.append(lo6)
listloc=ListeLocations(ll)
mains=Tk()
mains.geometry('500x400+0+0')
mains.title("login")
mains.configure(bg='#262626')
mains.resizable(0,0)
label_titl=Label(mains,text="page login",fg='white',bg='#262626')
label_titl.config(font=('Comic Sans MS',20))
label_titl.place(x=180, y=40)
label_login=Label(mains,text="login",fg='white',bg='#262626')
label_login.config(font=('Comic Sans MS',15))
label_login.place(x=80, y=120)
label_password=Label(mains,text="password",fg='white',bg='#262626')
label_password.config(font=('Comic Sans MS',15))
label_password.place(x=80, y=180)
login_box=Entry(mains,width=35)
login_box.place(x=200,y=130)
password_box=Entry(mains,width=35,show="*")
password_box.place(x=200,y=188)
def logins():
    nbl=0
    for i in l:
        if login_box.get()==i.login and password_box.get()==i.mdps :
            nbl+=1
    if nbl==0:
        messagebox.showerror("Les informations sont incorrectes","Les informations sont incorrectes")
    else :
        if messagebox.showinfo("welcom",f"welcom {login_box.get()}"):
            w= Toplevel(mains)
            mains.withdraw()
            def openwin():
                root = Toplevel(w)
                root.geometry("650x720-1+0")
                root.configure(bg='#262626')
                root.title("Gestion Utilisateur")
                # Add some style
                style = ttk.Style()
                #Pick a theme
                style.theme_use("default")
                # Configure our treeview colors
                style.configure("Treeview", 
                    background="#D3D3D3",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#D3D3D3"
                    )
                # Change selected color
                style.map('Treeview', 
                    background=[('selected', 'blue')])
                # Create Treeview Frame
                tree_frame = Frame(root)
                tree_frame.pack(pady=20)
                # Treeview Scrollbar
                tree_scroll = Scrollbar(tree_frame)
                tree_scroll.pack(side=RIGHT, fill=Y)
                # Create Treeview
                my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
                # Pack to the screen
                my_tree.pack()
                #Configure the scrollbar
                tree_scroll.config(command=my_tree.yview)
                # Define Our Columns
                my_tree['columns'] = ("Login", "password", "email")
                # Formate Our Columns
                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("Login", anchor=W, width=200)
                my_tree.column("password", anchor=CENTER, width=200)
                my_tree.column("email", anchor=W, width=200)
                # Create Headings 
                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("Login", text="Login", anchor=W)
                my_tree.heading("password", text="password", anchor=CENTER)
                my_tree.heading("email", text="email", anchor=W)
                # Add Data
                data=[]
                for i in l:
                    vd=[i.login,i.mdps,i.email]
                    data.append(vd)
                # Create striped row tags
                my_tree.tag_configure('oddrow', background="white")
                my_tree.tag_configure('evenrow', background="lightblue")
                global count
                count=0
                for record in data:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))
                    count += 1
                # add child
                #my_tree.insert(parent='', index='end', iid=6, text="Child", values=("Steve", "1.2", "Peppers"))
                #my_tree.move('6', '0', '0')
                add_frame = Frame(root)
                add_frame.pack(pady=20)
                #Labels
                nl = Label(add_frame, text="Login")
                nl.grid(row=0, column=0)
                il = Label(add_frame, text="password")
                il.grid(row=0, column=1)
                tl = Label(add_frame, text="email")
                tl.grid(row=0, column=2)
                #Entry boxes
                Login_box = Entry(add_frame)
                Login_box.grid(row=1, column=0)
                password_box = Entry(add_frame)
                password_box.grid(row=1, column=1)
                email_box = Entry(add_frame)
                email_box.grid(row=1, column=2)
                # Add Record
                def add_record():
                    my_tree.tag_configure('oddrow', background="white")
                    my_tree.tag_configure('evenrow', background="lightblue")
                    if Login_box.get()!="" and password_box.get()!="" and email_box.get()!="":
                        nb=0
                        for i in data:
                            if i[0]==Login_box.get():
                                nb=1
                                break
                        if nb==1:
                            messagebox.showerror("error","Utilisateur deja exist")
                        else:
                            obj=Utilisateur(Login_box.get(),password_box.get(),email_box.get())
                            l.append(obj)
                            data.append([Login_box.get(),password_box.get(),email_box.get()])
                            global count
                            if count % 2 == 0:
                                my_tree.insert(parent='', index='end', iid=count, text="", values=(Login_box.get(), password_box.get(), email_box.get()), tags=('evenrow',))
                            else:
                                my_tree.insert(parent='', index='end', iid=count, text="", values=(Login_box.get(), password_box.get(), email_box.get()), tags=('oddrow',))
                            count += 1
                             # Clear the boxes
                            Login_box.delete(0, END)
                            password_box.delete(0, END)
                            email_box.delete(0, END)
                    else:messagebox.showerror("error","entrez toutes les information")
                # Remove all records
                def remove_all():
                    for record in my_tree.get_children():
                        my_tree.delete(record)
                    l.clear()
                    Login_box.delete(0, END)
                    password_box.delete(0, END)
                    email_box.delete(0, END)
                # Remove one selected
                def remove_one():
                    try:
                        x = my_tree.selection()[0]
                        values = my_tree.item(x, 'values')
                        for i in data:
                            if i[0]==values[0]:
                                data.remove(i)
                        for i in l:
                            if i.login==values[0]:
                                l.remove(i)
                        my_tree.delete(x)
                        Login_box.delete(0, END)
                        password_box.delete(0, END)
                        email_box.delete(0, END)
                    except:
                        messagebox.showerror("error","pleas select Utilisateur")
                # Select Record
                def select_record():
                    # Clear entry boxes
                    Login_box.delete(0, END)
                    password_box.delete(0, END)
                    email_box.delete(0, END)
                    # Grab record number
                    selected = my_tree.focus()
                    # Grab record values
                    values = my_tree.item(selected, 'values')
                    #temp_label.config(text=values[0])
                    # output to entry boxes
                    Login_box.insert(0, values[0])
                    password_box.insert(0, values[1])
                    email_box.insert(0, values[2])
                # Save updated record
                def update_record():
                    try:
                        # Grab record number
                        selected = my_tree.focus()
                        values = my_tree.item(selected, 'values')
                        # Save new data
                        if Login_box.get()!="" and password_box.get()!="" and email_box.get()!="":
                            nb=0
                            for i in data:
                                if i[0]==Login_box.get() and values[0]!=Login_box.get():
                                    nb=1
                                    break
                            if nb==1:
                                messagebox.showerror("error","Utilisateur deja exist")
                            else:
                                for i in l:
                                    if i.login==values[0]:
                                        i.login=Login_box.get()
                                        i.mdps=password_box.get()
                                        i.email=email_box.get()
                                for i in data:
                                    if i[0]==values[0]:
                                        i[0]=Login_box.get()
                                        i[1]=password_box.get()
                                        i[2]=email_box.get()
                                my_tree.item(selected, text="", values=(Login_box.get(), password_box.get(), email_box.get()))
                                # Clear entry boxes
                                Login_box.delete(0, END)
                                password_box.delete(0, END)
                                email_box.delete(0, END)
                        else:messagebox.showerror("error","entrez toutes les information")
                    except:
                        messagebox.showerror("error","pleas select Utilisateur")
                # Create Binding Click function
                def clicker(e):
                    try:
                        select_record()
                    except:
                        None
                # Move Row up
                def up():
                    rows = my_tree.selection()
                    for row in rows:
                        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)
                # Move Row Down
                def down():
                    rows = my_tree.selection()
                    for row in reversed(rows):
                        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)
                #Buttons
                move_up = Button(root, text="Move Up", command=up,width=100,activeforeground='#00EAD4',activebackground='#262626')
                move_up.pack(pady=10)
                move_up['background'] = "#00EAD4" 
                move_up['foreground']= '#262626'  #000d33
                move_up.config(font=('Comic Sans MS',10))
                move_down = Button(root, text="Move Down", command=down,width=100,activeforeground='#00EAD4',activebackground='#262626')
                move_down.pack(pady=10)
                move_down['background'] = "#00EAD4" 
                move_down['foreground']= '#262626'  #000d33
                move_down.config(font=('Comic Sans MS',10))
                update_button = Button(root, text="modifier Utilisateur selected", command=update_record,width=100,activeforeground='#00EAD4',activebackground='#262626')
                update_button.pack(pady=10)
                update_button['background'] = "#00EAD4" 
                update_button['foreground']= '#262626'  #000d33
                update_button.config(font=('Comic Sans MS',10))
                add_record = Button(root, text="Ajouter Utilisateur" ,command=add_record,width=100,activeforeground='#00EAD4',activebackground='#262626')
                add_record['background'] = "#00EAD4" 
                add_record['foreground']= '#262626'  #000d33
                add_record.config(font=('Comic Sans MS',10))
                add_record.pack(pady=10)
                # Remove One
                remove_one = Button(root, text=" supprimer Utilisateur Selected",activeforeground='#00EAD4',activebackground='#262626', command=remove_one,width=100)
                remove_one.pack(pady=10)
                remove_one['background'] = "#00EAD4" 
                remove_one['foreground']= '#262626'  #000d33
                remove_one.config(font=('Comic Sans MS',10))
                # Remove all
                remove_all = Button(root, text="supprimer tout Utilisateur",width=100, command=remove_all,activeforeground='#00EAD4',activebackground='#262626')
                remove_all.pack(pady=10)
                remove_all['background'] = "#00EAD4" 
                remove_all['foreground']= '#262626'  #000d33
                remove_all.config(font=('Comic Sans MS',10))
                # Bindings
                #my_tree.bind("<Double-1>", clicker)
                my_tree.bind("<ButtonRelease-1>", clicker)
            def openwinclt():
                root = Toplevel(w)
                root.geometry("1000x720+0+0")
                root.configure(bg='#262626')
                root.title("Gestion Client")
                # Add some style
                style = ttk.Style()
                #Pick a theme
                style.theme_use("default")
                # Configure our treeview colors
                style.configure("Treeview", 
                    background="#D3D3D3",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#D3D3D3")
                # Change selected color
                style.map('Treeview', 
                    background=[('selected', 'blue')])
                # Create Treeview Frame
                tree_frame = Frame(root)
                tree_frame.pack(pady=20)
                # Treeview Scrollbar
                tree_scroll = Scrollbar(tree_frame)
                tree_scroll.pack(side=RIGHT, fill=Y)
                # Create Treeview
                my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
                # Pack to the screen
                my_tree.pack()
                #Configure the scrollbar
                tree_scroll.config(command=my_tree.yview)
                # Define Our Columns
                my_tree['columns'] = ("CIN", "nom", "prenom","NumPermis","tele ")
                # Formate Our Columns
                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("CIN", anchor=W, width=172)
                my_tree.column("nom", anchor=CENTER, width=172)
                my_tree.column("prenom", anchor=W, width=172)
                my_tree.column("NumPermis", anchor=W, width=172)
                my_tree.column("tele ", anchor=W, width=172)
                # Create Headings 
                my_tree.heading("#0", text="", anchor=W)
                my_tree.heading("CIN", text="CIN", anchor=W)
                my_tree.heading("nom", text="nom", anchor=CENTER)
                my_tree.heading("prenom", text="prenom", anchor=W)
                my_tree.heading("NumPermis", text="NumPermis", anchor=W)
                my_tree.heading("tele ", text="tele ", anchor=W)
                # Add Data
                data = []
                for i in lclt:
                    listr=[i.cin,i.nom,i.pre,i.numpermis,i.tele]
                    data.append(listr)
                # Create striped row tags
                my_tree.tag_configure('oddrow', background="white")
                my_tree.tag_configure('evenrow', background="lightblue")
                global count
                count=0
                for record in data:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2] ,record[3],record[4]), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],record[3],record[4]), tags=('oddrow',))
                    count += 1
                # add child
                #my_tree.insert(parent='', index='end', iid=6, text="Child", values=("Steve", "1.2", "Peppers"))
                #my_tree.move('6', '0', '0')
                add_frame = Frame(root)
                add_frame.pack(pady=20)
                #Labels
                nl = Label(add_frame, text="CIN")
                nl.grid(row=0, column=0)
                il = Label(add_frame, text="nom")
                il.grid(row=0, column=1)
                tl = Label(add_frame, text="prenom")
                tl.grid(row=0, column=2)
                ol = Label(add_frame, text="NumPermis")
                ol.grid(row=0, column=3)
                po=Label(add_frame, text="tele ")
                po.grid(row=0, column=4)
                #Entry boxes
                CIN_box = Entry(add_frame)
                CIN_box.grid(row=1, column=0)
                nom_box = Entry(add_frame)
                nom_box.grid(row=1, column=1)
                prenom_box = Entry(add_frame)
                prenom_box.grid(row=1, column=2)
                NumPermis_box = Entry(add_frame)
                NumPermis_box.grid(row=1, column=3)
                tele_box= Entry(add_frame)
                tele_box.grid(row=1,column=4)
                # Add Record
                def add_record():
                    my_tree.tag_configure('oddrow', background="white")
                    my_tree.tag_configure('evenrow', background="lightblue")
                    global count
                    if CIN_box.get()!="" and nom_box.get()!="" and prenom_box.get()!="" and NumPermis_box.get()!="" and tele_box.get()!="":
                        nb=0
                        for i in data:
                            if i[0]==CIN_box.get():
                                nb=1
                                break
                        if nb==1:
                            messagebox.showerror("error","Client deja exist")
                        else:
                            obj=Client(CIN_box.get(),nom_box.get(),prenom_box.get(),NumPermis_box.get(),tele_box.get())
                            lclt.append(obj)
                            data.append([CIN_box.get(), nom_box.get(), prenom_box.get() ,NumPermis_box.get(),tele_box.get()])
                            if count % 2 == 0:
                                my_tree.insert(parent='', index='end', iid=count, text="", values=(CIN_box.get(), nom_box.get(), prenom_box.get() ,NumPermis_box.get(),tele_box.get() ), tags=('evenrow',))
                            else:
                                my_tree.insert(parent='', index='end', iid=count, text="", values=(CIN_box.get(), nom_box.get(), prenom_box.get(),NumPermis_box.get(), tele_box.get()), tags=('oddrow',))
                            count += 1
                            # Clear the boxes
                            CIN_box.delete(0, END)
                            nom_box.delete(0, END)
                            prenom_box.delete(0, END)
                            NumPermis_box.delete(0,END)
                            tele_box.delete(0,END)
                    else:messagebox.showerror("error","entrez toutes les information")
                    
                # Remove all records
                def remove_all():
                    for record in my_tree.get_children():
                        my_tree.delete(record)
                    lclt.clear()
                # Remove one selected
                def remove_one():
                    try:
                        x = my_tree.selection()[0]
                        values = my_tree.item(x, 'values')
                        for i in data:
                            if i[0]==values[0]:
                                data.remove(i)
                        for i in lclt:
                            if i.cin==values[0]:
                                lclt.remove(i)
                        my_tree.delete(x)
                        CIN_box.delete(0, END)
                        nom_box.delete(0, END)
                        prenom_box.delete(0, END)
                        NumPermis_box.delete(0,END)
                        tele_box.delete(0 ,END)
                    except:
                        messagebox.showerror("error","pleas select client")
                # Select Record
                def select_record():
                    # Clear entry boxes
                    CIN_box.delete(0, END)
                    nom_box.delete(0, END)
                    prenom_box.delete(0, END)
                    NumPermis_box.delete(0,END)
                    tele_box.delete(0 ,END)
                    # Grab record number
                    selected = my_tree.focus()
                    # Grab record values
                    values = my_tree.item(selected, 'values')
                    #temp_label.config(text=values[0])
                    # output to entry boxes
                    CIN_box.insert(0, values[0])
                    nom_box.insert(0, values[1])
                    prenom_box.insert(0, values[2])
                    NumPermis_box.insert(0, values[3])
                    tele_box.insert(0, values[4])
                # Save updated record
                def update_record():
                    try:
                        # Grab record number
                        selected = my_tree.focus()
                        values = my_tree.item(selected, 'values')
                        # Save new data
                        if CIN_box.get()!="" and nom_box.get()!="" and prenom_box.get()!="" and NumPermis_box.get()!="" and tele_box.get()!="":
                            nb=0
                            for i in data:
                                if i[0]==CIN_box.get() and values[0]!=CIN_box.get():
                                    nb=1
                                    break
                            if nb==1:
                                messagebox.showerror("error","Client deja exist")
                            else:
                                for i in data:
                                    if i[0]==values[0]:
                                        i[0]=CIN_box.get()
                                        i[1]=nom_box.get()
                                        i[2]=prenom_box.get()
                                        i[3]=NumPermis_box.get()
                                        i[4]=tele_box.get()
                                for i in lclt:
                                    if i.cin==values[0]:
                                        i.cin=CIN_box.get()
                                        i.nom=nom_box.get()
                                        i.pre=prenom_box.get()
                                        i.numpermis=NumPermis_box.get()
                                        i.tele=tele_box.get()
                                my_tree.item(selected, text="", values=(CIN_box.get(), nom_box.get(), prenom_box.get() ,NumPermis_box.get(),tele_box.get()))
                                # Clear entry boxes
                                CIN_box.delete(0, END)
                                nom_box.delete(0, END)
                                prenom_box.delete(0, END)
                                NumPermis_box.delete(0,END)
                                tele_box.delete(0,END)
                        else:messagebox.showerror("error","entrez toutes les information")
                        
                    # Create Binding Click function
                    except:
                        messagebox.showerror("error","pleas select client")
                def clicker(e):
                    try:
                        select_record()
                    except:
                        None
                # Move Row up
                def up():
                    rows = my_tree.selection()
                    for row in rows:
                        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)
                # Move Row Down
                def down():
                    rows = my_tree.selection()
                    for row in reversed(rows):
                        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)
                #Buttons
                move_up = Button(root, text="Move Up", command=up,width=100,activeforeground='#00EAD4',activebackground='#262626')
                move_up.pack(pady=10)
                move_up['background'] = "#00EAD4" 
                move_up['foreground']= '#262626'  #000d33
                move_up.config(font=('Comic Sans MS',10))
                move_down = Button(root, text="Move Down", command=down,width=100,activeforeground='#00EAD4',activebackground='#262626')
                move_down.pack(pady=10)
                move_down['background'] = "#00EAD4" 
                move_down['foreground']= '#262626'  #000d33
                move_down.config(font=('Comic Sans MS',10))
                update_button = Button(root, text="modifier client selected", command=update_record,width=100,activeforeground='#00EAD4',activebackground='#262626')
                update_button.pack(pady=10)
                update_button['background'] = "#00EAD4" 
                update_button['foreground']= '#262626'  #000d33
                update_button.config(font=('Comic Sans MS',10))
                add_record = Button(root, text="Ajouter client" ,command=add_record,width=100,activeforeground='#00EAD4',activebackground='#262626')
                add_record['background'] = "#00EAD4" 
                add_record['foreground']= '#262626'  #000d33
                add_record.config(font=('Comic Sans MS',10))
                add_record.pack(pady=10)
                # Remove One
                remove_one = Button(root, text=" supprimer client Selected",activeforeground='#00EAD4',activebackground='#262626', command=remove_one,width=100)
                remove_one.pack(pady=10)
                remove_one['background'] = "#00EAD4" 
                remove_one['foreground']= '#262626'  #000d33
                remove_one.config(font=('Comic Sans MS',10))
                # Remove all
                remove_all = Button(root, text="supprimer tout client",width=100, command=remove_all,activeforeground='#00EAD4',activebackground='#262626')
                remove_all.pack(pady=10)
                remove_all['background'] = "#00EAD4" 
                remove_all['foreground']= '#262626'  #000d33
                remove_all.config(font=('Comic Sans MS',10))
                # Bindings
                #my_tree.bind("<Double-1>", clicker)
                my_tree.bind("<ButtonRelease-1>", clicker)
            def openwinvtr():
                root = Toplevel(w)
                root.geometry("1000x720+0+0")
                root.configure(bg='#262626')
                root.title("gestion de voiteur")
                # Add some style
                style = ttk.Style()
                #Pick a theme
                style.theme_use("default")
                # Configure our treeview colors
                style.configure("Treeview", 
                    background="#D3D3D3",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#D3D3D3")
                # Change selected color
                style.map('Treeview', 
                    background=[('selected', 'blue')])
                # Create Treeview Frame
                tree_frame = Frame(root)
                tree_frame.pack(pady=20)
                # Treeview Scrollbar
                tree_scroll = Scrollbar(tree_frame)
                tree_scroll.pack(side=RIGHT, fill=Y)
                # Create Treeview
                my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
                # Pack to the screen
                my_tree.pack()
                #Configure the scrollbar
                tree_scroll.config(command=my_tree.yview)
                # Define Our Columns
                my_tree['columns'] = ("immatriculation", "marque", "carburant","modèle","puissance_fiscale ","Voiture","type")
                # Formate Our Columns
                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("immatriculation", anchor=CENTER, width=140)
                my_tree.column("marque", anchor=CENTER, width=140)
                my_tree.column("carburant", anchor=CENTER, width=140)
                my_tree.column("modèle", anchor=CENTER, width=140)
                my_tree.column("puissance_fiscale ", anchor=CENTER, width=140)
                my_tree.column("Voiture", anchor=CENTER, width=140)
                my_tree.column("type", anchor=CENTER, width=140)
                # Create Headings 
                my_tree.heading("#0", text="", anchor=CENTER)
                my_tree.heading("immatriculation", text="immatriculation", anchor=CENTER)
                my_tree.heading("marque", text="marque", anchor=CENTER)
                my_tree.heading("carburant", text="carburant", anchor=CENTER)
                my_tree.heading("modèle", text="modèle", anchor=CENTER)
                my_tree.heading("puissance_fiscale ", text="puissance_fiscale ", anchor=CENTER)
                my_tree.heading("Voiture", text="Voiture", anchor=CENTER)
                my_tree.heading("type", text="type", anchor=CENTER)
                # Add Data
                data = []
                for i in lvt:
                    if isinstance(i,VoitureVip):
                        los=[i.immat,i.marque,i.cerburant,i.model,i.puis,"VIP",i.type]
                        data.append(los)
                    else:
                        los=[i.immat,i.marque,i.cerburant,i.model,i.puis,"Citadinne",i.gamme]
                        data.append(los)
                # Create striped row tags
                my_tree.tag_configure('oddrow', background="white")
                my_tree.tag_configure('evenrow', background="lightblue")
                global count
                count=0
                for record in data:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2] ,record[3],record[4],record[5],record[6]), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],record[3],record[4],record[5],record[6]), tags=('oddrow',))
                    count += 1
                add_frame = Frame(root)
                add_frame.pack(pady=20)
                #Labels
                nl = Label(add_frame, text="immatriculation")
                nl.grid(row=0, column=0)
                il = Label(add_frame, text="marque")
                il.grid(row=0, column=1)
                tl = Label(add_frame, text="carburant")
                tl.grid(row=0, column=2)
                ol = Label(add_frame, text="modèle")
                ol.grid(row=0, column=3)
                po=Label(add_frame, text="puissance_fiscale ")
                po.grid(row=0, column=4)
                so=Label(add_frame, text="Voiture",width=20)
                so.grid(row=0, column=5)
                co=Label(add_frame, text="type")
                co.grid(row=0, column=6)
                #Entry boxes
                immatriculation_box = Entry(add_frame)
                immatriculation_box.grid(row=1, column=0)
                marque_box = Entry(add_frame)
                marque_box.grid(row=1, column=1)
                carburant_box = Entry(add_frame)
                carburant_box.grid(row=1, column=2)
                modèle_box = Entry(add_frame)
                modèle_box.grid(row=1, column=3)
                puissance_fiscale_box= Entry(add_frame)
                puissance_fiscale_box.grid(row=1,column=4)
                pizza = StringVar()
                pizza.set("")
                rvip_box=Radiobutton(root, text="vip", variable=pizza, value="vip")
                rvip_box.place(x=680,y=344)
                rcit_box=Radiobutton(root, text="Citadinne", variable=pizza, value="Citadinne")
                rcit_box.place(x=740,y=344)
                rvip_box.select()
                rcit_box.deselect()
                type_box=Entry(add_frame)
                type_box.grid(row=1,column=6)
                # Add Record
                def add_record():
                    my_tree.tag_configure('oddrow', background="white")
                    my_tree.tag_configure('evenrow', background="lightblue")
                    global count
                    if immatriculation_box.get()!="" and marque_box.get()!="" and carburant_box.get()!="" and modèle_box.get()!="" and puissance_fiscale_box.get()!="" and pizza.get()!="" and type_box.get()!="" :
                        nb=0
                        for i in data:
                            if i[0]==immatriculation_box.get():
                                nb=1
                                break
                        if nb==1:
                            messagebox.showerror("error","Utilisateur deja exist")
                        else:
                            if (pizza.get()=="vip") and (type_box.get()=="4*4" or type_box.get()=="SUV" or type_box.get()=="limousine" or type_box.get()=="minibus") or(pizza.get()=="Citadinne") and (type_box.get()=="A" or type_box.get()=="B" or type_box.get()=="C" or type_box.get()=="a" or type_box.get()=="b" or type_box.get()=="c"):
                                if pizza.get()=="vip":
                                    obj=VoitureVip(immatriculation_box.get(), marque_box.get(), carburant_box.get() ,modèle_box.get(),puissance_fiscale_box.get(),type_box.get())
                                    los=[immatriculation_box.get(), marque_box.get(), carburant_box.get() ,modèle_box.get(),puissance_fiscale_box.get(),"VIP",type_box.get()]
                                    data.append(los)
                                    lvt.append(obj)
                                else:
                                    obj=VoitureCitadinne(immatriculation_box.get(), marque_box.get(), carburant_box.get() ,modèle_box.get(),puissance_fiscale_box.get(),type_box.get())
                                    los=[immatriculation_box.get(), marque_box.get(), carburant_box.get() ,modèle_box.get(),puissance_fiscale_box.get(),"Citadinne",type_box.get()]
                                    data.append(los)
                                    lvt.append(obj)
                                if count % 2 == 0:
                                    my_tree.insert(parent='', index='end', iid=count, text="", values=(immatriculation_box.get(), marque_box.get(), carburant_box.get() ,modèle_box.get(),puissance_fiscale_box.get(),pizza.get(),type_box.get() ), tags=('evenrow',))
                                else:
                                    my_tree.insert(parent='', index='end', iid=count, text="", values=(immatriculation_box.get(), marque_box.get(), carburant_box.get(),modèle_box.get(), puissance_fiscale_box.get(),pizza.get(),type_box.get()), tags=('oddrow',))
                                    count += 1
                                # Clear the boxes
                                immatriculation_box.delete(0, END)
                                marque_box.delete(0, END)
                                carburant_box.delete(0, END)
                                modèle_box.delete(0,END)
                                puissance_fiscale_box.delete(0,END)
                                rvip_box.select()
                                rcit_box.deselect()
                                type_box.delete(0,END)
                            else:
                                messagebox.showerror("error","""il devrat etre comme suit:

                                voiture: VIP et type: 4*4 ou SUV ou limousine ou minibus



                                ou




                                voiture : Citadinne  et  type : A  ou  B  ou  C """)
                    else:
                        messagebox.showerror("error","entre touts les information")
                    
                # Remove all records
                def remove_all():
                    for record in my_tree.get_children():
                        my_tree.delete(record)
                    lvt.clear()
                # Remove one selected
                def remove_one():
                    try:
                        x = my_tree.selection()[0]
                        values=my_tree.item(x, 'values')
                        for i in data:
                            if i[0]==values[0]:
                                data.remove(i)
                        for i in lvt:
                            if i.immat==values[0]:
                                lvt.remove(i)
                        my_tree.delete(x)
                        immatriculation_box.delete(0, END)
                        marque_box.delete(0, END)
                        carburant_box.delete(0, END)
                        modèle_box.delete(0,END)
                        puissance_fiscale_box.delete(0 ,END)
                        rvip_box.deselect()
                        rcit_box.select()
                        type_box.delete(0,END)
                    except :
                        messagebox.showerror("error","pleas select voitur")
                       
                # Select Record
                def select_record():
                    # Clear entry boxes
                    immatriculation_box.delete(0, END)
                    marque_box.delete(0, END)
                    carburant_box.delete(0, END)
                    modèle_box.delete(0,END)
                    rvip_box.deselect()
                    rcit_box.select()
                    puissance_fiscale_box.delete(0 ,END)
                    type_box.delete(0,END)
                    
                    # Grab record number
                    selected = my_tree.focus()
                    # Grab record values
                    values = my_tree.item(selected, 'values')
                    #temp_label.config(text=values[0])
                    # output to entry boxes
                    immatriculation_box.insert(0, values[0])
                    marque_box.insert(0, values[1])
                    carburant_box.insert(0, values[2])
                    modèle_box.insert(0, values[3])
                    selected = my_tree.focus()
                    values = my_tree.item(selected, 'values')
                    if values[5]=="VIP":
                        rvip_box.select()
                        rcit_box.deselect()
                    else:
                        rvip_box.deselect()
                        rcit_box.select()
                    puissance_fiscale_box.insert(0, values[4])
                    type_box.insert(0, values[6])
                # Save updated record
                def update_record():
                    # Grab record number
                    try:
                        selected = my_tree.focus()
                        values = my_tree.item(selected, 'values')
                        # Save new data
                        if immatriculation_box.get()!="" and marque_box.get()!="" and carburant_box.get()!="" and modèle_box.get()!="" and puissance_fiscale_box.get()!="" and pizza.get()!="" and type_box.get()!="" :
                            nb=0
                            for i in data:
                                if i[0]==immatriculation_box.get() and values[0]!=immatriculation_box.get():
                                    nb=1
                                    break
                            if nb==1:
                                messagebox.showerror("error"," voitur deja exist")
                            else:
                                if (pizza.get()=="vip") and (type_box.get()=="4*4" or type_box.get()=="SUV" or type_box.get()=="limousine" or type_box.get()=="minibus") or(pizza.get()=="Citadinne") and (type_box.get()=="A" or type_box.get()=="B" or type_box.get()=="C" or type_box.get()=="a" or type_box.get()=="b" or type_box.get()=="c"):
                                    if pizza.get()=="vip":
                                        for i in data:
                                            if i[0]==values[0]:
                                                i[0]=immatriculation_box.get()
                                                i[1]=marque_box.get()
                                                i[2]=carburant_box.get()
                                                i[3]=modèle_box.get()
                                                i[4]=puissance_fiscale_box.get()
                                                i[5]="VIP"
                                                i[6]=type_box.get()
                                        for i in lvt:
                                            if i.immat==values[0]:
                                                if values[5]=="VIP" or values[5]=="vip":
                                                    i.immat=immatriculation_box.get()
                                                    i.marque=marque_box.get()
                                                    i.cerburant=carburant_box.get()
                                                    i.model=modèle_box.get()
                                                    i.puis=puissance_fiscale_box.get()
                                                    i.type=type_box.get()
                                                else:
                                                    for i in lvt:
                                                        if i.immat==values[0]:
                                                            lvt.remove(i)
                                                    obj=VoitureVip(immatriculation_box.get(), marque_box.get(), carburant_box.get() ,modèle_box.get(),puissance_fiscale_box.get(),type_box.get())
                                                    lvt.append(obj)
                                    else:
                                        for i in data:
                                            if i[0]==values[0]:
                                                i[0]=immatriculation_box.get()
                                                i[1]=marque_box.get()
                                                i[2]=carburant_box.get()
                                                i[3]=modèle_box.get()
                                                i[4]=puissance_fiscale_box.get()
                                                i[5]="Citadinne"
                                                i[6]=type_box.get()
                                        for i in lvt:
                                            if i.immat==values[0]:
                                                if values[5]=="Citadinne" or values[5]=="citadinne":
                                                    i.immat=immatriculation_box.get()
                                                    i.marque=marque_box.get()
                                                    i.cerburant=carburant_box.get()
                                                    i.model=modèle_box.get()
                                                    i.puis=puissance_fiscale_box.get()
                                                    i.gamme=type_box.get()
                                                else:
                                                    for i in lvt:
                                                        if i.immat==values[0]:
                                                            lvt.remove(i)
                                                    obj=VoitureCitadinne(immatriculation_box.get(), marque_box.get(), carburant_box.get() ,modèle_box.get(),puissance_fiscale_box.get(),type_box.get())
                                                    lvt.append(obj)
                                    my_tree.item(selected, text="", values=(immatriculation_box.get(), marque_box.get(), carburant_box.get() ,modèle_box.get(),puissance_fiscale_box.get(),pizza.get(),type_box.get()))
                                    # Clear entry boxes
                                    immatriculation_box.delete(0, END)
                                    marque_box.delete(0, END)
                                    carburant_box.delete(0, END)
                                    modèle_box.delete(0,END)
                                    rvip_box.deselect()
                                    rcit_box.select()
                                    puissance_fiscale_box.delete(0,END)
                                    type_box.delete(0,END)
                                else:
                                    messagebox.showerror("error","""il devrat etre comme suit:

                                    voiture: VIP et type: 4*4 ou SUV ou limousine ou minibus



                                    ou




                                    voiture : Citadinne  et  type : A  ou  B  ou  C """)
                        else: messagebox.showerror("error","entre touts les information")
                    except:
                        messagebox.showerror("error","pleas select voitur")
                    
                # Create Binding Click function
                def clicker(e):
                    try:
                        select_record()
                    except:
                        None
                # Move Row up
                def up():
                    rows = my_tree.selection()
                    for row in rows:
                        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)
                # Move Row Down
                def down():
                    rows = my_tree.selection()
                    for row in reversed(rows):
                        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)
                #Buttons
                move_up = Button(root, text="Move Up", command=up,width=100,activeforeground='#00EAD4',activebackground='#262626')
                move_up.pack(pady=10)
                move_up['background'] = "#00EAD4" 
                move_up['foreground']= '#262626'  #000d33
                move_up.config(font=('Comic Sans MS',10))
                move_down = Button(root, text="Move Down", command=down,width=100,activeforeground='#00EAD4',activebackground='#262626')
                move_down.pack(pady=10)
                move_down['background'] = "#00EAD4" 
                move_down['foreground']= '#262626'  #000d33
                move_down.config(font=('Comic Sans MS',10))
                update_button = Button(root, text="modifier Voiture selected", command=update_record,width=100,activeforeground='#00EAD4',activebackground='#262626')
                update_button.pack(pady=10)
                update_button['background'] = "#00EAD4" 
                update_button['foreground']= '#262626'  #000d33
                update_button.config(font=('Comic Sans MS',10))
                add_record = Button(root, text="Ajouter Voiture" ,command=add_record,width=100,activeforeground='#00EAD4',activebackground='#262626')
                add_record['background'] = "#00EAD4" 
                add_record['foreground']= '#262626'  #000d33
                add_record.config(font=('Comic Sans MS',10))
                add_record.pack(pady=10)
                # Remove One
                remove_one = Button(root, text=" supprimer Voiture Selected",activeforeground='#00EAD4',activebackground='#262626', command=remove_one,width=100)
                remove_one.pack(pady=10)
                remove_one['background'] = "#00EAD4" 
                remove_one['foreground']= '#262626'  #000d33
                remove_one.config(font=('Comic Sans MS',10))
                # Remove all
                remove_all = Button(root, text="supprimer tout Voiture",width=100, command=remove_all,activeforeground='#00EAD4',activebackground='#262626')
                remove_all.pack(pady=10)
                remove_all['background'] = "#00EAD4" 
                remove_all['foreground']= '#262626'  #000d33
                remove_all.config(font=('Comic Sans MS',10))
                # Bindings
                #my_tree.bind("<Double-1>", clicker)
                my_tree.bind("<ButtonRelease-1>", clicker)
            def openwinloca():
                root =Toplevel(w)
                root.geometry("800x700-1+0")
                root.configure(bg='#262626')
                root.title("gestion de location")
                # Add some style
                style = ttk.Style()
                #Pick a theme
                style.theme_use("default")
                # Configure our treeview colors
                style.configure("Treeview", 
                    background="#D3D3D3",
                    foreground="black",
                    rowheight=20,
                    fieldbackground="#D3D3D3"
                    )
                # Change selected color
                style.map('Treeview', 
                    background=[('selected', 'blue')])
                # Create Treeview Frame
                tree_frame = Frame(root)
                tree_frame.pack(pady=20)
                # Treeview Scrollbar
                tree_scroll = Scrollbar(tree_frame)
                tree_scroll.pack(side=RIGHT, fill=Y)
                # Create Treeview
                my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
                # Pack to the screen
                my_tree.pack()
                #Configure the scrollbar
                tree_scroll.config(command=my_tree.yview)
                # Define Our Columns
                my_tree['columns'] = ("idLocation","date_de_location","durée_de_location","prix_de_location","CIN","immatriculation")
                # Formate Our Columns
                my_tree.column("#0", width=0, stretch=NO)
                my_tree.column("idLocation", anchor=CENTER, width=120)
                my_tree.column("date_de_location", anchor=CENTER, width=120)
                my_tree.column("durée_de_location", anchor=CENTER, width=120)
                my_tree.column("prix_de_location", anchor=CENTER, width=120)
                my_tree.column("CIN", anchor=CENTER, width=120)
                my_tree.column("immatriculation", anchor=CENTER, width=120)
                # Create Headings 
                my_tree.heading("#0", text="", anchor=CENTER)
                my_tree.heading("idLocation", text="idLocation", anchor=CENTER)
                my_tree.heading("date_de_location", text="date_de_location", anchor=CENTER)
                my_tree.heading("durée_de_location", text="durée_de_location", anchor=CENTER)
                my_tree.heading("prix_de_location", text="prix_de_location", anchor=CENTER)
                my_tree.heading("CIN", text="CIN", anchor=CENTER)
                my_tree.heading("immatriculation", text="immatriculation", anchor=CENTER)
                # Add Data
                data = []
                for i in ll:
                    lk=[i.idloca,i.date,i.duree,i.prix,i.clt.cin,i.voitur.immat]
                    data.append(lk)
                # Create striped row tags
                my_tree.tag_configure('oddrow', background="white")
                my_tree.tag_configure('evenrow', background="lightblue")
                global count
                count=0
                for record in data:
                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2] ,record[3],record[4],record[5] ), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],record[3],record[4],record[5] ), tags=('oddrow',))
                    count += 1
                # add child
                #my_tree.insert(parent='', index='end', iid=6, text="Child", values=("Steve", "1.2", "Peppers"))
                #my_tree.move('6', '0', '0')
                add_frame = Frame(root)
                add_frame.pack(pady=10)
                #Labels
                nl = Label(add_frame, text="CIN")
                nl.grid(row=0, column=2)
                np = Label(add_frame, text="immatriculation")
                np.grid(row=0, column=3)
                cho=Label(add_frame, text="durée_de_location")
                cho.grid(row=0, column=0)
                cto=Label(add_frame, text="prix_de_location")
                cto.grid(row=0, column=1)
                #Entry boxes
                CIN_box = Entry(add_frame)
                CIN_box.grid(row=1, column=2)
                immatriculation_box = Entry(add_frame)
                immatriculation_box.grid(row=1, column=3)
                durée_de_location_box=Entry(add_frame)
                durée_de_location_box.grid(row=1,column=0)
                prix_de_location_box=Entry(add_frame)
                prix_de_location_box.grid(row=1,column=1)
                # Add Record
                def add_record():
                    my_tree.tag_configure('oddrow', background="white")
                    my_tree.tag_configure('evenrow', background="lightblue")
                    global count
                    if  durée_de_location_box.get()!="" and CIN_box.get()!="" and immatriculation_box.get()!="":
                        nbvt=0
                        nbclt=0
                        for i in lvt:
                            if i.immat==immatriculation_box.get():
                                objv=i
                                nbvt+=1
                                break
                        for i in lclt:
                            if i.cin==CIN_box.get():
                                objc=i
                                nbclt+=1
                                break
                        if nbclt==0 and nbvt==1:
                            messagebox.showerror("error","le CIN client ne pas exist   visit l option gestion de client et creat client et ecrir le meme CIN")
                        elif nbvt==0 and nbclt==1:
                            messagebox.showerror("error","le voitur ne pas exist   visit l option gestion de voitur et creat voitur et ecrir le meme immatriculation")
                        elif nbclt==0 and nbvt==0:
                            messagebox.showerror("error","le immatriculation de voitur et de CIN client ne pas exist   visit l option gestion de voitur et gestion de client -> creat voitur et client ecrir le meme immatriculation et le meme CIN")
                        else:
                            obj=Location(durée_de_location_box.get(),prix_de_location_box.get(),objc,objv)
                            ll.append(obj)
                            if count % 2 == 0:
                                my_tree.insert(parent='', index='end', iid=count, text="", values=(obj.idloca,obj.date,durée_de_location_box.get(),prix_de_location_box.get(),CIN_box.get(),immatriculation_box.get() ), tags=('evenrow',))
                            else:
                                my_tree.insert(parent='', index='end', iid=count, text="", values=(obj.idloca,obj.date,durée_de_location_box.get(),prix_de_location_box.get(),CIN_box.get(),immatriculation_box.get()), tags=('oddrow',))
                            count += 1
                            # Clear the boxes
                            durée_de_location_box.delete(0,END)
                            prix_de_location_box.delete(0,END)
                            CIN_box.delete(0, END)
                            immatriculation_box.delete(0, END)
                            durée_de_location_box.delete(0,END)
                            prix_de_location_box.delete(0,END)
                    else:messagebox.showerror("error","entrez toutes les information")
                # Remove all records
                def remove_all():
                    for record in my_tree.get_children():
                        my_tree.delete(record)
                    ll.clear()
                    data.clear()
                # Remove one selected
                def remove_one():
                    try:
                        x = my_tree.selection()[0]
                        values = my_tree.item(x, 'values')
                        for i in data:
                            if str(i[0])==str(values[0]):
                                data.remove(i)
                        for i in ll:
                            if str(i.idloca)==str(values[0]):
                                ll.remove(i)
                        my_tree.delete(x)
                        durée_de_location_box.delete(0,END)
                        prix_de_location_box.delete(0,END)
                        CIN_box.delete(0, END)
                        immatriculation_box.delete(0, END)
                    except:
                        messagebox.showerror("error","pleas select location")
                # Select Record
                def select_record():
                    # Clear entry boxes
                    durée_de_location_box.delete(0,END)
                    prix_de_location_box.delete(0,END)
                    CIN_box.delete(0, END)
                    immatriculation_box.delete(0, END)
                    # Grab record number
                    selected = my_tree.focus()
                    # Grab record values
                    values = my_tree.item(selected, 'values')
                    #temp_label.config(text=values[0])
                    # output to entry boxes
                    durée_de_location_box.insert(0, values[2])
                    prix_de_location_box.insert(0, values[3])
                    CIN_box.insert(0, values[4])
                    immatriculation_box.insert(0, values[5])
                # Save updated record
                def update_record():
                    try:
                        # Grab record number
                        selected = my_tree.focus()
                        values = my_tree.item(selected, 'values')
                        if  durée_de_location_box.get()!="" and CIN_box.get()!="" and immatriculation_box.get()!="":
                            nbvt=0
                            nbclt=0
                            for i in lvt:
                                if i.immat==immatriculation_box.get():
                                    objv=i
                                    nbvt+=1
                                    break
                            for i in lclt:
                                if i.cin==CIN_box.get():
                                    objc=i
                                    nbclt+=1
                                    break
                            if nbclt==0 and nbvt==1:
                                messagebox.showerror("error","le CIN client ne pas exist   visit l option gestion de client et creat client et ecrir le meme CIN")
                            elif nbvt==0 and nbclt==1:
                                messagebox.showerror("error","le voitur ne pas exist   visit l option gestion de voitur et creat voitur et ecrir le meme immatriculation")
                            elif nbclt==0 and nbvt==0:
                                messagebox.showerror("error","le immatriculation de voitur et de CIN client ne pas exist   visit l option gestion de voitur et gestion de client -> creat voitur et client ecrir le meme immatriculation et le meme CIN")
                            else:
                                # Save new data
                                for i in ll:
                                    if str(i.idloca)==str(values[0]):
                                        i.duree=durée_de_location_box.get()
                                        i.prix=prix_de_location_box.get()
                                        i.clt=objc
                                        i.voitur=objv
                                for i in data:
                                    if i[0]==values[0]:
                                        i[2]==durée_de_location_box.get()
                                        i[3]==prix_de_location_box.get()
                                        i[4]==CIN_box.get()
                                        i[5]==immatriculation_box.get()
                                my_tree.item(selected, text="", values=(values[0],values[1],durée_de_location_box.get(),prix_de_location_box.get(),CIN_box.get(),immatriculation_box.get()))
                                # Clear entry boxes
                                CIN_box.delete(0, END)
                                immatriculation_box.delete(0, END)
                                durée_de_location_box.delete(0,END)
                                prix_de_location_box.delete(0,END)
                        else:messagebox.showerror("error","entrez toutes les information")
                    except:
                        messagebox.showerror("error","pleas select location")

                    
                # Create Binding Click function
                def clicker(e):
                    try:
                        select_record()
                    except:
                        None
                # Move Row up
                def up():
                    rows = my_tree.selection()
                    for row in rows:
                        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)
                # Move Row Down
                def down():
                    rows = my_tree.selection()
                    for row in reversed(rows):
                        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)
                #Buttons
                move_up = Button(root, text="Move Up", command=up,width=100,activeforeground='#00EAD4',activebackground='#262626')
                move_up.pack(pady=10)
                move_up['background'] = "#00EAD4" 
                move_up['foreground']= '#262626'  #000d33
                move_up.config(font=('Comic Sans MS',10))
                move_down = Button(root, text="Move Down", command=down,width=100,activeforeground='#00EAD4',activebackground='#262626')
                move_down.pack(pady=10)
                move_down['background'] = "#00EAD4" 
                move_down['foreground']= '#262626'  #000d33
                move_down.config(font=('Comic Sans MS',10))
                update_button = Button(root, text="modifier Location selected", command=update_record,width=100,activeforeground='#00EAD4',activebackground='#262626')
                update_button.pack(pady=10)
                update_button['background'] = "#00EAD4" 
                update_button['foreground']= '#262626'  #000d33
                update_button.config(font=('Comic Sans MS',10))
                add_record = Button(root, text="Ajouter Location" ,command=add_record,width=100,activeforeground='#00EAD4',activebackground='#262626')
                add_record['background'] = "#00EAD4" 
                add_record['foreground']= '#262626'  #000d33
                add_record.config(font=('Comic Sans MS',10))
                add_record.pack(pady=10)
                # Remove One
                remove_one = Button(root, text=" supprimer Location Selected",activeforeground='#00EAD4',activebackground='#262626', command=remove_one,width=100)
                remove_one.pack(pady=10)
                remove_one['background'] = "#00EAD4" 
                remove_one['foreground']= '#262626'  #000d33
                remove_one.config(font=('Comic Sans MS',10))
                # Remove all
                remove_all = Button(root, text="supprimer tout Location",width=100, command=remove_all,activeforeground='#00EAD4',activebackground='#262626')
                remove_all.pack(pady=10)
                remove_all['background'] = "#00EAD4" 
                remove_all['foreground']= '#262626'  #000d33
                remove_all.config(font=('Comic Sans MS',10))
                # Bindings
                #my_tree.bind("<Double-1>", clicker)
                my_tree.bind("<ButtonRelease-1>", clicker)
            w.geometry('900x500+300+150')
            w.configure(bg='#262626')
            w.resizable(0,0)
            w.title('agence de location de voiture 🔘')
            l1=Label(w,text='agence de location de voiture 🚗',fg='white',bg='#262626')
            l1.config(font=('Comic Sans MS',40))
            l1.pack(padx=20,pady=80,)
            l2=Label(w,text='❤️La meilleure agence de location de voiture  ❤️',fg='white',bg='#262626')
            l2.config(font=('Comic Sans MS',20))
            l2.pack(padx=20,pady=20)
            def toggle_win():
                f1=Frame(w,width=300,height=500,bg='#12c4c0')
                f1.place(x=0,y=0)
                #buttons
                def bttn(x,y,text,bcolor,fcolor,cmd):
                    def on_entera(e):
                        myButton1['background']= bcolor #ffcc66
                        myButton1['foreground']= '#262626'  #000d33
                    def on_leavea(e):
                        myButton1['background']= fcolor
                        myButton1['foreground']= '#262626'
                    myButton1 = Button(f1,text=text,
                                width=42,
                                height=2,
                                fg='#262626',
                                border=0,
                                bg=fcolor,
                                activeforeground='#262626',
                                activebackground=bcolor,            
                                    command=cmd)             
                    myButton1.bind("<Enter>", on_entera)
                    myButton1.bind("<Leave>", on_leavea)
                    myButton1.place(x=x,y=y)
                bttn(0,80,'Gestion Utilisateur','#0f9d9a','#12c4c0',openwin)
                bttn(0,117,'Gestion Client','#0f9d9a','#12c4c0', openwinclt)
                bttn(0,154,'Gestion Voiture','#0f9d9a','#12c4c0',openwinvtr)
                bttn(0,191,'Gestion Locations','#0f9d9a','#12c4c0',openwinloca)
                def dele():
                    f1.destroy()
                global img2
                img2 = "X"
                Button(f1,
                    text=img2,
                    border=0,
                    font=('Comic Sans MS',20),
                    command=dele,
                    bg="#12c4c0",
                    fg='#ffffff',
                    activebackground='#12c4c0').place(x=0,y=0)
            img1 = "|||"
            Button(w,text=img1,
                command=toggle_win,
                border=0,
                font=('Comic Sans MS',20),
                bg='#262626',
                fg= '#00EAD4',
                activebackground='#262626').place(x=5,y=10)
def registers():
    re=Toplevel(mains)
    re.geometry('450x400+150+150')
    re.configure(bg='#262626')
    re.resizable(0,0)
    label_titl=Label(re,text="page registers",fg='white',bg='#262626')
    label_titl.config(font=('Comic Sans MS',20))
    label_titl.place(x=160, y=40)
    label_login=Label(re,text="login",fg='white',bg='#262626')
    label_login.config(font=('Comic Sans MS',15))
    label_login.place(x=70, y=120)
    label_password=Label(re,text="password",fg='white',bg='#262626')
    label_password.config(font=('Comic Sans MS',15))
    label_password.place(x=70, y=180)
    label_email=Label(re,text="email",fg='white',bg='#262626')
    label_email.config(font=('Comic Sans MS',15))
    label_email.place(x=70, y=240)
    login_box=Entry(re,width=35)
    login_box.place(x=200,y=130)
    password_box=Entry(re,width=35)
    password_box.place(x=200,y=188)
    email_box=Entry(re,width=35)
    email_box.place(x=200,y=250)
    def tot():
        if login_box.get()!="" and password_box.get()!="" and email_box.get()!="":
            nb=0
            for i in l:
                if i.login==login_box.get():
                    nb=1
                    break
            if nb==1:
                messagebox.showerror("error","Utilisateur deja exist")
            else:
                obj=Utilisateur(login_box.get(),password_box.get(),email_box.get())
                l.append(obj)
                if messagebox.showinfo("enregistré avec succès","enregistré avec succès"):
                    re.destroy()
        else:messagebox.showerror("error","entrez toutes les information")
    reg = Button(re, text="s´inscrire",width=10,activeforeground='#00EAD4',activebackground='#262626',command=tot)
    reg.place(x=200,y=300)
    reg['background'] = "#00EAD4" 
    reg['foreground']= '#262626'  #000d33
    reg.config(font=('Comic Sans MS',10))
login = Button(mains, text="Login",width=10,activeforeground='#00EAD4',activebackground='#262626',command=logins)
login.place(x=250,y=250)
login['background'] = "#00EAD4" 
login['foreground']= '#262626'  #000d33
login.config(font=('Comic Sans MS',10))
register = Button(mains, text="register",width=10,activeforeground='#00EAD4',activebackground='#262626',command=registers)
register.place(x=380,y=250)
register['background'] = "#00EAD4" 
register['foreground']= '#262626'  #000d33
register.config(font=('Comic Sans MS',10))
mains.mainloop()