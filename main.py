from UI.consola_noua import meniu
from UI.console import runMenu
from Tests.testAll import runAllTests


def main():
    runAllTests()
    lista=[]

    while True:
        print("1.Consola clasica")
        print("2.Consola noua")
        print("3.Exit")
        op=int(input("Alegeti consola: "))
        if op==1:
            lista=runMenu(lista)
        elif op==2:
            lista=meniu(lista)
        elif op==3:
            break
        else:
            print("Optiune invalida")

main()