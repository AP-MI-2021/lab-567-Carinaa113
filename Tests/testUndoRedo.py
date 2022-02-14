from Logic.CRUD import getById, adaugaCarte
from UI.console import undo,redo


def testUndoRedo():
    # 1
    lista = []
    undolist = []
    redolist = []
    # 2
    undolist.append(lista)
    redolist.clear()
    lista = adaugaCarte("1", "Scufita Rosie", "fantastica", 45, "silver", lista)

    # 3
    undolist.append(lista)
    redolist.clear()
    lista = adaugaCarte("2", "Comoara ascunsa", "romantica", 100, "gold", lista)

    # 4
    undolist.append(lista)
    redolist.clear()
    lista = adaugaCarte("3", "Arta Conversatiei", "drama", 28, "none", lista)

    assert len(lista) == 3

    # 5

    lista = undo(lista, undolist, redolist)
    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is not None
    assert getById('3', lista) is None

    # 6
    lista = undo(lista, undolist, redolist)
    assert len(lista) == 1
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None

    # 7
    lista = undo(lista, undolist, redolist)
    assert len(lista) == 0
    assert getById('1', lista) is None
    assert getById('2', lista) is None
    assert getById('3', lista) is None

    # 8

    assert len(lista) == 0
    assert getById('1', lista) is None
    assert getById('2', lista) is None
    assert getById('3', lista) is None

    # 9
    undolist.append(lista)
    redolist.clear()
    lista = adaugaCarte("1", "Scufita Rosie", "fantastica", 45, "silver", lista)

    undolist.append(lista)
    redolist.clear()
    lista = adaugaCarte("2", "Comoara ascunsa", "romantica", 100, "gold", lista)

    undolist.append(lista)
    redolist.clear()
    lista = adaugaCarte("3", "Arta Conversatiei", "drama", 28, "none", lista)

    # 10
    lista = redo(lista, undolist, redolist)
    assert len(lista) == 3
    assert getById('1', lista) is not None
    assert getById('2', lista) is not None
    assert getById('3', lista) is not None

    # 11
    lista = undo(lista, undolist, redolist)
    lista = undo(lista, undolist, redolist)

    assert len(lista) == 1
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None

    # 12

    lista = redo(lista, undolist, redolist)
    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is not None
    assert getById('3', lista) is None

    # 13

    lista = redo(lista, undolist, redolist)
    assert len(lista) == 3
    assert getById('1', lista) is not None
    assert getById('2', lista) is not None
    assert getById('3', lista) is not None

    # 14

    lista = undo(lista, undolist, redolist)
    lista = undo(lista, undolist, redolist)

    assert len(lista) == 1
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None

    # 15
    undolist.append(lista)
    redolist.clear()
    lista = adaugaCarte("4", "Arta Conversatiei", "drama", 28, "none", lista)

    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None
    assert getById('4', lista) is not None

    # 16
    lista = redo(lista, undolist, redolist)
    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None
    assert getById('4', lista) is not None

    # 17
    lista = undo(lista, undolist, redolist)
    assert len(lista) == 1
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None
    assert getById('4', lista) is None

    # 18
    lista = undo(lista, undolist, redolist)
    assert len(lista) == 0
    assert getById('1', lista) is None
    assert getById('2', lista) is None
    assert getById('3', lista) is None
    assert getById('4', lista) is None

    # 19
    lista = redo(lista, undolist, redolist)
    lista = redo(lista, undolist, redolist)
    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None
    assert getById('4', lista) is not None

    # 20
    lista = redo(lista, undolist, redolist)
    assert len(lista) == 2
    assert getById('1', lista) is not None
    assert getById('2', lista) is None
    assert getById('3', lista) is None
    assert getById('4', lista) is not None