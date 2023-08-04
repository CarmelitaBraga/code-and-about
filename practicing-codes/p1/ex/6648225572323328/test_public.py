from undertst import eh_quadrado_magico
    
def test_1():
    assert eh_quadrado_magico([[2, 7, 6], [9, 5, 1], [4, 3, 8]])

def test_2():
    assert not eh_quadrado_magico([[1, 2, 3], [4, 5, 6]])
