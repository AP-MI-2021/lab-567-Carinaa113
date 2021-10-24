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
    return{
        "id":id,
        "titlu":titlu,
        "gen":gen,
        "pret":pret,
        "tip_reducere":tip_reducere
    }

def getId(carte):
    '''
    da Id-ul cartii
    :param carte: un dictionar ce contine o carte
    :return: id ul cartii
    '''
    return carte["id"]

def getTitlu(carte):
    return carte["titlu"]

def getGen(carte):
    return carte["gen"]

def getPret(carte):
    return carte["pret"]

def getTip_Reducere(carte):
    return carte["tip_reducere"]


def toString(carte):
    return "Id:{},Titlu:{},  Gen:{} ,Pret:{}, Tip_Reducere:{}".format(
        getId(carte),
        getTitlu(carte),
        getGen(carte),
        getPret(carte),
        getTip_Reducere(carte)
    )

