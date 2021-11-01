from Logic.CRUD import *


def showAll(lista):
    for carte in lista:
        print(toString(carte))


def linia_principala(lista):
    while True:
        givenString=input()
        if givenString=="help"
            print("add,id,nume,descriere,pret,tip_reducere")
            print("delete,id")
            print("showALL")
            print("Exit")

        else
            optiuni=givenString.split(";")
            if optiuni[0]=="exit":
                break
            else
                for optiune in optiuni:
                    opti= optiune.split(",")
                    if(opt[0]=="add"):
                        try:
                            lista= adaugaInventar(opti[1],opti[2],opti[3],float(opti[4],opti[5],lista))
                        except ValueError as ve:

