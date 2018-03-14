# Teste de quociente de inteligência emocional
# By: Daniel Mendes do Nascimento (14/03/2018)
divisao = '-' * 125
erro = '\033[1;31m-x\033[m' * 62
total = 0
print('=-=' * 41)
print('* As questões a seguir mostrarão a média do seu Quociente de Inteligência Emocional (QE).')
print('* Responda com base no que você faria na realidade da situação proposta, não há uma melhor resposta.')
print('=-=' * 41)
print('\033[1;30m{:^125s}\033[m\n'.format('Teste de quociente de inteligência emocional (QIE)'))

# 1 ====================================================================================================================
while True:
    print(divisao)
    print('''
    1°) Você está viajando de avião. De repente, entra numa área de grande turbulência e começa a balançar de um lado para o
        outro. O que você faz?\n
    a)	Continua a ler o livro, o jornal ou a ver o filme, prestando pouca atenção à turbulência.
    b)	Fica de prontidão para uma emergência, cuidadosamente olha na tripulação e lê o cartão de instruções de emergência.
    c)	Um pouco de ambos (a e b).
    d)	Não tem certeza, nunca prestou atenção
    ''')
    r1 = str(input('\033[1;30mResposta:\033[m ')).upper().strip()[0]
    if r1 in 'ABC':
        total += 20
        break
    elif r1 == 'D':
        r1 += 0
        break
    elif r1 not in 'ABCD':
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        print(erro)
print(divisao)
# 2 ====================================================================================================================
while True:
    print('''
    2°) Você leva a um parque um grupo de crianças de quatro anos de idade, e uma delas começa a chorar porque as outras não
        querem brincar com ela. O que você faz?\n
    a)	Não dá bola, deixa as crianças resolverem sozinhas.
    b)	Conversa com a criança e a ajuda a “bolar” meios para que as outras brinquem com ela.
    c)	Fala para ela não chorar, em um tom meigo.
    d)	Tenta distrair a chorona, mostrando outras coisas com as quais ela poderia brincar.
    ''')
    r2 = str(input('\033[1;30mResposta:\033[m ')).upper().strip()[0]
    if r2 == 'B':
        total += 20
        break
    elif r2 in 'ACD':
        total += 0
        break
    elif r2 not in 'ABCD':
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        print(erro)
print(divisao)
# 3 ====================================================================================================================
while True:
    print('''
    3°) Suponha que você é um estudante universitário que esperava tirar nota 10 (dez), mas acabou de saber que obteve um
        4 (quatro). O que você faz?\n
    a)	Traça um plano específico para melhorar sua nota e resolve seguir o plano.
    b)	Resolve fazer melhor na próxima vez.
    c)	Diz a você mesmo que não importa como você foi de nota no curso e se concentra em aulas onde suas notas
        são mais altas.
    d)	Procura o professor e tenta falar com ele para aumentar sua nota.
    ''')
    r3 = str(input('\033[1;30mResposta:\033[m ')).upper().strip()[0]
    if r3 == 'A':
        break
    elif r3 in 'BCD':
        break
    elif r3 not in 'ABCD':
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        print(erro)
print(divisao)
# 4 ====================================================================================================================
while True:
        print('''
        4°) Imagine que você é um vendedor de seguros contatando possíveis clientes. Quinze pessoas contatadas de uma vez 
            desligaram o telefone na sua cara, e você está ficando desencorajado. O que faz?\n
        a)	Para e espera ter mais sorte no dia seguinte.
        b)	Avalia possíveis características suas que possam estar prejudicando sua capacidade de fazer a venda.
        c)	Experimenta nova abordagem no telefonema seguinte e continua tentando.
        d)	Pensa que é melhor mudar de trabalho.
        ''')
        r4 = str(input('\033[1;30mResposta:\033[m ')).upper().strip()[0]
        if r4 == 'C':
            total += 20
            break
        elif r4 in 'ABD':
            total += 0
            break
        elif r4 not in 'ABCD':
            print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
            print(erro)
