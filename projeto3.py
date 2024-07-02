import os
# PROJETO3: Calculadora de IMC


nome = input('Digite seu nome: ')

altura = int(input('Digite qual a sua ALTURA em cm: '))

peso = int(input('Digite seu peso em KG: '))

imc = peso / (altura/100) ** 2

if imc < 18.5:
    estado = print(f'Sua massa corporal é: {imc} seu estado fisico MAGREZA')
elif imc > 18.5 and imc < 24.9:
    estado = print(f'Sua massa corporal é: {imc} seu estado fisico NORMAL')
elif imc >= 25 and imc < 29.9:
    estado = print(f'Sua massa corporal é: {imc} seu estado fisico SOBREPESO')
elif imc >= 30 and imc < 39.9:
    estado = print(f'Sua massa corporal é: {imc} seu estado fisico OBESIDADE')
else:
    estado = print(f'Sua massa corporal é: {imc} seu estado fisico OBESIDADE GRAVE')

os.system('pause')
