from Domain.carte import getId, getTitlu, getPret, getGen, getTip_Reducere, creeazaCarte


# reducerea pretului in functie de discountul aplicat
from Logic.CRUD import modificaCarte


def aplicareDiscount(lista):
    '''
    Aplicam un discount de 5% pentru reduceri silver si 10% pentru reduceri gold
    :param lista: lista de carti
    :return: noua lista de carti,modificata
    '''

    listaNoua = []
    for carte in lista:
        if getTip_Reducere(carte) == "silver":
            noua_vanzare = creeazaCarte(
                getId(carte),
                getTitlu(carte),
                getGen(carte),
                getPret(carte)-0.05*getPret(carte),
                getTip_Reducere(carte),
        )
            listaNoua.append(noua_vanzare)

        elif getTip_Reducere(carte) == "gold":
             noua_vanzare = creeazaCarte(
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


def modificareGen(titluNou, GenNou, lista):
    '''
    Modifica genul cartii
    :param titluNou:titlu cartii actuale
    :param GenNou:noul gen al cartii
    :param lista:lista de carti
    :return:genul modificat al cartii
    '''

    for carte in lista:
        id = getId(carte)
        titlu = getTitlu(carte)
        pret = getPret(carte)
        tip_reducere = getTip_Reducere(carte)
        if getTitlu(carte) == titluNou:
            lista = modificaCarte(id, titlu, GenNou, pret, tip_reducere, lista)
        else:
            pass
    return lista


def pretMin(lista):
    '''
    Determina pretul minim pentru fiecare gen
    :param lista:lista de carti
    :return:pretul minim pentru fiecare gen
    '''

    rezultat = {}#creeam un dictionar
    for carte in lista:
        gen = getGen(carte)
        pret = getPret(carte)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen] = pret
        else:
                rezultat[gen] = pret
    return rezultat


def ordonarePret(lista):
    '''
    Ordonarea cartilor dupa pret
    :param lista:
    :return: Cartile in functie de pret
    '''

    return sorted(lista, key=getPret)


def numarTitluri(lista):
   genuri = {}
   titluri = {}

   for carte in lista:
       titlu = getTitlu(carte)
       gen = getGen(carte)
       if titlu not in titluri:
           if gen in genuri:
              genuri[gen] = genuri[gen]+1
              titluri[titlu] = titlu
           else:
               genuri[gen] = 1
               titluri[titlu] = titlu
   return genuri


def doUndo(undolist, redolist, lista_curenta):
    '''
    Returneaza lista dupa un apel al functiei Undo
    :param undolist:lista listei de cheltuieli,modificata in urma unui apel al functionalitatii
    :param redolist:lista de liste care se modifica in urma fiecarui apel Undo
    :param lista_curenta:lista curenta de carti
    :return:lista noua ini urma apelului Undo
    '''
    if undolist:
        top_undo = undolist.pop()
        redolist.append(lista_curenta)
        return top_undo
    return None

def doRedo(undolist, redolist, listacurenta):
    '''
    Returneaza lista dupa un apel al functiei Redo
    :param undolist: Lista de liste de carti,ce se modifica in urma apeluluui unei functionalitati
    :param redolist: lista de liste care se modifica in urma unei apelari Undo
    :param listacurenta: lista actuala de carti
    :return: lista noua ce se obtine dupa Redo
    '''

    if redolist:
        top_redo = redolist.pop()
        undolist.append(listacurenta)
        return top_redo
    return None