print(divisao)
# 5 ====================================================================================================================
while True:
    print('''
    5°) Você é um gerente em uma organização que está tentando incentivar o respeito pela diversidade racial e étnica. 
        Você ouve alguém contar uma piada racista. O que você faz?\n
    a)	Ignora a piada, afinal, é apenas uma brincadeira.
    b)	Chama a pessoa a seu escritório para uma repreensão.
    c)	Fala na hora que tais piadas são inapropriadas e não serão toleradas na sua organização.
    d)	Sugere à pessoa que contou a piada que faça um programa de treinamento sobre diversidade racial.
    ''')
    r5 = str(input('\033[1;30mResposta:\033[m ')).upper().strip()[0]
    if r5 == 'C':
        total += 20
        break
    elif r5 in 'ABD':
        total += 0
        break
    elif r5 not in 'ABCD':
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        print(erro)
print(divisao)
# 6 ====================================================================================================================
while True:
    print('''
    6°) Você está tentando acalmar um amigo que estava furioso com um motorista que quase bateu no carro dele, tirando uma 
        “fina” em alta velocidade. O que você faz?\n
    a)	Diz a ele para esquecer, ele agora está bem e afinal não aconteceu nada.
    b)	Coloca uma música, ou aumenta o som do rádio e tenta distrai-lo.
    c)	Junta-se a ele na desqualificação do outro motorista, como prova de solidariedade.
    d)	Diz a ele que uma vez algo semelhante aconteceu com você e que ficou tão furioso quanto ele está agora, mas aí você 
        viu que o outro motorista estava a caminho do Pronto-Socorro.
    ''')
    r6 = str(input('\033[1;30mResposta:\033[m ')).upper().strip()[0]
    if r6 == 'D':
        total += 20
        break
    elif r6 in 'BC':
        total += 5
        break
    elif r6 == 'A':
        total += 0
        break
    elif r6 not in 'ABCD':
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        print(erro)
print(divisao)
# 7 ====================================================================================================================
while True:
    print('''
    7°) Você e seu parceiro(a) (namorado(a), marido/esposa, companheiro(a) etc.) entram numa discussão que evoluiu para uma 
        gritaria desafiadora; vocês estão desapontados e no auge da discussão, e não gostariam de fazer ataques pessoais. 
        Qual a melhor coisa a fazer?\n
    a)	Parar por uns 20 minutos e depois continuar a discussão.
    b)	Parar a discussão e ficar em silêncio, não importa o que o outro disser.
    c)	Pedir desculpas e pedir para o outro se desculpar também.
    d)	Parar por um momento, refletir um pouco, e então dar a sua opinião de forma clara e precisa.
    ''')
    r7 = str(input('\033[1;30mResposta:\033[m ')).upper().strip()[0]
    if r7 == 'A':
        total += 20
        break
    elif r7 in 'BCD':
        total += 0
        break
    elif r7 not in 'ABCD':
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        print(erro)
print(divisao)
# 8 ====================================================================================================================
while True:
    print('''
    8°) Você foi indicado para chefiar um grupo que está tentando uma solução para um problema de trabalho. Qual a primeira
        coisa a fazer?\n
    a)	Pegar uma agenda e alocar tempo para discutir cada item de forma a fazer o melhor uso possível do seu tempo junto 
        com os outros.
    b)	Fazer com que o pessoal do grupo gaste algum tempo para que se conheçam melhor.
    c)	Começar perguntando para cada pessoa por ideias sobre como resolver o problema, enquanto as ideias estão “frescas”
        na cabeça do pessoal.
    d)	Começar com uma sessão de discussão aberta, sem restrições, encorajando cada uma a falar o que vem à mente, 
        não importando quão estranho possa parecer.
    ''')
    r8 = str(input('\033[1;30mResposta:\033[m ')).upper().strip()[0]
    if r8 == 'A':
        total += 20
        break
    elif r8 in 'BCD':
        total += 0
        break
    elif r8 not in 'ABCD':
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        print(erro)
print(divisao)
# 9 ====================================================================================================================
while True:
    print('''
    9°) O seu filho de três anos de idade é extremamente tímido, e tem se mostrado muito hipersensível sobre isso e meio 
        amedrontado em relação a lugares e pessoas novas, desde que nasceu. O que você faz?\n
    a)	Aceita que seu temperamento é retraído e procura formas de protegê-lo de situações que o perturbem.
    b)	Leva seu filho a um psiquiatra infantil para ajuda.
    c)	Leva propositadamente seu filho a conhecer uma porção de pessoas e lugares de forma que ele possa superar seus medos.
    d)	“Bola” um programa de experiências desafiadoras, porém administráveis, para que ele aprenda que é capaz de lidar com
        locais e pessoas que não conhece.
    ''')
    r9 = str(input('\033[1;30mResposta:\033[m ')).upper().strip()[0]
    if r9 == 'D':
        total += 20
        break
    elif r9 == 'B':
        total += 5
        break
    elif r9 in 'AC':
        total += 0
        break
    elif r9 not in 'ABCD':
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        print(erro)
print(divisao)
# 10 ===================================================================================================================
while True:
    print('''
    10°) Durante vários anos você gostaria de voltar a aprender a tocar um instrumento que tentou tocar quando era criança, 
        e agora vai finalmente começar, só por diversão. Porém, você quer usar seu tempo de forma eficiente e eficaz. 
        O que você deve fazer?\n
    a)	Reservar diariamente um horário para praticar o instrumento.
    b)	Escolher peças que desenvolvam, de cada vez, um pouco mais a habilidade que você tem.
    c)	Praticar somente quando dá vontade.
    d)	Escolher peças que estão muito além da sua habilidade, mas que você é capaz de aprender com muito esforço.
    ''')
    r10 = str(input('\033[1;30mResposta:\033[m ')).upper().strip()[0]
    if r10 == 'B':
        total += 20
        break
    elif r10 in 'ACD':
        total += 0
        break
    elif r10 not in 'ABCD':
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        print(erro)
print(divisao)

