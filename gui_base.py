# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:59:38 2022

@author: tndim
"""
import tkinter, webbrowser

def open_youtube():
    webbrowser.open_new("https://youtube.com")

#la fenètre de base

window = tkinter.Tk()

#personnaliser la fenetre
window.title("My Application")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("prh.ico")
window.config(background='#41B77F')

#créer une frame
frame = tkinter.Frame(window, bg='#41B77F') #bd=1, relief='sunken')

#Ajouter un nouveau texte
label_title = tkinter.Label(frame, text="Bienvenue sur l'application", font=("Courrier", 40), bg='#41B77F', fg='white')
label_title.pack()

#ajouter un second texte
label_subtitle = tkinter.Label(frame, text="Salut à tous c'est Maury", font=("Courrier", 28), bg='#41B77F', fg='white')
label_subtitle.pack()

#ajouter un premier bouton
th_button = tkinter.Button(frame, text="Open YouTube", font=("Courrier", 40), bg='white', fg='#41B77F', command=open_youtube)
th_button.pack(pady='25', fill='x') 

#ajouter le frame
frame.pack(expand='YES')


#Afficher 

window.mainloop()