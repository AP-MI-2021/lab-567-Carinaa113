from Domain.carte import getPret,getGen,getId
from Logic.Crud import adaugaCarte,getById
from Logic.functionalitate import aplicareDiscount,modificareGen,pretMin,ordonarePret,numarTitluri


def testaplicareDiscount():
    lista=[]
    lista=adaugaCarte("1","Iliada Homer","istorie",80,"gold",lista)
    lista=adaugaCarte("2","Surprise Me","actiune",45,"silver",lista)
    lista=adaugaCarte("3","Arta Conversatiei","realism",38,"none",lista)

    lista=aplicareDiscount(lista)
    assert getPret(carte[0])==72
    assert getPret(carte[1])==42.75
    assert getPret(carte[2])==38

def testmodificareGen():
    lista=[]
    lista=adaugaCarte("1","Iliada Homer","istorie",80,"gold",lista)
    lista=adaugaCarte("2","Surprise Me","actiune",45,"silver",lista)
    lista=adaugaCarte("3","Arta Conversatiei","realism",38,"none",lista)

    modificareGen("Iliada Homer","istorie",80,"gold",lista)
    assert getGen(getById("1",lista))=="istorie"

    modificareGen("Arta Conversatiei","realism",38,"none",lista)
    assert getGen(getById("3",lista))=="realism"

    modificareGen("Surprise Me","actiune",45,"silver",lista)
    assert getGen(getById("2",lista))=="actiune"

def testpretMin():
    lista=[]
    lista=adaugaCarte("1","Iliada Homer","istorie",80,"gold",lista)
    lista=adaugaCarte("2","Surprise Me","actiune",45,"silver",lista)
    lista=adaugaCarte("3","Arta Conversatiei","realism",38,"none",lista)

    rezultat=pretMin(lista)

    assert len(rezultat)==2
    assert rezultat["realism"]== 38
    assert rezultat["actiune"]==45

def testordonarePret():
    lista=[]
    lista = adaugaCarte("1", "Iliada Homer", "istorie", 80, "gold", lista)
    lista = adaugaCarte("2", "Surprise Me", "actiune", 45, "silver", lista)
    lista = adaugaCarte("3", "Arta Conversatiei", "realism", 38, "none", lista)

    rezultat=ordonarePret(lista)

    assert getId(rezultat[0])=="3"
    assert getId(rezultat[1])=="2"
    assert getId(rezultat[2])=="1"


def testnumarTitluri():
    lista=[]
    lista = adaugaCarte("1", "Iliada Homer", "istorie", 80, "gold", lista)
    lista = adaugaCarte("2", "Surprise Me", "actiune", 45, "silver", lista)
    lista = adaugaCarte("3", "Arta Conversatiei", "realism", 38, "none", lista)

    rezultat=numarTitluri(lista)

    assert rezultat["istorie"]==1
    assert rezultat["actiune"]==1
    assert rezultat["realism"]==1



