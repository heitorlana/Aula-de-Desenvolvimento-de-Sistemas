#EXERCÍCIO 01
n1 = int(input("digite 1 número: "))
n2 = int(input("digite 1 número: "))
n3 = int(input("digite 1 número: "))
n4 = int(input("digite 1 número: "))
n5 = int(input("digite 1 número: "))


soma = n1 , n2 , n3 , n4 , n5
calculo = sum(soma)
print("a soma é", calculo)


#EXERCÍCIO 02
nm1 = int(input("digite o primeiro número: "))
nm2 = int(input("digite o segundo número: "))
nm3 = int(input("digite o terceiro número: "))
nm4 = int(input("digite o quarto  número: "))
numeros = nm1 , nm2 , nm3 , nm4


maior = max(numeros)
menor = min(numeros)


print("O maior número é:", maior)
print("O menor número é:", menor)


#EXERCÍCIO 03

palavra = input("digite uma palavra: ")
vogais = "a,e,i,o,u"
contador = 0


for letra in palavra:
    if letra in vogais:
        contador += 1


print(f"A palavra '{palavra}' contém {contador} vogais.")


#EXERCÍCIO 04

nms1 = int(input("digite 1 número: "))
nms2 = int(input("digite 1 número: "))
nms3 = int(input("digite 1 número: "))
nms4 = int(input("digite 1 número: "))
nms5 = int(input("digite 1 número: "))
nms6 = int(input("digite 1 número: "))
inp  = nms1, nms2, nms3, nms4, nms5, nms6
contador = 0


for numero in inp:
    if numero % 2 == 0:
        print(numero, end=" ")


print()

# EXERCÍCIO 05


nota1 = float(input("digite 1 nota: "))
nota2 = float(input("digite 2 nota: "))
nota3 = float(input("digite 3 nota: "))
nota4 = float(input("digite 4 nota: "))
provas = nota1 + nota2 + nota3 + nota4
divisão = provas/4
print("sua média é ", divisão)


#EXERCÍCIO 06


numero = int(input("Digite um número: "))
print(numero * 1)
print(numero * 2)
print(numero * 3)
print(numero * 4)
print(numero * 5)
print(numero * 6)
print(numero * 7)
print(numero * 8)
print(numero * 9)
print(numero * 10)


#EXERCÍCIO 07


N = int(input("Digite um número: "))

for i in range(1, N + 1):
    print(i)


# EXERCÍCIO 08

palavra = input("Digite uma palavra: ")
palavra_invertida = palavra[::-1]  # Usando slicing para inverter a palavra
print("Palavra invertida:", palavra_invertida)


# EXERCÍCIO 09

numero = int(input("Digite um número: "))
numero3 = numero * 3

if numero >= numero3 :
  print("o número é multiplo de 3")
else:
  print("o numero não multiplo 3")


#EXERCÍCIO 10

nomes = []

for i in range(3):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)


nomes_ordenados = sorted(nomes)

print("Nomes em ordem alfabética:", nomes_ordenados)

