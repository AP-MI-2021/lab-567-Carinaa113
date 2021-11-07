from Logic.CRUD import adaugaCarte
from UI.consola_noua import meniu
from UI.console import runMenu
from Tests.testAll import runAllTests

def meniu_nou():
    print("1.Rezolvare prima metoda al UI")
    print("2.A doua metoda de rezolvare")
    print("3.Iesire")

def main():
    runAllTests()

    while True:
        meniu_nou()
        optiune=input("Dati optiunea: ")

        if optiune=="1":
            lista=[]
            lista=adaugaCarte("1","Colt Alb", "aventura",15,"silver",lista)
            lista=adaugaCarte("2","Scufita Rosie", "aventura",15,"silver",lista)
            print(runMenu(lista))
        elif optiune=="2":
            print(meniu())
        elif optiune=="3":
            break
        else:
            print("Optiune gresita!Reincercati :")

main()
