num1 = int(input('Num 1: '))
num2 = int(input('Num 2: '))
print('''[ 1 ] Somar
[ 2 ] Subtrair
[ 3 ] Multiplicar
[ 4 ] Dividir
[ 5 ] Maior
[ 6 ] Novos números
[ 7 ] Sair do programa''')
operacao = int(input('O que deseja fazer: '))

while operacao != 7:
    print('-=-' * 5)
    if operacao == 1:
        resultado = num1 + num2
        print('{} + {} = {}'.format(num1, num2, resultado))
    elif operacao == 2:
        resultado = num1 - num2
        print('{} - {} = {}'.format(num1, num2, resultado))
    elif operacao == 3:
        resultado = num1 * num2
        print('{} x {} = {}'.format(num1, num2, resultado))
    elif operacao == 4:
        resultado = num1 / num2
        print('{} ÷ {} = {}'.format(num1, num2, resultado))
    elif operacao == 5:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num2 > num1:
            print('{} é maior que {}'.format(num2, num1))
        else:
            print('{} é igual a {}'.format(num1, num2))
    elif operacao == 6:
        num1 = int(input('Num 1: '))
        num2 = int(input('Num 2: '))
    print('-=-' * 5)
    print('''[ 1 ] Somar
[ 2 ] Subtrair
[ 3 ] Multiplicar
[ 4 ] Dividir
[ 5 ] Maior
[ 6 ] Novos números
[ 7 ] Sair do programa''')
    operacao = int(input('O que deseja fazer: '))
