from solution import quantos_comeram

def test_se_todos_comeram():
    assert quantos_comeram(30, [15, 6, 9]) == 30

def test_so_grupo1():
    assert quantos_comeram(10, [9, 5]) == 9

def test_so_grupo12():
    assert quantos_comeram(14, [9, 5, 1]) == 14

def test_ninguem():
    assert quantos_comeram(8, [9, 5, 1]) == 0

def test_so_grupo1():
    assert quantos_comeram(10, [9, 5]) == 9

def test_dois():
    assert quantos_comeram(5, [4, 2]) == 4

def test_nenhum_dos_dois():
    assert quantos_comeram(8, [10, 5, 3]) == 0
