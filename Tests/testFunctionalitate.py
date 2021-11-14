from Domain.carte import getPret,getGen,getId
from Logic.CRUD import adaugaCarte,getById
from Logic.functionalitate import aplicareDiscount,modificareGen,pretMin,ordonarePret,numarTitluri


def testaplicareDiscount():
    lista = []
    lista = adaugaCarte("1", "Iliada Homer" , "istorie", 80, "gold", lista)
    lista = adaugaCarte("2", "Surprise Me", "actiune", 45, "silver", lista)


    lista = aplicareDiscount(lista)

    assert getPret(getById("1", lista)) == 72
    assert getPret(getById("2", lista)) == 42.75

def testmodificareGen():
    lista = []
    lista = adaugaCarte("1","Iliada Homer","istorie",80,"gold", lista)
    lista = adaugaCarte("2","Surprise Me","actiune",45,"silver", lista )


    modificareGen("Iliada Homer","istorie", lista)
    assert getGen(getById("1", lista))=="istorie"


    modificareGen("Surprise Me","actiune",lista)
    assert getGen(getById("2", lista))=="actiune"

def testpretMin():
    lista = []
    lista = adaugaCarte("1","Iliada Homer","istorie", 80, "gold", lista)
    lista = adaugaCarte("2", "Surprise Me", "actiune", 45, "silver", lista)
    lista = adaugaCarte("3", "Cine conduce lumea", "drama", 60, "gold", lista)


    rezultat=pretMin(lista)

    assert len(rezultat) == 3
    assert rezultat["actiune"] == 45
    assert rezultat["drama"] == 60
    assert rezultat["istorie"] == 80

def testordonarePret():
    lista=[]
    lista = adaugaCarte("1", "Iliada Homer", "istorie", 80, "gold", lista)
    lista = adaugaCarte("2", "Surprise Me", "actiune", 45, "silver", lista)

    rezultat=ordonarePret(lista)

    assert getId(rezultat[0]) == "1"
    assert getId(rezultat[1]) == "2"



def testnumarTitluri():
    lista=[]
    lista = adaugaCarte("1", "Iliada Homer", "istorie", 80, "gold", lista)
    lista = adaugaCarte("2", "Surprise Me", "actiune", 45, "silver", lista)



    rezultat=numarTitluri(lista)

    assert rezultat["istorie"] == 1
    assert rezultat["actiune"] == 1



