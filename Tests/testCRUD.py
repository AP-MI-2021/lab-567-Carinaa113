from Logic.CRUD import adaugaCarte,getById,stergeCarte,modificaCarte
from Domain.carte import getId,getTitlu,getPret,getGen,getTip_Reducere

def testAdaugaCarte():
    lista=[]
    lista= adaugaCarte("1","Colt Alb", "aventura",15,"silver",lista)



    assert len(lista)== 1
    assert getId(getById("1",lista))=="1"
    assert getTitlu(getById("1",lista))=="Colt Alb"
    assert getGen(getById("1",lista))==15
    assert getPret(getById("1",lista))=="aventura"
    assert getTip_Reducere(getById("1",lista))=="silver"


    def testStergeCarte():
        lista=[]
        lista=adaugaCarte("1","Colt Alb", "aventura",15,"silver",lista)
        lista=adaugaCarte("2","Scufita Rosie", "aventura",15,"silver",lista)

        lista=stergeCarte("3",lista)

    assert len(lista)==1
    assert getById("1",lista) is None
    assert getById("2",lista) is not None

    try:
        lista=stergeCarte("3",lista)
        assert False
    except ValueError:
        assert len(lista)==1
        assert getById("2",lista) is not None
    except Exception:
        assert False

def testmodificaCarte():
    lista=[]
    lista=adaugaCarte("1","Colt Alb", "aventura",15,"silver",lista)
    lista=adaugaCarte("2","Scufita Rosie", "aventura",15,"silver",lista)
    lista=modificaCarte("1","Cine conduce lumea","drama",60,"gold",lista)

    carteUpdatata=getById("1",lista)
    assert getId(carteUpdatata)== "1"
    assert getTitlu(carteUpdatata)=="Cine conduce lumea"
    assert getGen(carteUpdatata)=="drama"
    assert getPret(carteUpdatata)==60
    assert getTip_Reducere(carteUpdatata)=="gold"

    carteNeupdatata=getById("2",lista)
    assert getId(carteNeupdatata)== "2"
    assert getTitlu(carteNeupdatata)=="Scufita Rosie"
    assert getGen(carteNeupdatata)=="aventura"
    assert getPret(carteNeupdatata)==15
    assert getTip_Reducere(carteNeupdatata)=="silver"

    lista=[]
    lista=adaugaCarte("1","Colt Alb", "aventura",15,"silver",lista)
    lista=modificaCarte("1","Cine conduce lumea","drama",60,"gold",lista)

    carteNeupdatata=getById("1",lista)
    assert getId(carteNeupdatata) == "1"
    assert getTitlu(carteNeupdatata) == "Cine conduce lumea"
    assert getGen(carteNeupdatata) == "fictiune"
    assert getPret(carteNeupdatata) == 60
    assert getTip_Reducere(carteNeupdatata) == "gold"


