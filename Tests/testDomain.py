from Domain.carte import creeazaCarte,getId,getTitlu,getPret,getGen,getTip_Reducere

def testCarte():

    carte = creeazaCarte("1","Colt Alb", "aventura",15,"silver")

    assert getId(carte)=="1"
    assert getTitlu(carte)=="Colt Alb"
    assert getGen(carte)==15
    assert getPret(carte)=="aventura"
    assert getTip_Reducere(carte)=="silver"