from Domain.carte import creeazaCarte,getId,getTitlu,getTip_Reducere


def adaugaCarte(id,titlu,gen,pret,tip_reducere,lista):
    '''
    adauga o carte intr o lista
    :param id:string
    :param titlu:string
    :param gen:string
    :param pret:float
    :param tip_reducere:string
    :param lista:lista de carti
    :return:o lista continand elementele vechi si noua carte
    '''
    if getById(id,lista) is not None:
        raise ValueError("Id-ul exista deja!")
    carte=creeazaCarte(id,titlu,gen,pret,tip_reducere)
    if pret<0:
        raise ValueError("Pretul nu poate fi numar negativ!")
    return lista+[carte]

def getById(id,lista):
    '''
    da cartea cu id-ul dat dintr o lista
    :param id: string
    :param lista: lista de carti
    :return: cartea cu id ul dat din lista sau None daca aceasta nu exista
    '''
    for carte in lista:
        if getId(carte)==id:
            return carte
    return None

def getByTitlu(titlu,lista):
    '''

    :param titlu:
    :param lista:
    :return:
    '''
    for carte in lista:
        if getTitlu(carte)==titlu:
            return carte
        return None

def stergeCarte(id,lista):
    '''

    :param id:
    :param lista:
    :return:
    '''

    if getById(id,lista) is None:
        raise ValueError("Nu exista vreo carte cu id-ul dat!")
    return[carte for carte in lista if getId(carte) != id]



def modificaCarte(id,titlu,gen,pret,tip_reducere):
    '''
    modifica o prajitura dupa id
    :param id:
    :param titlu:
    :param gen:
    :param pret:
    :param tip_reducere:
    :return:
    '''

    if getById(id,lista) is None:
        raise ValueError("Nu exista vreo carteu id-ul dat!")
    listaNoua=[]
    for carte in lista:
        if getId(carte)==id:
            carte_noua==creeazaCarte(id,titlu,gen,pret,tip_reducere)
            listaNoua.append(carte_noua)
        else:
            listaNoua.append(carte)
    return listaNoua