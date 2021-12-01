from Domain.cheltuiala import creeaza_cheltuiala, get_numar_apartament, get_data, get_suma, get_tipul


def test_cheltuiala():
    cheltuiala = creeaza_cheltuiala("13", 300, "23.02.2003", "electricitate")

    assert get_numar_apartament(cheltuiala) == "13"
    assert get_suma(cheltuiala) == 300
    assert get_data(cheltuiala) == "23.02.2003"
    assert get_tipul(cheltuiala) == "electricitate"
