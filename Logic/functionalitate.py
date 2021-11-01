from Domain.carte import getId,getTitlu,getPret,getGen,getTip_Reducere


# reducerea pretului in functie de discountul aplicat

def aplicareDiscount(id,titlu,gen,pret,tip_reducere,lista):
    '''
    Aplicam un discount de 5% pentru reduceri silver si 10% pentru reduceri gold
    :param lista: lista de carti
    :return: noua lista de carti,modificata
    '''


    for carte in lista:
        if getTip_Reducere(carte) == "Silver":
            pret_redus = getPret() - getPret() * 5/100

            # carteNoua = creeazaCarte(
            #     getId(carte),
            #     getTitlu(carte),
            #     getGen(carte),
            #     getPret(carte) * 5/100,
            #     getTip_Reducere(carte),
            # )


        elif getTip_Reducere(carte) == "Gold":
               pret_redus = getPret() - getPret() * 10/100
            #   carteNoua = creeazaCarte(
            #     getId(carte),
            #     getTitlu(carte),
            #     getGen(carte),
            #     getPret(carte) * 10/100,
            #     getTip_Reducere(carte),
            #     )

        else:
            return None



# redarea pretului nou in functie de gen

# def pretminim(lista):
#     '''
#     Dterminam pretul minim pentru fiecare gen
#     :param lista: lista cartilor
#     :return: pretul minim in functie de gen
#     '''
#     rezultat = {}
#     for carte in lista:
#         gen = getGen(carte)
#         pret = getPret(carte)
#         if gen in rezultat:
#             if pret < rezultat[gen]:
#                 rezultat[gen] = pret
#             else:
#                 rezultat[gen]
#     return rezultat
#
#
# # ordonare crescatoare in functie de pret
#
# def ordonareCrescatoare(lista):
#     '''
#     Ordonarea cartilor in functie de pret
#     :param lista: lista cartilor
#     :return: lista cartilor ordonata in functie de pret
#     '''
#
#     listanoua = sorted(lista, key=lambda carte: getPret(carte))
#     return listanoua
#
print(aplicareDiscount("1","Colt Alb", "aventura",15,"silver",lista))