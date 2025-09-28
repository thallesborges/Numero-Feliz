from numero_feliz import numero_feliz

while True:
    try:
        intervalo_inicial = int(input('♠ Insira o intervalo inicial X (X de Y): '))
        if intervalo_inicial <= 0:
            print('## Por favor, insira um número inteiro maior que 0.')
            continue
        intervalo_final = int(input(f'♠ Insira o intervalo final Y ({intervalo_inicial} de Y): '))
        if intervalo_final <= 0:
            print('## Por favor, insira um número inteiro maior que 0.')
            continue
        break
    except ValueError:
        print('## Por favor, insira um número inteiro válido.')

numeros_felizes = []
for i in range(intervalo_inicial, intervalo_final+1):
    resultado = numero_feliz(i)
    if resultado:
        numeros_felizes.append(i)

print(f'♠ Existem {len(numeros_felizes)} números felizes de {intervalo_inicial} a {intervalo_final}, são eles:')    
print(f'{' - '.join(str(n) for n in numeros_felizes)}')