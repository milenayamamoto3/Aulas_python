"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
digite_um_numero_inteiro = input('Digite um número inteiro: ')

try: 
    numero_inteiro = int(digite_um_numero_inteiro)
    if numero_inteiro % 2 == 0:
        print('Seu número é par')
    if numero_inteiro % 2 != 0:
        print('Seu número é ímpar')

except:
    print('Não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_user = input('Qual horário agora?')

try:
    hora_int = int(hora_user)
    if 0 <= hora_int <= 11:
        print('Bom dia')

    if 12 <= hora_int <= 17:
        print('Boa tarde')

    if 18 <= hora_int <= 23:
        print('Boa noite')

except: 
    print('Coloque apenas as horas')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome_user = input('Qual seu primeiro nome? ')

if 1 <= len(nome_user) <=4:
    print('Seu nome é curto')

if 5 <= len(nome_user) <= 6:
    print('Seu nome é normal')

if 6 < len(nome_user):
    print('Seu nome é muito grande')

else:
    print('Digite algo ou sem ser números')