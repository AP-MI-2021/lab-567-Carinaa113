from Domain.carte import toString
from Logic.CRUD import adaugaCarte,stergeCarte,modificaCarte
from Logic.functionalitate import aplicareDiscount,modificareGen,pretMin,ordonarePret,numarTitluri




def printMenu():
    print("1.Adaugare carte")
    print("2.Stergere carte")
    print("3.Modificare carte")
    print("4.Aplicare discount pentru toate cartile")
    print("5.Modificare gen in functie de titlu")
    print("6.Determinarea pretului minim in functie de gen")
    print("7.Ordonarea vanzarilor in ordine crescatoare")
    print("8.Afisarea numarului de titluri distincte pentru fiecare gen")
    print("u.undo")
    print("r.Redo")
    print("a.Afisare carti ")
    print("x.Iesire")

def undo(lista, undo_list, redo_list):
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    return lista

def redo(lista, undo_list, redo_list):
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    return lista

def uiAdaugaCarte(lista,undolist,redolist):
    try:
        id=input("Dati id-ul: ")
        titlu=input("Dati titlul:")
        gen=input("Dati genul:")
        pret=float(input("Dati pretul:"))
        tip_reducere=input("Dati tipul reducerii:")

        rezultat=adaugaCarte(id,titlu,gen,pret,tip_reducere,lista)

        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print('Eroare! Detalii:'.format(ve))
        return lista


def uiStergeCarte(lista, undolist, redolist):
   try:
       id = input("Dati id-ul cartii de sters: ")
       rezultat = stergeCarte(id, lista)

       undolist.append(lista)
       redolist.clear()
       return rezultat
   except ValueError as ve:
       print("Eroare: {}".format(ve))




def uiModificaCarte(lista,undolist,redolist):
    try:

        id = input("Dati id-ul cartii de modificat: ")
        titlu = input("Dati noul titlul:")
        gen = input("Dati  noul gen:")
        pret = float(input("Dati noul  pret:"))
        tip_reducere = input("Dati tipul noii reducerii:")
        rezultat = modificaCarte(id,titlu,gen,pret,tip_reducere,lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showAll(lista):
    for carte in lista:
        print(toString(carte))

def uiaplicareDiscount(lista, undolist, redolist):
    nou = aplicareDiscount(lista)
    undolist.append(lista)
    redolist.clear()
    return nou

def uimodificareGen(lista, undolist, redolist):
        titlu = input("Titlul cartii careia ii modificam genul: ")
        genNou = input("Noul gen: ")
        rezultat = modificareGen(titlu, genNou, lista)
        undolist.append(lista)
        redolist.clear()
        return rezultat


def uipretMin(lista):
    rezultat = pretMin(lista)
    for gen in rezultat:
        print("Genul {} are pretul minim".format(gen, rezultat[gen]))

def uiordonarePret(lista):
    showAll(ordonarePret(lista))

def uinumarTitluri(lista, undolist, redolist):
    print(numarTitluri(lista))


def runMenu( lista ):
   undolist = []
   redolist = []
   while True:
       printMenu()
       optiune=input("Dati optiunea: ")

       if optiune == "1":
           lista = uiAdaugaCarte(lista, undolist, redolist)
       elif optiune == "2":
           lista = uiStergeCarte(lista, undolist, redolist)
       elif optiune == "3":
           lista = uiModificaCarte(lista,undolist,redolist)
       elif optiune == "4":
           lista = uiaplicareDiscount(lista,undolist,redolist)
       elif optiune == "5":
           lista = uimodificareGen(lista, undolist, redolist)
       elif optiune == "6":
           uipretMin(lista)
       elif optiune == "7":
           uiordonarePret(lista)
       elif optiune == "8":
           uinumarTitluri(lista, redolist, undolist)
       elif optiune == "u":
           if len(undolist) > 0:
               redolist.append(lista)
               lista=undolist.pop()
           else:
               print("Nu se poate face undo.")
       elif optiune == "r":
           if len(redolist) > 0:
               undolist.append(lista)
               lista=redolist.pop()
           else:
               print("Nu se poate face redo.")
       elif optiune == "a":
           showAll(lista)
       elif optiune == "x":
           break
       else:
           print("Optiune gresita!Reincercati: ")



