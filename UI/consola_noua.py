from Domain.carte import toString
from Logic.CRUD import modificaCarte,adaugaCarte,stergeCarte

def adaugare(id,titlu,gen,pret,tip_reducere,lista):
    try:
        return adaugaCarte(id,titlu,gen,pret,tip_reducere,lista)
    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista
def modificare(id,titlu,gen,pret,tip_reducere,lista):
    try:
        return modificaCarte(id,titlu,gen,pret,tip_reducere,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def stergere(id,lista):
    try:
        return stergeCarte(id,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showAll():
    for carte in lista:
        print(toString(carte))


def ajutor():
    print("Meniul comenzilor:")
    print("add - id, titlu, gen, pret, reducere(none, silver, gold) - adauga vanzare")
    print("update - id, titlu, gen, pret, reducere(none, silver, gold) - modifica vanzare")
    print("showAll - afisarea tuturor vanzarilor")
    print("delete - id - sterge vanzarea")
    print("stop - opreste programul")
    print("Introduceti comanda: ")

def meniu():
    lista=[]
    lista=adaugaCarte("1","Iliada Homer","istorie",80,"gold",lista)
    lista=adaugaCarte("2","Surprise Me","actiune",45,"silver",lista)
    functioneaza=True

    while functioneaza is True:
        ajutor()
        alegere = input()
        if alegere == "help":
            ajutor()
        else:
            comanda_lista = alegere.split(";")
            optiune = comanda_lista[0]
            for comanda in comanda_lista[1:]:
                opt = comanda.split(",")

            if optiune == "add":
                try:
                    lista = adaugare(opt[0], opt[1], opt[2], float(opt[3]), opt[4], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))

            elif optiune == "update":
                try:
                    lista = modificare(opt[0], opt[1], opt[2], float(opt[3]), opt[4], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))

            elif optiune == "delete":
                lista = stergere(opt[0], lista)
            elif optiune == "showAll":
                show_all(lista)
            elif optiune == "stop":
                functioneaza = False
            else:
                print("Comanda gresita! Incercati din nou!")



