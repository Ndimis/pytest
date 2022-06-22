# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 17:52:38 2022

@author: tndim
"""

import tkinter, string, random 

def generate_password():
    min_pwd = 6
    max_pwd = 12
    all_char = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(all_char) for x in range(random.randint(min_pwd, max_pwd)))
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)    
        
    

#créer la fenètre 
window = tkinter.Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("prh.ico")
window.config(background='#4065A4')

#Frame principale
frame = tkinter.Frame(window, bg='#4065A4')

#creation d'image
width = 300
height = 300
image= tkinter.PhotoImage(file="user-data.png").zoom(16).subsample(32)
canvas = tkinter.Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky='w')

#Sous boite
rigth_frame = tkinter.Frame(frame, bg='#4065A4')

#Titre
label_title = tkinter.Label(rigth_frame, text='Mot de passe',font=("Helvetica", 20), bg='#4065A4', fg='white')
label_title.pack()

#Un champ de saisi
password_entry = tkinter.Entry(rigth_frame,  font=("Helvetica", 20), bg='#4065A4', fg='white')
password_entry.pack()

#Button
generate_pwd_button = tkinter.Button(rigth_frame, text='Générer',font=("Helvetica", 20), bg='#4065A4', fg='white', command=generate_password)
generate_pwd_button.pack(fill='x')

#on place la sous boite à droite de la frame 
rigth_frame.grid(row=0, column=1, sticky='w')

#Afficher la frame
frame.pack(expand='YES')

#Bar de menu
menu_bar = tkinter.Menu(window)
#premier menu
file_menu = tkinter.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)

#Ajouter la menu bar a la fenetre
window.config(menu=menu_bar)

menu_bar.add_cascade(label='Fichier', menu=file_menu)

#Afficher la fenètre
window.mainloop()
