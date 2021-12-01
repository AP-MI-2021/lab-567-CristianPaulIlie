from Domain.cheltuiala import to_string
from Logic.CRUD import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala


def print_menu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala")
    print("3. Modificare cheltuiala")
    print("a. Afisare cheltuiala")
    print("x. Iesire")


def ui_adauga_prajitura(lista):
    numar_apartament = input("Dati numarul apartamentului:")
    suma = float(input("Dati suma: "))
    data = input("Dati data cand s-a efectuat cheltuiala: ")
    tipul = input("Dati tipul cheltuielii: ")
    return adauga_cheltuiala(numar_apartament, suma, data, tipul, lista)


def ui_sterge_chetuiala(lista):
    numar_apartament = input("Dati numarul apartamentului: ")
    return sterge_cheltuiala(numar_apartament, lista)


def ui_modifica_cheltuiala(lista):
    numar_apartament = input("Dati numarul apartamentului al carei cheltuiala trebuie modificata:")
    suma = float(input("Dati noua suma: "))
    data = input("Dati noua data cand s-a efectuat cheltuiala: ")
    tipul = input("Dati noul tip al cheltuielii: ")
    return modifica_cheltuiala(numar_apartament, suma, data, tipul, lista)


def show_all(lista):
    for cheltuiala in lista:
        print(to_string(cheltuiala))


def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = ui_adauga_prajitura(lista)
        elif optiune == "2":
            lista = ui_sterge_chetuiala(lista)
        elif optiune == "3":
            lista = ui_modifica_cheltuiala(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

