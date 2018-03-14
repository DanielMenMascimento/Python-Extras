# Criar um algorítimo que:
# / Conte quantas pessoas foram cadastradas.
# / Conte quantos homens e quantas mulheres foram cadastrados
# / Mostre o homem e a mulher mais velhos
print('=' * 45)
print('{:-^45}'.format('={ While }='))
print('=' * 45)

cont = 1
homem = mulher = 0
homemMV = mulherMV = ' '
maiorIdadeH = maiorIdadeM = 0

while True:
    print('{:~^45}'.format(f'=[ Dados da {cont}° pessoa ]='))

    # Tratamento de erro para nome com menos de 3 caractéies
    while True:
        nome = str(input('Nome: ')).strip().title()
        if len(nome) < 3:
            print('\033[1;31mSeu nome deve no mínimo 3 caractéries!\033[m')
        else:
            break
    # =================================================

    # Tratamento de erro para idades menores que 0
    while True:
        idade = int(input('Idade: '))
        if idade > 0:
            break
        else:
            print('\033[1;31mIdade inválida!\033[m')
    # =================================================

    # Tratamento de erro para sexo diferente de M ou F
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('\033[1;31mOpção inválida!\033[m')
    # =================================================

    # Tratamento de erro para opção diferente de S ou N
    print('*' * 45)
    while True:
        fim = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

        if fim == 'S' or fim == 'N':
            break

    if fim == 'S':
        cont += 1

    else:
        break
    # =================================================

    if cont == 1 and sexo == 'M':
        homemMV = nome
        maiorIdadeH = idade


    if cont == 1 and sexo == 'F':
        mulherMV = nome
        maiorIdadeM = idade

    if sexo == 'M':
        homem += 1
        if idade > maiorIdadeH:
            homemMV = nome
            maiorIdadeH = idade

    if sexo == 'F':
        mulher += 1
        if idade > maiorIdadeM:
            mulherMV = nome
            menorIdadeM = idade

print('#' * 45)
print('\033[1;34m{:^45}\033[m'.format('Estatísticas'))
print(f'{cont} pessoas foram cadastradas')
print(f'{homem} homens sendo que {homemMV} é o homem mais velho')
print(f'{mulher} mulheres e {mulherMV} é a mulher mais velha')
