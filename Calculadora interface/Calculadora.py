
numero1 = int(input('Digite o primeiro numero'))
numero2 = int(input('Digite o segundo numero'))
operador = input('Escolha o operador (+,-,*,/)')
todos = numero1, numero2, operador



while True:
    if operador == '-':
        resultadomenos = numero1 - numero2
        print('O Resultado da Subtração é:', resultadomenos)
    elif operador == '+':
        resultadomais = numero1 + numero2
        print('O Resultado da Soma é:', resultadomais)
    elif operador == '*':
        resultadovezes = numero1 * numero2
        print('O Resultado da multiplicação é:', resultadovezes)
    elif operador == '/':
        resultadodizes = numero1 / numero2
        print('O Resultado da divisão é:', resultadodizes)
    else:
        print('Operador invalido, digite novamente :/')
    break

