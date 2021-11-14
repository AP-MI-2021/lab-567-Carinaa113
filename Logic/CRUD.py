
from Domain.carte import creeazaCarte, getId, getTitlu


def adaugaCarte(id, titlu, gen, pret, tip_reducere, lista):
    '''
    adauga o carte in lista
    :param id: int
    :param titlu: string
    :param gen: string
    :param pret: float
    :param tip_reducere: string
    :param lista: o lista ce retine cartile
    :return: o lista ce contine lista veche plus cartea adaugata
    '''

    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    carte = creeazaCarte(id, titlu, gen, pret, tip_reducere)
    return lista+[carte]

def getById(id, lista):#cautam in lista cartea cu id-ul deja introdus
    '''
    da cartea cu id-ul dat dintr o lista
    :param id: string
    :param lista: lista de carti
    :return: cartea cu id ul dat din lista sau None daca aceasta nu exista
    '''
    for carte in lista:
        if getId(carte) == id:
            return carte
    return None

def getByTitlu(titlu, lista):
    '''
    da cartea cu titlul dat dintr-o lista
    :param titlu:string
    :param lista:lista de carti
    :return:cartea cu titlul dat din lista sau None daca nu exista
    '''
    for carte in lista:
        if getTitlu(carte ) == titlu:
            return carte
        return None

def stergeCarte(id, lista):
    '''
    sterge o carte dupa id dintr o lista
    :param id:id ul cartii de sters
    :param lista:lista de carti
    :return:lista continand cartile cu id ul diferit de id
    '''

    if getById(id, lista) is None:
        raise ValueError("Nu exista vreo carte cu id-ul dat!")
    return[carte for carte in lista if getId(carte) != id]



def modificaCarte(id, titlu, gen, pret, tip_reducere, lista=None):
    '''
    modifica o prajitura dupa id
    :param id:
    :param titlu:
    :param gen:
    :param pret:
    :param tip_reducere:
    :return:
    '''

    if getById(id, lista) is None:
        raise ValueError("Nu exista vreo carte cu  id-ul dat!")
    listaNoua=[]
    for carte in lista:
        if getId(carte)==id:
            carte_noua=creeazaCarte(id,titlu,gen,pret,tip_reducere)
            listaNoua.append(carte_noua)
        else:
            listaNoua.append(carte)
    return listaNoua