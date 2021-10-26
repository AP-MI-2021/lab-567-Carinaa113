#reducerea pretului in functie de discountul aplicat
def reducere(lista):
    listanoua=[]
    for carte in lista :
        if getTip_Reducere(carte)=="silver":
            cartenoua=creeazaCarte(
                getId(carte),
                getTitlu(carte),
                getGen(carte),
                getPret(carte)*0,95,
                getTip_Reducere(carte)
            )
            listanoua.append(cartenoua)
        elif getTip_Reducere(carte)=="gold":
             cartenoua=creeazaCarte(
                 getId(carte),
                 getTitlu(carte),
                 getGen(carte),
                 getPret(carte)*0.90,
                 getTip_Reducere(carte)
             )
            listanoua.append(cartenoua)
        else
            listanoua.append(carte)
        return listanoua

#Modificarea genului pentru un titlu dat.

def modificGenul(gennou,titlu,lista):
    listan=[]
    for carte in lista:
        if titlu==getTitlu(lista):
    return carte