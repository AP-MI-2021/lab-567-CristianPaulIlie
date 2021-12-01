from Domain.cheltuiala import get_numar_apartament, get_suma, get_tipul, get_data
from Logic.CRUD import adauga_cheltuiala, get_by_numar_apartament, sterge_cheltuiala, modifica_cheltuiala


def test_adauga_cheltuiala():
    lista = []
    lista = adauga_cheltuiala("13", 300, "23.02.2020", "electricitate", lista)

    assert len(lista) == 1
    assert get_numar_apartament(get_by_numar_apartament("13", lista)) == "13"
    assert get_suma(get_by_numar_apartament("13", lista)) == 300
    assert get_data(get_by_numar_apartament("13", lista)) == "23.02.2020"
    assert get_tipul(get_by_numar_apartament("13", lista)) == "electricitate"


def test_sterge_cheltuiala():
    lista = []
    lista = adauga_cheltuiala("13", 300, "23.02.2020", "electricitate", lista)
    lista = adauga_cheltuiala("81", 565, "12.11.2021", "gaz", lista)
    lista = sterge_cheltuiala("13", lista)

    assert len(lista) == 1
    assert get_by_numar_apartament("13", lista) is None
    assert get_by_numar_apartament("81", lista) is not None


def test_modifica_cheltuiala():
    lista = []
    lista = adauga_cheltuiala("13", 300, "23.02.2020", "electricitate", lista)
    lista = modifica_cheltuiala("13", 350, "23.02.2020", "electricitate", lista)

    assert len(lista) == 1
    assert get_numar_apartament(get_by_numar_apartament("13", lista)) == "13"
    assert get_suma(get_by_numar_apartament("13", lista)) == 350
    assert get_data(get_by_numar_apartament("13", lista)) == "23.02.2020"
    assert get_tipul(get_by_numar_apartament("13", lista)) == "electricitate"