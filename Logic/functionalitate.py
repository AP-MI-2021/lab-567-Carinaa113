#reducerea pretului in functie de discountul aplicat
def reducere(lista):
    listaNoua=[]
    for carte in lista :
        if getTip_Reducere(carte)=="silver":
            cartenoua=creeazaCarte(
                getId(carte),
                getTitlu(carte),
                getGen(carte),
                getPret(carte)*0,95,
                getTip_Reducere(carte)
            )
            listaNoua.append(cartenoua)
        elif getTip_Reducere(carte)=="gold":
             cartenoua=creeazaCarte(
                 getId(carte),
                 getTitlu(carte),
                 getGen(carte),
                 getPret(carte)*0.90,
                 getTip_Reducere(carte)
             )
            listaNoua.append(cartenoua)
        else
            listaNoua.append(carte)
        return listaNoua

#Modificarea genului pentru un titlu dat.

def modificGenul(gennou,titlu,lista):
    lnoua=[]
    for carte in lista:
        if titlu==getTitlu(lista):
           listanoua=creeazaCarte(
                 getId(carte),
                 getTitlu(carte),
                 getGen(carte),
                 getPret(carte),
                 getTip_Reducere(carte)
             )
           lnoua.append(listanoua)
        else:
           lnoua.append(carte)
    return lnoua

# Ordonarea vânzărilor crescător după preț.

