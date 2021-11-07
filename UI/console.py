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
    print("a.Afisare carti")
    print("x.Iesire")

def uiAdaugaCarte(lista):
    try:
        id=input("Dati id-ul: ")
        titlu=input("Dati titlul:")
        gen=input("Dati genul:")
        pret=float(input("Dati pretul:"))
        tip_reducere=input("Dati tipul reducerii:")

        rezultat=adaugaCarte(id,titlu,gen,pret,tip_reducere,lista)

        undolist.append(lista)
        redolist.clear(lista)
        return rezultat
    except ValueError as ve:
        print('Eroare! Detalii:', ve)
        return lista


def uiStergeCarte(lista):
   try:
       id=input("Dati id-ul cartii de sters: ")
       rezultat=stergeCarte(id,lista)

       undolist.append(lista)
       redolist.clear()
       return rezultat
   except ValueError as ve:
       print("Eroare: {}".format(ve))
       return lista



def uiModificaCarte(lista,undolist,redolist):
    try:

        id = input("Dati id-ul cartii de modificat: ")
        titlu = input("Dati noul titlul:")
        gen = input("Dati  noul gen:")
        pret = float(input("Dati noul  pret:"))
        tip_reducere = input("Dati tipul noii reducerii:")
        rezultat=modificareCarte(id,titlu,gen,pret,tip_reducere,lista)

        undolist.append(lista)
        redolist.clear()
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showAll(lista):
    for carte in lista:
        print(toString(carte))

def consolemodificareGen():
    try:
        titlu=input("Titlul cartii careia ii modificam genul: ")
        genNou=input("Noul gen: ")
        modificareGen(titlu,genNou,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def consolepretMin(lista):
    rezultat=pretMin(lista)
    for gen in rezultat:
        print("Genul {} are pretul minim".format(gen,rezultat[gen]))

def consoleordonarePret(lista):
    showAll(ordonarePret(lista))

def consolenumarTitluri(lista,undolist,redolist):
    rezultat=numarTitluri(lista)
    for gen in rezultat:
        print("Genul {} are numarul de titluri egal cu {}".format(gen,rezultat[gen]))

def uiaplicareDiscount(lista,undolist,redolist):
    undolist.append(lista)
    redolist.clear()
    return aplicareDiscount(lista)


def runMenu(lista):
   undolist=[]
   redolist=[]
   while True:
       print_menu()
       optiune=input("Datio optiunea: ")

       if optiune=="1":
           lista=uiAdaugaCarte(lista,undolist,redolist)
       elif optiune=="2":
           lista=uiStergeCarte(lista,undolist,redolist)
       elif optiune=="3":
           lista=uiModificaCarte(lista,undolist,redolist)
       elif optiune=="4":
           lista=uiaplicareDiscount(lista,undolist,redolist)
       elif optiune=="5":
           consolemodificareGen(lista)
       elif optiune=="6":
           consolepretMin(lista)
       elif optiune=="7":
           consoleordonarePret(lista)
       elif optiune=="8":
           consolenumarTitluri(lista)
       elif optiune=="u":
           redolist.append(lista)
           if len(undolist) > 0:
               lista=undolist.pop()
           else:
               print("Nu se poate face undo.")
       elif optiune=="r":
           undolist.append(lista)
           if len(redolist) > 0:
               lista=redolist.pop()
           else:
               print("Nu se poate face redo.")
       elif optiune =="a":
           showAll(lista)
       elif optiune=="x":
           break
       else:
           print("Optiune gresita!Reincercati: ")



