#____________________________________________________________________________________
#-----------------Files_Managers version 1-2 using ttkbootstrop-----------------------
#------------------Lib_Importation----------
import os
import os.path 
import shutil  
from win10toast import ToastNotifier #----No needed if we want to built an exe cause of incompatiblity with pyinstaller if we want to built an exe
import tkinter
import time
import ttkbootstrap
import threading
#from functools import partial
from tkinter import filedialog,messagebox

#________________App.config________________
Config=[False] #Table 
#________________________def-about-langage_________________________
#Config[0]_return_an_bool_about_langage_:_True_for_Fr_And_False_for_Not_Fr_so_Es !
translate=[] # An board contain all words and sentences translating by Trad
"""def load():
    try:
        with open("Files_Manager.config","r") as config:
            Config.append(config.read())
    except:
        Config.append(False)
"""
def Trad():
    if Config[0]: #Fr
        text_0="Chargement..."
        text_1="Selectionner le Dossier cible de Files Manager:"
        text_2="Cibler"
        text_3="Excécuter Files_Manager frequement"
        text_4=text_1+"Selectionné"
        text_5="Organiser !!"
        text_6="Definir une frequence:"
        text_7="Lancement..."
        text_8="Arreter"
        text_9="Files Manager a été lancer avec success"
        text_10="ERREUR verifiez la frequence !"
        text_11="Fichiers ont été organisés par Files_Manager !"
        text_12="Organisation..."
        text_13="Aucun fichier trouver !"
        text_14="Arret..."
    else:
        text_0="Loading..."
        text_1="Please select Files Manager's Target Folder:"
        text_2="Target"
        text_3="Run Files_Manager frequenctlly"
        text_4=text_1+"Selected"
        text_5="Manage !!"
        text_6="Define frequency:"
        text_7="Launching..."
        text_8="Turn off"
        text_9="Files Manager has been launched successfully !!"
        text_10="ERROR,Please check frequency !"
        text_11="Files has been Managed By Files_manager !"
        text_12="Management..."
        text_13="No file found !"
        text_14="Stand off..."
    elts=(text_0,text_1,text_2,text_3,text_4,text_5,text_6,text_7,text_8,text_9,text_10,text_11,text_12,text_13,text_14)
    translate=[] 
    for elt in elts :
        translate.append(elt)
    return translate
    
    """
    def save():
    with open("Files_Manager.config","w") as doc:
        doc.write(str(Config[0]))
    """
def updating(bar_label):
    translate=Trad()
    if check_var.get():
        check_label.config(text=translate[6])
        if not Config[0]:
            put.place(x=300,y=260)
        else:
            put.place(x=350,y=260)
    label2.config(text=translate[1])
    if level[0]:
        but.config(text=translate[2])
        put.place(x=1000,y=1000)
    if level[1]:
        but.config(text=translate[5])
        bar_label.config(text=translate[12])
    if level[2]:
        but.config(text=translate[8])
    check.config(text=translate[3])

    
    #bar[0].config(text=translate[8])
    print("update")
def FM():
    #time.sleep(1000)
    label1.config(text="Files Manager")
    print("ok")
def next_prgm_4(bar):
    translate=Trad()
    label1.config(text=translate[0]+"Trad: Okay")
    updating(bar)
    screem.after(500,FM)
def change_langage(bar):
    if Config[0]:
        Config[0]=False
        
    else: 
        Config[0]=True
    #save()
    translate=Trad()
    label1.config(text=translate[0]+"Trad:")
    screem.after(1000,lambda:next_prgm_4(bar))
    

def do_nothing():#Because i can't write wid.config(command=lambda:pass)
    pass
def try_creation_dir(dir):
    try:os.mkdir(dir)
    except:pass

notification=ToastNotifier()
def notif(a,b,c=3):
    try:notification.show_toast(title=a,msg=b,duration=c,threaded=True)
    except:pass
def is_myself(file):
        
        return file in myself
def increase(n):
    return n+1
img=("png","jpeg","ico","jpg")
video=("mp4","ts")
sound=("mp3","m4a")
doc=("txt","docx","pdf")
compress=("zip","rar")
exe=("exe","py","c","c++","bat","vbs")
dirs=("Images","Video","Sounds","Documents","Others","Programms","Compressed")
ext_dir={
    img:dirs[0],
    video:dirs[1],
    sound:dirs[2],
    doc:dirs[3],
    exe:dirs[5],
    compress:dirs[6],
}
myself=("Files_manager.py","Files_manager.bat")
red="darkred"
white="white"
green="lightgreen"
black="black"
font1=("Bold",15)
font2=("arial",12)

def Off():
    screem.quit()
    exit()
def is_number(frequency):
    try:
        int(frequency)
        return int(frequency)
    except:
        return 3
def next_prgm_2(press):
    translate=Trad()
    press[1].place(x=220,y=420)
    press[0].config(text=translate[12])




level=[False,False,False]




