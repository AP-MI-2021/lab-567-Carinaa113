from Logic.CRUD import adaugaCarte, stergeCarte, getById


def testUndoRedo():
    lista = []
    undoList = []
    redoList = []
    mesaje = []


    #o prima adaugare
    lista = adaugaCarte("1", "Legile Naturii", "actiune", 50, "silver", lista)
    undoList.append([
        lambda: stergeCarte("1",lista),
        lambda: adaugaCarte("1", "Legile Naturii", "actiune", 50, "silver", lista)
    ])
    redoList.clear()

    #o a doua adaugare
    lista = adaugaCarte("2", "Animalul Politic", "politica", 35, "none", lista)
    undoList.append([
        lambda: stergeCarte("2", lista),
        lambda: adaugaCarte("2", "Animalul Politic", "politica", 35, "none", lista)
    ])
    redoList.clear()

    lista = adaugaCarte("3", "Nunta in Cer", "romantica", 20, "gold", lista)
    undoList.append([
        lambda: stergeCarte("3",lista),
        lambda: adaugaCarte("3", "Nunta in Cer", "romantica", 20, "gold", lista)
    ])
    redoList.clear()
    assert len(lista) == 3

    #primul undo
    if len(undoList) > 0:
        mesaje = undoList.pop()
        redoList.append(mesaje)
        lista = mesaje[0]()
    else:
        pass
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is None

    #al doilea undo
    if len(undoList) > 0:
        mesaje = undoList.pop()
        redoList.append(mesaje)
        lista = mesaje[0]()
    else:
        pass
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None

    #al treilea undo
    if len(undoList) > 0:
        mesaje = undoList.pop()
        redoList.append(mesaje)
        lista = mesaje[0]()
    else:
        pass
    assert len(lista) == 0
    assert getById("1", lista) is None

    if len(undoList) > 0:
        mesaje = undoList.pop()
        redoList.append(mesaje)
        lista = mesaje[0]()
    else:
        pass
    assert len(lista) == 0

    lista = adaugaCarte("2", "Animalul Politic", "politica", 35, "none", lista)
    undoList.append([
        lambda: stergeCarte("2", lista),
        lambda: adaugaCarte("2", "Animalul Politic", "politica", 35, "none", lista)
    ])
    redoList.clear()

    lista = adaugaCarte("3", "Nunta in Cer", "romantica", 20, "gold", lista)
    undoList.append([
        lambda: stergeCarte("3", lista),
        lambda: adaugaCarte("3", "Nunta in Cer", "romantica", 20, "gold", lista)
    ])
    redoList.clear()
    assert len(lista) == 3

    #primul redo
    if len(redoList) > 0:
        mesaje = redoList.pop()
        undoList.append(mesaje)
        lista = mesaje[1]()
    else:
        pass
    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None

    #al 5 lea si al 6lea undo

    if len(undoList) > 0:
        mesaje = undoList.pop()
        redoList.append(mesaje)
        lista = mesaje[0]()
    else:
        pass
    if len(undoList) > 0:
        mesaje = undoList.pop()
        redoList.append(mesaje)
        lista = mesaje[0]()
    else:
        pass
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

    #al 2lea redo

    if len(redoList) > 0:
        mesaje = redoList.pop()
        undoList.append(mesaje)
        lista = mesaje[1]()
    else:
        pass
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is None

    #al 3lea redo

    if len(redoList) > 0:
        mesaje = redoList.pop()
        undoList.append(mesaje)
        lista = mesaje[1]()
    else:
        pass
    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None

    #al 7lea 8lea undo

    if len(undoList) > 0:
        mesaje = undoList.pop()
        redoList.append(mesaje)
        lista = mesaje[0]()
    else:
        pass
    if len(undoList) > 0:
        operations = undoList.pop()
        redoList.append(operations)
        lista = operations[0]()
    else:
        pass
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

    # al patrulea redo
    if len(redoList) > 0:
        mesaje = redoList.pop()
        undoList.append(mesaje)
        lista = mesaje[1]()
    else:
        pass
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is None

    #al
    #cincelea
    #redo


    if len(redoList) > 0:
        operations = redoList.pop()
        undoList.append(operations)
        lista = operations[1]()
    else:
        pass
    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None

    # noualea si al zecelea undo
    if len(undoList) > 0:
        mesaje = undoList.pop()
        redoList.append(mesaje)
        lista = mesaje[0]()
    else:
        pass
    if len(undoList) > 0:
        mesaje = undoList.pop()
        redoList.append(mesaje)
        lista = mesaje[0]()
    else:
        pass
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

    #a 7a adaugare

    lista = adaugaCarte("4", "Harry Potter", "science-fiction", 110, "silver", lista)
    undoList.append([
        lambda: stergeCarte("4", lista),
        lambda: adaugaCarte("4", "Harry Potter", "science-fiction", 110, "silver", lista)

    ])
    redoList.clear()
    assert len(lista) == 2

    # al saselea redo
    if len(redoList) > 0:
        mesaje = redoList.pop()
        undoList.append(mesaje)
        lista = mesaje[1]()
    else:
        pass
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is not None

    # al unsprezecelea undo
    if len(undoList) > 0:
        mesaje = undoList.pop()
        redoList.append(mesaje)
        lista = mesaje[0]()
    else:
        pass
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is None

    # al doisprezecelea undo
    if len(undoList) > 0:
        mesaje = undoList.pop()
        redoList.append(mesaje)
        lista = mesaje[0]()
    else:
        pass
    assert len(lista) == 0
    assert getById("1", lista) is None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is None

    # al saptelea si al optulea redo
    if len(redoList) > 0:
        mesaje = redoList.pop()
        undoList.append(mesaje)
        lista = mesaje[1]()
    else:
        pass
    if len(redoList) > 0:
        operations = redoList.pop()
        undoList.append(operations)
        lista = operations[1]()
    else:
        pass
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is not None

    # al noualea redo
    if len(redoList) > 0:
        mesaje = redoList.pop()
        undoList.append(mesaje)
        lista = mesaje[1]()
    else:
        pass
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None
    assert getById("4", lista) is not None









