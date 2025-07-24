import math
import statistics 
# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# x = input("Digite um numero: ")
# y = input("Digite outro numero: ")
# print(f"Os numeros digitados sao: {x} e {y}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# x = int(input("Digite o numero que sera dividido por 5: "))
# print(f"O resto da divisao do numero que voce digitou ({x}) eh : {(x % 5)}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# x = int(input("Digite um numero: "))
# y = int(input("Digite outro numero: "))
# print(f"O produto de {x} e {y} eh: {(x * y)}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# x = int(input("Digite um numero: "))
# y = int(input("Digite outro numero: "))
# print(f"A divisiao inteira de {x} por {y} eh: {(x // y)}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# x = int(input("Digite o numero: "))
# print(f"O quadrado de ({x}) eh : {(x ** 2)}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# x = float(input("Digite um numero: "))
# y = float(input("Digite outro numero: "))
# print(f"A soma de {x} e {y} eh: {(x + y)}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# x = float(input("Digite um numero: "))
# y = float(input("Digite outro numero: "))
# print(f"A media de {x} e {y} eh: {statistics.mean([x, y])}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# x = int(input("Digite um numero: "))
# y = int(input("Digite outro numero: "))
# print(f"A potencia de {x} elevado a {y} eh: {math.pow(x,y)}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# cel = float(input("Digite a temperatura em Celsius que deseja converter para Fahrenheit: "))
# far = (cel * 9/5) + 32
# print(f"A temperatura de {cel}ºC em Fahrenheit eh: {far}ºF")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio_do_circulo = float(input("Digite o valor do raio: "))
# area_do_circulo = math.pi * raio_do_circulo ** 2
# print(f'A area do circulo eh: {area_do_circulo:.2f}')


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# string = str(input("Digite a string que deseja converter: "))
# print(f"O resultado da conversao eh: {string.upper()}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# string = str(input("Digite seu nome completo: "))
# print(f"O resultado da conversao eh: {string.lower()}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# string = str(input("Digite seu nome completo: "))
# print(f'O resultado sem espacos do lado direito eh: >',string.rstrip(),'<')
# print(f'O resultado sem espacos do lado esquerdo eh: >',string.lstrip(),'<')

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# lista = input("Insira uma data no formato dd/mm/aaaa: ").split('/')
# print(f'O dia eh {lista[0]}, o mes eh {lista[1]} e o ano eh {lista[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# string1 = str(input("Digite a primeira string: "))
# string2 = str(input("Digite a segunda string: "))
# frase = (string1, " ", string2)
# print(f'A concatenacao das duas strings eh: {"".join(frase)}')


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# opr1 = eval(input("Digite a primeira operacao: "))
# opr2 = eval(input("Digite a segunda operacao: "))
# print(f'O resultado da operacao and eh: {opr1 and opr2}')

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# opr1 = eval(input("Digite a primeira operacao: "))
# opr2 = eval(input("Digite a segunda operacao: "))
# print(f'O resultado da operacao or eh: {opr1 or opr2}')

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# valor = bool(input("Digite um valor(True/False): "))
# print(f' O valor invetido eh: {not valor}')

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# valor1 = input("Digite o primeiro valor: ")
# valor2 = input("Digite o segundo valor: ")

# if valor1 == valor2:
#     resultado = "sao iguais"
# else:
#     resultado = "sao diferentes"

# print(f'Os valores {resultado}')


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# valor1 = input("Digite o primeiro valor: ")
# valor2 = input("Digite o segundo valor: ")

# if valor1 == valor2:
#     resultado = "sao iguais"
# else:
#     resultado = "sao diferentes"

# print(f'Os valores {resultado}')


# #### try-except e if

# 21: Conversor de Temperatura


# try:

#     temp = float(input("Digite o valor da temperatura: "))
#     medida = input("Digite a unidade de medida(C/F):").upper()

#     if medida == "C":
#         far = (temp * 9/5) + 32
#         print(f'O valor da temperatura em Fahrenheit eh : {far:.1f}ºF')
#     elif medida == "F":
#         cel = (temp - 32) * 5/9
#         print(f'O valor da temperatura em Fahrenheit eh : {cel:.1f}ºC')
#     else:
#         print("Unidade invalida use 'C' para Celcius e 'F' para Fahrenheit")    

# except ValueError as e:
#     print(f'Valor digitado incorreto: {e}')


# 22: Verificador de Palíndromo

# def verificador(texto):
#     texto_limpo = texto.replace(" ", "").lower()
#     return texto_limpo == texto_limpo[::-1]

# try:
#     entrada = input("Digite o texto para ser verificado: ").strip()
    
#     if not entrada:
#         print('Erro: Entrada vazia!')
#     elif verificador(entrada):
#         print(f'"{entrada}" eh um Paliandromo.')
#     else:
#         print(f'"{entrada}" nao eh um Paliandro.')
# except KeyboardInterrupt:
#     print("\nOperacao cancelada pelo usuario!")
# except Exception as e:
#     print(f"Erro inesperado: {e}")

# 23: Calculadora Simples

# try:
#     valor1 = float(input("Digite um valor: "))
#     valor2 = float(input("Digite outro valor: "))
#     operacao = input("Digite a operacao(+,-,*,/): ")

#     if operacao == "+":
#         print(f'O resultado da soma de {valor1} + {valor2} = {valor1 + valor2}')
#     elif operacao == "-":
#         print(f'O resultado da subtracao de {valor1} - {valor2} = {valor1 - valor2}')
#     elif operacao == "*":
#         print(f'O resultado da multiplicao de {valor1} * {valor2} = {valor1 * valor2}')
#     elif operacao == "/":
#         print(f'O resultado da divisao de {valor1} / {valor2} = {valor1 / valor2}')
#     else:
#         print(f'Opercao digitada incorre, escolha: \n+ para soma,\n- para subtracao,\n* para multiplicacao,\n/ para divisao.')
# except ValueError as e:
#     print(f'Valor digitado incorreto: {e}')


# 24: Classificador de Números

# try:
#     lista = input("Digite os numeros que deseja classificar separados por ',': ")
#     lista_limpa = lista.split(',').sort()
#     print(f'A classificacao correta eh: {lista_limpa}')
# except ValueError as e:
#     print('Valor digitado incorreto: {e}')

# 25: Conversão de Tipo com Validação

# try:
#     valor = input("Digite um valor: ")
#     tipo = input("Digite o tipo: ").lower()

#     if tipo == "int":
#         resultado = int(valor)
#         print(f'O valor convertido eh: {resultado}')
#     elif tipo == "float":
#         resultado = float(valor)
#         print(f'O valor convertido eh: {resultado}')
#     else:
#         print("Digite um tipo valor int ou float!")
        
# except ValueError as e:
#     print(f'Valor digitado nao reconhecido: {e}')