def Go(frequency,running=True):
    translate=Trad()
    level[2]=True
    try:frequency=int(frequency)
    except:
        running=[False,]
        exit()
    running=[True,]
    pressbar.start()
    if check_var.get():
        pressbar_label.place(x=30,y=410)
        screem.after(1000,lambda:next_prgm_2([pressbar_label,pressbar]))
        but.place(x=640,y=445)
        bar=[pressbar_label,pressbar]
    while running[0]:
            files=os.listdir()
            number=0
            translate=Trad()
            for file in files:
                        #print("je suis la")
                        ext=file.split(".")
                        ext=ext[-1]
                        if ext in img :
                            try_creation_dir(ext_dir[img])
                            shutil.move(file,"Images/"+file)
                            number=increase(number)
                        elif ext in video:
                            try_creation_dir(ext_dir[video])
                            shutil.move(file,"Video/"+file)
                            number=increase(number)
                        elif ext in sound :
                            try_creation_dir(ext_dir[sound])
                            shutil.move(file,"Sounds/"+file)
                            number=increase(number)
                        elif ext in doc :
                            try_creation_dir(ext_dir[doc])
                            shutil.move(file,"Documents/"+file)
                            number=increase(number)
                        elif ext in exe and not is_myself(file) :
                            try_creation_dir(ext_dir[exe])
                            shutil.move(file,"Programms/"+file)
                            number=increase(number)
                        elif ext in compress :
                            try_creation_dir(ext_dir[compress])
                            shutil.move(file,"Compressed/"+file)
                            number=increase(number)
                        else :
                            if  is_myself(file) or os.path.isdir(file):
                                pass
                            else:
                                try_creation_dir(dirs[4])
                                shutil.move(file,"Others/"+file)
                                number=increase(number)
            but.config(text=translate[8],command=lambda:kill(running,bar))
            
            if number:
                        notif("Files Manager",str(number)+translate[11],5)
                        number=0
                    #print("fin------------")
            if check_var.get():
                pass
                
            else:
                running[0]=False
                but.config(text=translate[2],command=lambda:select())
                but.place(x=640,y=120)
                check.place(x=1000,y=1000)
                if number:
                    notif("Files Manager",str(number)+translate[11],5)
                else:
                    notif("Files Manager",translate[13],5)
            time.sleep(frequency)
            print(running)
    
def set_frequence():
    translate=Trad()
    if check_var.get():
        check_label.config(text=translate[6],font=("arial",12))
        check_label.place(x=105,y=265)
        if not Config[0]:
            put.place(x=300,y=260)
        else:
            put.place(x=350,y=260)
        
    else:
        check_label.place(x=1000,y=1000)
        put.place(x=1000,y=1000)
    
def next_prgm_3(bar):
    translate=Trad()
    put.place(x=1000,y=1000)
    check_label.place(x=1000,y=1000)
    if check_var.get():
        bar[0].place(x=1000,y=1000)
        bar[1].place(x=1000,y=1000)
    but.config(text=translate[2],command=lambda:select())
    but.place(x=640,y=120)
    check.place(x=1000,y=1000)


def kill(running,bar):
    translate=Trad()
    level[0],level[1],level[2]=True,False,False
    running[0]=False
    #print(running)
    screem.after(1100,lambda:next_prgm_3(bar))
    bar[0].config(text=translate[14])
    but.config(command=do_nothing)
    translate=Trad()
    return running


def can_be_converted(n):
    try:
        int(n)
        return True
    except:
        return False
def Run():
    #but.config(command=lambda:kill())
    translate=Trad()
    if check_var.get():
        #font2=("arial",12)
        if can_be_converted(put.get()):
            notif("Files Managers",translate[6]+str(put.get()))
            threading.Thread(target=Go,args=(put.get())).start()
        else:
            notif("Files Managers",translate[10],2)
        if not Config[0]:
            put.place(x=300,y=260)
        else:
            put.place(x=350,y=260)
    else:
        Go(0) #call just one time ////
        level[0],level[1],level[2]=True,False,False


def select():
    #time.sleep(1)
    translate=Trad()
    level[0],level[1]=False,True
    target=filedialog.askdirectory()
    label2.config(text=translate[4])
    but.place(x=640,y=370)
    but.config(text=translate[5],command=Run)
    pressbar_label.config(text=translate[7])
    check.place(x=105,y=170)
    check_label.place(x=105,y=265)
    if check_var.get():
        if not Config[0]:
            put.place(x=300,y=260)
        else:
            put.place(x=350,y=260)
    os.chdir(target)
    print()
    but.config(text=translate[5])


def next_prgm():
    translate=Trad()
    label1.config(text="Files Manager")
    label2.place(x=95,y=70)
    but.place(x=640,y=120)
    notif( "Files Manager",translate[9],6)
    
#-------------------------------------The_main_part-------------------------------------------
#load()

translate=Trad()
level[0]=True

screem=ttkbootstrap.Window(title="Files_Manager",themename="vapor",resizable=(False,False),iconphoto="Files_manager.ico")
screem.geometry("800x520")
#screem.resizable(width=False,height=False)
label1=ttkbootstrap.Label(text=translate[0],font=font1)
screem.after(1500,next_prgm)
label2=ttkbootstrap.Label(text=translate[1],font=font2,foreground=green)
but=ttkbootstrap.Button(text=translate[2],command=select,bootstyle="outline-secondary",)
label1.place(x=280,y=7)
check_var=ttkbootstrap.IntVar()
check_label=ttkbootstrap.Label(text="",foreground=red)
check_label.place(x=1000,y=1000)
put=ttkbootstrap.Entry()
check=ttkbootstrap.Checkbutton(text=translate[3],variable=check_var,command=set_frequence,bootstyle="success-round-toggle")

pressbar_label=ttkbootstrap.Label(text=translate[7],font=font2,foreground=green)
pressbar=ttkbootstrap.Progressbar(length=400,mode=['indeterminate'])
menu=ttkbootstrap.Menu()
menu.add_command(label="Change langage",command=lambda:change_langage(pressbar_label))
screem.config(menu=menu)
screem.mainloop()