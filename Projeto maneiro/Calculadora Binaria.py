escolha = None

while escolha != "8":
    print("==========================================")
    print("Calculadora Binária e Octal")
    print("==========================================")
    print("1 - Converter binário para decimal \n")
    print("2 - Converter decimal para binário \n")
    print("3 - Converter binário para octal \n")
    print("4 - Converter octal para binário \n")
    print("5 - Somar os dois números binários \n")
    print("6 - Subtrair dois números binários \n")
    print("7 - Multiplicar dois números binários \n")
    print("8 - Sair ")
    print("==========================================")
    escolha = input("Escolha uma opção:")

    if escolha == "1":
        binario = int(input("Digite um número binário: "))
        decimal = 0
        potencia = 0
        while binario != 0:
            decimal += (binario % 10) * (2 ** potencia)
            binario //= 10
            potencia += 1
        print("Decimal equivalente:", decimal)

    elif escolha == "2":
        decimal = int(input("Digite um número decimal: "))
        binario = ""
        while decimal != 0:
            binario = str(decimal % 2) + binario
            decimal //= 2
        print("Binário equivalente:", binario)

    elif escolha == "3":
        binario = int(input("Digite um número binário: "))
        decimal = 0
        potencia = 0
        while binario != 0:
            decimal += (binario % 10) * (2 ** potencia)
            binario //= 10
            potencia += 1
        octal = ""
        while decimal != 0:
            octal = str(decimal % 8) + octal
            decimal //= 8
        print("Octal equivalente:", octal)

    elif escolha == "4":
        octal = int(input("Digite um número octal: "))
        decimal = 0
        potencia = 0
        while octal != 0:
            decimal += (octal % 10) * (8 ** potencia)
            octal //= 10
            potencia += 1
        binario = ""
        while decimal != 0:
            binario = str(decimal % 2) + binario
            decimal //= 2
        print("Binário equivalente:", binario)

    elif escolha == "5":
        bin1 = int(input("Digite o primeiro número binário: "))
        bin2 = int(input("Digite o segundo número binário: "))
        decimal1 = 0
        potencia = 0
        while bin1 != 0:
            decimal1 += (bin1 % 10) * (2 ** potencia)
            bin1 //= 10
            potencia += 1
        decimal2 = 0
        potencia = 0
        while bin2 != 0:
            decimal2 += (bin2 % 10) * (2 ** potencia)
            bin2 //= 10
            potencia += 1
        resultado_decimal = decimal1 + decimal2
        resultado_binario = ""
        while resultado_decimal != 0:
            resultado_binario = str(resultado_decimal % 2) + resultado_binario
            resultado_decimal //= 2
        print("Resultado da soma:", resultado_binario)

    elif escolha == "6":
        bin1 = int(input("Digite o primeiro número binário: "))
        bin2 = int(input("Digite o segundo número binário: "))
        decimal1 = 0
        potencia = 0
        while bin1 != 0:
            decimal1 += (bin1 % 10) * (2 ** potencia)
            bin1 //= 10
            potencia += 1
        decimal2 = 0
        potencia = 0
        while bin2 != 0:
            decimal2 += (bin2 % 10) * (2 ** potencia)
            bin2 //= 10
            potencia += 1
        resultado_decimal = decimal1 - decimal2
        resultado_binario = ""
        while resultado_decimal != 0:
            resultado_binario = str(resultado_decimal % 2) + resultado_binario
            resultado_decimal //= 2
        print("Resultado da subtração:", resultado_binario)

    elif escolha == "7":
        bin1 = int(input("Digite o primeiro número binário: "))
        bin2 = int(input("Digite o segundo número binário: "))
        decimal1 = 0
        potencia = 0
        while bin1 != 0:
            decimal1 += (bin1 % 10) * (2 ** potencia)
            bin1 //= 10
            potencia += 1
        decimal2 = 0
        potencia = 0
        while bin2 != 0:
            decimal2 += (bin2 % 10) * (2 ** potencia)
            bin2 //= 10
            potencia += 1
        resultado_decimal = decimal1 * decimal2
        resultado_binario = ""
        while resultado_decimal != 0:
            resultado_binario = str(resultado_decimal % 2) + resultado_binario
            resultado_decimal //= 2
        print("Resultado da multiplicação:", resultado_binario)

    elif escolha == "8":
        print("Saindo...")
        break