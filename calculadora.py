def soma(a, b):
    return a + b


def subtração(a, b):
    return a - b


def multi(a, b):
    return a * b


def divisao(a, b):
    return a / b


operacao = int(input("Digite 1 para soma, 2 para subtração, 3 para multiplicação ou 4 para divisão: "))
a = int(input("Digite um numero: "))
b = int(input("Agora o outro: "))

if operacao == 1:
    print("Resultado: {}".format(soma(a, b)))
elif operacao == 2:
    print("Resultado: {}".format(subtração(a, b)))
elif operacao == 3:
    print("Resultado: {}".format(multi(a, b)))
elif operacao == 4:
    print("Resultado: {}".format(divisao(a, b)))
else:
    print("Informações inválidas!")
