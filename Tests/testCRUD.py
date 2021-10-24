from Logic.CRUD import adaugaCarte,getById
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
