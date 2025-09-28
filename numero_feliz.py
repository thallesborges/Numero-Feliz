def numero_feliz(numero):
    global resultados
    resultados = [] 
    ciclo = set()
    while True:
        digitos = [int(digito) for digito in str(numero)]
        resultado = sum(digito*digito for digito in digitos)
        resultados.append((digitos, resultado))
        
        if resultado == 1:
            return True
        
        if resultado in ciclo:
            return False

        ciclo.add(resultado)
        numero = resultado

if __name__ == '__main__':
    print('== Número Feliz ==')
    while True:
        try:
            valor = int(input('♦ Digite um número: '))
            if valor <= 0:
                print('# Por favor, insira um número inteiro maior que 0.')
                continue
            break
        except ValueError:
            print('# Por favor, insira um número inteiro válido.')
    
    if numero_feliz(valor):
        print(f'✅ {valor} é feliz, porque: ')
        for digito, resultado in resultados:
            print(f'{' + '.join(f'{d}²' for d in digito)} = {resultado}')
    else:
        print(f'❌ {valor} não é feliz, porque entra em um ciclo infinito: ')
        ciclo = ' -> '.join(str(resultado) for _, resultado in resultados)
        print(f'{valor} -> {ciclo}...')