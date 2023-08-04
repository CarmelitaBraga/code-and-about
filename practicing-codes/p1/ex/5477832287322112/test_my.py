from undertst import le_cod

def test_codigo1():
    assert le_cod('012pessoal', 'oi sdfgh') == 'oi pessoal'

def test_codigo2():
    assert le_cod('987654321tah dah', 'kkk') == '987654321tah dah'
