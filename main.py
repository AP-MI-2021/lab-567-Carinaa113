
from UI.console import runMenu
from Tests.testAll import runAllTests
from UI.consola_noua import meniu



def main():
    runAllTests()
    print("1.consola veche")
    print("2.consola noua")
    console = int(input("dati nr consolei pe care vreti sa o alegeti"))
    if console == 1:
        runMenu([])
    elif console == 2:
        meniu([])


if __name__ == "__main__":
    main()
