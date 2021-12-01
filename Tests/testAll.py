from Tests.testDomain import test_cheltuiala
from Tests.testCrud import test_adauga_cheltuiala, test_sterge_cheltuiala, test_modifica_cheltuiala


def run_all_tests():
    test_cheltuiala()
    test_adauga_cheltuiala()
    test_sterge_cheltuiala()
    test_modifica_cheltuiala()