print('\033[34m{}\033[m'.format('=' * 125))
print('\033[1;30m{:^125}\033[m'.format('Resultado'))
print('\033[34m{}\033[m'.format('=' * 125), end='\n')

print(f'Sua pontuação total foi de {total}, o que da à você a classificação de: ', end='')
if total <= 24:
    print('\033[31mNascendo para a vida\033[m')
if total >= 25 and total <= 49:
    print('\033[31mHomem das cavernas\033[m')
if total >= 50 and total <= 74:
    print('\033[32mPrepare-se para um desafio emocional\033[m')
if total >= 75 and total <= 99:
    print('\033[32mPsicoterapia (já pensou nisso?)\033[m')
if total >= 100 and total <= 124:
    print('\033[33mMÉDIA - equilibrado\033[m')
if total >= 125 and total <= 149:
    print('\033[33mUm Freud - um psicanalista\033[m')
if total >= 150 and total <= 174:
    print('\033[33mUm Gandhi - um líder\033[m')
if total >= 175 and total <= 199:
    print('\033[34mO empático\033[m')
if total >= 200:
    print('\033[34mGênio do QIE\033[m')

# Tabela de pontuação
while True:
    tabela = str(input('Quer ver a tabela de pontuação[S/N]: ')).upper().strip()[0]
    if tabela == 'S':
        print('''
0  - 24 Nascendo para a vida
25 - 49	Homem das cavernas
50 - 74	Prepare-se para um desafio emocional
75 - 99	Psicoterapia (já pensou nisso?)
100-124	MÉDIA - equilibrado
125-149	Um Freud - um psicanalista
150-174 Um Gandhi - um líder
175-199 O empático
200 	Gênio do QIE
        ''')
        break
    elif tabela == 'N':
        break
    elif tabela not in 'SN':
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        print(erro)

# Gabarito
print('\033[34m{}\033[m'.format('=' * 125))
while True:
    gabarito = str(input('Quer ver o gabarito[S/N]: ')).upper().strip()[0]
    if gabarito == 'S':
        print('Cada nota certa vale 20pts')
        print('''
1   = A B C estão certas
2   = B
3   = A
4   = C
5   = C
6   = D está certa, mas B e C contam 25% corretas
7   = A
8   = A
9   = D
10  = B
        ''')
        break
    elif gabarito == 'N':
        break
    elif gabarito not in 'SN':
        print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        print(erro)
print('\033[34m{}\033[m'.format('=' * 125))

# Fonte: Ciências Humanas - Perspectivas Profissionais pág.: 145 - 149 (UNIASSELVI, Mar - 2018)