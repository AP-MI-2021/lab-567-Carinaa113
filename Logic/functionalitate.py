from Domain.carte import getId,getTitlu,getPret,getGen,getTip_Reducere,schimbareGen,creeazaCarte
from Logic.CRUD import getByTitlu


# reducerea pretului in functie de discountul aplicat

def aplicareDiscount(lista):
    '''
    Aplicam un discount de 5% pentru reduceri silver si 10% pentru reduceri gold
    :param lista: lista de carti
    :return: noua lista de carti,modificata
    '''

    listaNoua=[]
    for carte in lista:
        if getTip_Reducere(carte) == "silver":
            noua_vanzare=creeazaCarte(
                getId(carte),
                getTitlu(carte),
                getGen(carte),
                getPret(carte)-0.05*getPret(carte),
                getTip_Reducere(carte),
        )
            listaNoua.append(noua_vanzare)

        elif getTip_Reducere(carte)=="gold":
             noua_vanzare=creeazaCarte(
                 getId(carte),
                 getTitlu(carte),
                 getGen(carte),
                 getPret(carte)-0.1*getPret(carte),
                 getTip_Reducere(carte),

        )
             listaNoua.append(noua_vanzare)
        else:
              listaNoua.append(carte)
    return listaNoua


def modificareGen(titlu,GenNou,lista):
    '''
    Modifica genul cartii
    :param titlu:titlu cartii actuale
    :param GenNou:noul gen al cartii
    :param lista:lista de carti
    :return:genul modificat al cartii
    '''

    for carte in lista:
        if getTitlu(carte)==titlu:
            modificareGen(carte,GenNou)
        if getByTitlu(titlu,lista) is None:
            raise ValueError("Nu exista titlu dat!")


def pretMin(lista):
    '''
    Determina pretul minim pentru fiecare gen
    :param lista:lista de carti
    :return:pretul minim pentru fiecare gen
    '''

    rezultat={}#creeam un dictionar
    for carte in lista:
        gen=getGen(carte)
        pret=getPret(carte)
        if gen in rezultat:
            if pret<rezultat[gen]:
                rezultat[gen]=pret
        else:
                rezultat[gen]=pret
    return rezultat


def ordonarePret(lista):
    '''
    Ordonarea cartilor dupa pret
    :param lista:
    :return: Cartile in functie de pret
    '''

    return sorted(lista, key=getPret)

def numarTitluri(lista):
    '''
    Afisarea numarului de titluri distincte in functie de gen
    :param lista:
    :return: numarul de titluri diferite pentru fiecare gen in parte
    '''

   numar = 1
   rezultat={}
   for carte in lista:
       titlu=getTitlu(carte)
       gen=getGen(carte)
       if gen in rezultat:
           if titlu!= rezultat[gen]:
               numar=numar+1
               rezultat[gen]=numar
       else:
           rezultat[gen]=1
   return rezultat

