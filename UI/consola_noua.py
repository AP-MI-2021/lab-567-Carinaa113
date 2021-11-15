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


def meniu(lista):
    print("Comenzile introduse trebuie separate prin ; acestea putand fi: \n"
                  "Adaugare: add,id,titlu,gen,pret,tip reducere \n"
                  "Stergere: delete,id-ul cartii de sters \n"
                  "Afisare: showall \n"
                  "Atentie !!! Comenzile trebuie introduse exact ca in modelul de mai sus !")

def meniu_nou(lista):
    while True:
        meniu(lista)
        comenzi = input("Introduceti comenzile: ").split(";")
        for i in range(len(comenzi)):
            comanda = comenzi[i].split(",")
            if comanda[0] == "add":
                try:
                    lista=adaugaCarte(comanda[1], comanda[2], comanda[3], float(comanda[4]), comanda[5], lista)
                except Exception as e:
                    print(f"Eroare: {e}")
            elif comanda[0] == " delete":
                try:
                    lista=stergeCarte(comanda[1], lista)
                except ValueError as ve:
                    print(f"Eroare: {ve}")
            elif comanda[0] == " showall ":
                for carte in lista:
                    print(toString(carte))
            else:
                print("Reincercati! Comanda introdusa gresit! ")

