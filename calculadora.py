# como fazer uma calculadora em python 

# print("#######calculadora#####")

numero1 = int (input ("digite o primeiro numero: "))
numero2 = int(input ("digite o segundo número: "))


def soma (numero1, numero2):
    return print(numero1 + numero2)
    

def multiplicacao (numero1, numero2):
    return print(numero1 * numero2)

def subtracao (numero1, numero2):
    return print(numero1 - numero2)

def divisao (numero1, numero2):
    return print(numero1 / numero2)

print("Escolha uma das opções e digite a baixo: soma, multiplicacao, subtracao, divisao")

opção = input("digite a opção sem acentuação \n")

if opção == "soma":
    soma(numero1, numero2)
    
elif opção == "multiplicacao":
    multiplicacao(numero1, numero2)
    
elif opção == "subtracao":
    subtracao(numero1, numero2)
   
elif opção == "divisao":
    divisao(numero1, numero2)
   


   
   
   
