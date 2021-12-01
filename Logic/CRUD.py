from Domain.cheltuiala import creeaza_cheltuiala, get_numar_apartament


def adauga_cheltuiala(numar_apartament, suma, data, tipul, lista):
      """
      adauga o cheltuiala intr-o lista
      :param numar_apartament: string
      :param suma: int
      :param data: string
      :param tipul: string
      :return: o lista continand elementele vechi cat si noua cheltuiala
      """
      cheltuiala = creeaza_cheltuiala(numar_apartament, suma, data, tipul)
      return lista + [cheltuiala]


def get_by_numar_apartament(numar_apartament, lista):
      """
      da cheltuiala cu numarul apartamentului dat
      :param numar_apartament: string
      :param lista: lista de cheltuieli
      :return: cheltuiala cu numarul apartamentului dat din lista sau None daca aceasta nu exista
      """
      for cheltuiala in lista:
            if get_numar_apartament(cheltuiala) == numar_apartament:
                  return cheltuiala
      return None


def sterge_cheltuiala(numar_apartament, lista):
      """
      sterge o cheltuiala cu numarul apartamentului dat
      :param numar_apartament: string
      :param lista: lista de chetuieli
      :return: lista de cheltuieli fara cheltuiala cu numarul apartamentului dat
      """
      return [cheltuiala for cheltuiala in lista if get_numar_apartament(cheltuiala) != numar_apartament]


def modifica_cheltuiala(numar_apartament, suma, data, tipul, lista):
      """
      modifica o cheltuiala dupa numar apartament
      :param numar_apartament: string
      :param suma: float
      :param data: string
      :param tipul: string
      :param lista: lista de cheltuieli
      :return: lista de cheltuieli modificata
      """
      lista_noua = []
      for cheltuiala in lista:
            if get_numar_apartament(cheltuiala) == numar_apartament:
                  cheltuiala_noua = creeaza_cheltuiala(numar_apartament, suma, data, tipul)
                  lista_noua.append(cheltuiala_noua)
            else:
                  lista_noua.append(cheltuiala)
      return lista_noua
