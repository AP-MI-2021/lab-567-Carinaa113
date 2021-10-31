#reducerea pretului in functie de discountul aplicat

def AplicareDiscount(lista):
    '''
    Aplicam un discount de 5% pentru reduceri silver si 10% pentru reduceri gold
    :param lista: lista de carti
    :return: noua lista de carti,modificata
    '''

    listanoua=[]
    for carte in lista:
        if getTip_Reducere(carte)=="Silver":
            carteNoua=creeazaCarte(
            getId(carte),
            getTitlu(carte),
            getGen(carte),
            getPret(carte)*19/20,
            getTip_Reducere(carte)
        )

          listanoua.append(carteNoua)
    elif  getTip_Reducere(carte)=="Gold":
         carteNoua=creeazaCarte(
             getId(carte),
             getTitlu(carte),
             getGen(carte),
             getPret(carte)*9/10,
             getTip_Reducere(carte)
         )
         listanoua.append(carteNoua)
    else
         listanoua.append(carte)

    return listanoua

#redarea pretului nou in functie de gen

def pretminim(lista):
    '''
    Dterminam pretul minim pentru fiecare gen
    :param lista: lista cartilor
    :return: pretul minim in functie de gen
    '''
    rezultat={}
    for carte in lista:
        gen=getGen(carte)
        pret=getPret(carte)
        if gen in rezultat:
            if pret<rezultat[gen]:
                rezultat[gen]=pret
            else:
                rezultat[gen]
    return rezultat

#ordonare crescatoare in functie de pret

def ordonareCrescatoare(lista):
    '''
    Ordonarea cartilor in functie de pret
    :param lista: lista cartilor
    :return: lista cartilor ordonata in functie de pret
    '''

    listanoua=sorted(lista,key=lambda carte:getPret(carte))
    return listanoua
