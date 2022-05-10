#Autor Ousseni Ouedraogo etudiant en 4eme annee de medecine a l'universite de ouagadougou
#ce logiciel permetra de calculer la valeur en somme de l'or lors de la vente ou du payement

#importation des modules tkinter et math
from tkinter import*
from math import*
#determination des entrees de gold
Fen_Gold=Tk()#la fenetre principale
Fen_Gold.configure(bg="violet")

Entree_PH=Entry(Fen_Gold)
Entree_PB=Entry(Fen_Gold)
Entree_C=Entry(Fen_Gold)
#mise sur la grille les entrees
Entree_PH.grid(row=3,column=2,padx=10,pady=5)
Entree_PH.focus_set()#ramene le curseur a entre poids haut
Entree_PB.grid(row=5,column=2,padx=10,pady=5)
Entree_C.grid(row=7,column=2,padx=10,pady=5)
#determination des labels qui sont au nombres de sept
Poids_Haut=Label(Fen_Gold,text="Poids Haut",fg="blue")
Poids_Bas=Label(Fen_Gold,text="Poids Bas",fg="blue")
Coure=Label(Fen_Gold,text="Coure",fg="blue")
Unite1=Label(Fen_Gold,text="grammes",fg="blue")
Unite2=Label(Fen_Gold,text="grammes",fg="blue")
Unite3=Label(Fen_Gold,text="Francs cfa",fg="blue")
Quara=Label(Fen_Gold,text="Quara :",fg="blue")
Resultat=Label(Fen_Gold,text="Resultat=",fg="red")
Label_Valider=Label(Fen_Gold,text="")
LabQuara=Label(Fen_Gold,text="")
#mise sur la grille les labels
Poids_Haut.grid(row=3,column=1,padx=10,pady=5)
Poids_Bas.grid(row=5,column=1,padx=10,pady=5)
Coure.grid(row=7,column=1,padx=10,pady=5)
Unite1.grid(row=3,column=3,padx=10,pady=5)
Unite2.grid(row=5,column=3,padx=10,pady=5)
Unite3.grid(row=11,column=3,padx=10,pady=5)
Quara.grid(row=13,column=3,padx=10,pady=5)
Resultat.grid(row=11,column=1,padx=10,pady=5)
Label_Valider.grid(row=11,column=2,padx=10,pady=5)
LabQuara.grid(row=14,column=3,padx=10,pady=5)
#modelisation
Poids_Haut.configure(bg="violet")
Poids_Bas.configure(bg="violet")
Coure.configure(bg="violet")
Resultat.configure(bg="violet")
Unite3.configure(bg="violet")
Unite2.configure(bg="violet")
Unite1.configure(bg="violet")
#definition de la fonction calculatrice
def Calculatrice():
    Density=10.55
    Titre=52.838
    Uplower=float(Entree_PH.get())/float(Entree_PB.get())
    x1="%.2f" % Uplower
    x=float(x1)
    Resulat1=x-Density
    Resultat2=Resulat1*Titre
    y1="%.2f" % Resultat2
    y=float(y1)
    Resultat3=y/x
    z1="%.2f" % Resultat3
    global z
    z=float(z1)
    Resultat_Total1=z*float(Entree_PH.get())*float(Entree_C.get())
    p="%.2f" % Resultat_Total1
    Resultat_Total=float(p)
    return Resultat_Total
#mise en place de la fonction valider
def Valider():
    Chaine=Calculatrice()
    Label_Valider.config(text=Chaine)
def Initialiser():
    Label_Valider.config(text="")
    LabQuara.config(text="")
    Entree_C.delete(0,END)
    Entree_PB.delete(0,END)
    Entree_PH.delete(0,END)
    Entree_PH.focus_set()
#gestion des boutons
Buton_Valider=Button(Fen_Gold,text="Valider",bg="green",fg="white",command=Valider)
Buton_Reinitialiser=Button(Fen_Gold,text="Reinitialiser",bg="yellow",fg="blue",command=Initialiser)
Buton_Quitter=Button(Fen_Gold,text="Quiter",bg="red",fg="white",command=Fen_Gold.quit)
#affichase des boutons sur la grille
Buton_Valider.grid(row=9,column=2,padx=10,pady=5)
Buton_Reinitialiser.grid(row=13,column=1,padx=10,pady=5)
Buton_Quitter.grid(row=13,column=2,padx=10,pady=5)
#la fenetre principale
Fen_Gold.mainloop()