

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
    carte = creeazaCarte(id,titlu,gen,pret,tip_reducere)
    return lista + [carte]

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


def stergeCarte(id,lista):
    '''

    :param id:
    :param lista:
    :return:
    '''

    listaNoua=[]
    for carte in lista:
        if getId(carte) != id:
            listaNoua.append(carte)
    return listaNoua


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

    listaNoua=[]
    for carte in lista:
        if getId(carte)==id:
            carteNoua+ creeazaCarte(id,titlu,gen,pret,tip_reducere)
            listaNoua.append(carteNoua)
        else:
            listNoua.append(carte)
    return listaNoua
