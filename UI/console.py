def printMenu():
    print("1.Adaugare carte")
    print("2.Stergere carte")
    print("3.Modificare carte")
    print("a.Afisare carti")
    print("x.Iesire")

def uiAdaugaCarte(lista):
    id=input("Dati id-ul: ")
    titlu=input("Dati titlul:")
    gen=input("Dati genul:")
    pret=float(input("Dati pretul:"))
    tip_reducere=input("Dati tipul reducerii:")
    return adaugaCarte(id,titlu,gen,pret,tip_reducere,lista)

def uiStergeCarte(lista):
    id =input("Dati id-ul prajiturii de sters:")
    return stergeCarte(id,lista)


def uiModificaCarte(lista):
    id = input("Dati id-ul cartii de modificat: ")
    titlu = input("Dati noul titlul:")
    gen = input("Dati  noul gen:")
    pret = float(input("Dati noul  pret:"))
    tip_reducere = input("Dati tipul noii reducerii:")
    return modificaCarte(id, titlu, gen, pret, tip_reducere, lista)

def showAll(lista):
    for carte in lista:
        print(toString(carte))


def runMenu(lista):
    while True:
        printMenu()
        optiune=input("Dati optiunea:")

        if optiune=="1":
            lista=uiAdaugaCarte(lista)
        elif optiune=="2":
            lista=uiStergeCarte(lista)
        elif optiune=="3":
            lista=uiModificaCarte(lista)
        elif optiune=="a":
            showAll(lista)
        elif optiune=="x":
            break
        else:
            print("Optiune gresita!Reincercati:")



