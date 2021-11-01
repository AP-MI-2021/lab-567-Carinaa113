from UI.console import showAll
from Logic.CRUD import stergeCarte,modificaCarte,adaugaCarte
from Domain.carte import toString


def ShowAll(lista):
    for carte in lista:
        print(toString(carte))


def consola_noua(lista):
    while True:
        mesaj=input()
        if mesaj=="help":
            print("Add, id, pret, descriere, pret, locatie -> adauga obiect")
            print("Delete, id -> sterge obiect")
            print("Update, id -> modifica obiect")
            print("Showall -> afiseaza toate obiectele")
            print("Exit -> opreste programul")
        else:
            optiuni=mesaj.split(";")
            if optiuni[0]=="Exit":
                break
            else:
                for optiuni in optiuni:
                    camp=optiune.split(",")
                    if camp[0]=="Add":
                        try:
                            lista= addObject(camp[1], camp[2], camp[3], camp[4], camp[5], lista)
                        except ValueError as ve:
                            print("Eroare : {}".format(ve))
                    elif camp[0] == "Showall":
                        ShowAll(lista)
                    elif camp[0] == "Update":
                        lista = modifyObject(camp[1], camp[2], camp[3], camp[4], camp[5], lista)
                    elif camp[0] == "Delete":
                        try:
                            lista = deleteObject(camp[1], lista)
                        except ValueError as ve1:
                            print("Eroare : {}".format(ve1))
                    else:
                        print("Optiune gresita! Acceseaza comanda 'help'!")




