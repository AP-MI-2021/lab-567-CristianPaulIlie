def creeaza_cheltuiala(numar_apartament, suma, data, tipul):
    """""
    creeaza un dictionar ce reprezinta o cheltuiala
    :param numar_apartament: int
    :param suma: float
    :param data: string
    :param tipul: string
    :return: un dictionar ce contine o cheltuiala
    """
    return {
        "numar_apartament": numar_apartament,
        "suma": suma,
        "data": data,
        "tipul": tipul,
    }


def get_numar_apartament(cheltuiala):
    """
    da numarul apartamentului care a facut cheltuiala
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: numarul apartamentului care a realizat cheltuiala
    """
    return cheltuiala["numar_apartament"]


def get_suma(cheltuiala):
    return cheltuiala["suma"]


def get_data(cheltuiala):
    return cheltuiala["data"]


def get_tipul(cheltuiala):
    return cheltuiala["tipul"]


def to_string(cheltuiala):
    return "Numarul apartamentului: {}, Suma: {}, Data: {}, Tipul: {}".format(
    get_numar_apartament(cheltuiala),
    get_suma(cheltuiala),
    get_data(cheltuiala),
    get_tipul(cheltuiala),
    )
