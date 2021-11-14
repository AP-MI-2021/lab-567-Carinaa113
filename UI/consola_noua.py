from Domain.carte import toString
from Logic.CRUD import modificaCarte,stergeCarte,adaugaCarte

def uiAdaugaCarte(vanzari,lista):
    try:
        id = vanzari[0]
        titlu = vanzari[1]
        gen = vanzari[2]
        pret = float(vanzari[3])
        tip_reducere = vanzari[4]
        return adaugaCarte(id, titlu, gen, pret, tip_reducere, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergeCarte(vanzari, lista):
    try:
        id = vanzari[0]
        return stergeCarte(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificaCarte(vanzari, lista):
    try:
        id = vanzari[0]
        titlu = vanzari[1]
        gen = vanzari[2]
        pret = float(vanzari[3])
        tip_reducere = vanzari[4]
        return modificaCarte(id, titlu, gen, pret, tip_reducere, lista)
    except ValueError as ve:
        print("Eroare:{}".format(ve))
        return lista


def showAll(lista):
    for carte in lista:
        print(toString(carte))

def ajutor():
    '''
    un nou meniu prin care tote comenzile sunt separate prin ';' si ","
    :return:
    '''
    print("add, id, titlu, gen, pret, tip_reducere"
          "Delete, id"
          "Modify, id,titlu, gen, pret, tip_reducere"
          "Show All"
          "help"
          "Iesire")


def meniu(lista):
    try:
        while True:
            comenzi = input("Comenzi separate prin ';' si ','")
            vanzari = []
            vanzari = comenzi.split(";")
            for comanda in vanzari:
                operatie = []
                operatie = comanda.split(",")
                if operatie[0] == "Add":
                    operatie.pop(0)
                    lista = uiAdaugaCarte(operatie , lista)
                elif operatie[0] == "Delete":
                    operatie.pop(0)
                    lista = uiStergeCarte(operatie, lista)
                elif operatie[0] == "Modify":
                    operatie.pop(0)
                    lista = uiModificaCarte(operatie, lista)
                elif operatie[0] == "Show All":
                    showAll(lista)
                elif operatie[0] == "help":
                    help()
                elif operatie[0] == "Iesire":
                    break
                else:
                    print("Optiune gresita! Reincercati: ")

    except Exception as ex:
        print("Eroare, reincercati!" , ex)



