from numero_feliz import numero_feliz

def test_numeros_felizes():
    verdadeiros = [1, 7, 10, 13, 19]
    for i in verdadeiros:
        assert numero_feliz(i) == True, f'Falhou para {i}'

def test_numeros_nao_felizes():
    falsos = [2, 3, 4, 5, 6]
    for i in falsos:
        assert numero_feliz(i) == False, f'Falhou para {i}'




