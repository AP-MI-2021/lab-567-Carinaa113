def creeazaCarte(id,titlu,gen,pret,tip_reducere):
    '''
    creeaza un dictionar ce reprezinta o carte
    :param id:string
    :param titlu:string
    :param gen:string
    :param pret:float
    :param tip_reducere:string
    :return:un dictionar ce contine o carte
        '''

    list=[id,titlu,gen,pret,tip_reducere]

    return list



def getId(carte):
    '''
    da Id-ul cartii
    :param carte: un dictionar ce contine o carte
    :return: id ul cartii
    '''
    return carte[0]

def getTitlu(carte):
    return carte[1]

def getGen(carte):
    return carte[2]

def getPret(carte):
    return carte[3]

def getTip_Reducere(carte):
    return carte[4]


def toString(carte):
    return "Id:{},Titlu:{},  Gen:{} ,Pret:{}, Tip_Reducere:{}".format(
        getId(carte),
        getTitlu(carte),
        getGen(carte),
        getPret(carte),
        getTip_Reducere(carte)
    )

