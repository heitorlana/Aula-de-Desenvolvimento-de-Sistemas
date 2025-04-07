# 1- idade

idade = input("Digite sua idade: ")

if idade < 12:
    print("Criança")
elif idade >= 12 or idade <= 17:
    print("Adolecente")
else:
    print("Adulto")

#2- MAior de dois números

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    print("O ", n1, " é maior que o ", n2)
elif n2 > n1:
    print("O ", n2, " é maior que o ", n1)
else:
    print("Os valores ", n1, " e ", n2, " são os mesmos")



# 3- verificação de vogal ou consoante

Letra = str(input("Digite uma letra: "))

if Letra == "a" or Letra == "e" or Letra == "i" or Letra == "o" or Letra == "u":
    print("A letra é vogal")
else:
   print("A letra é consoante")

# 4- Comparação de senhas

Senha = input("Crie uma senha: ")
Senha2 = input("confirme sua senha: ")

if Senha2 == Senha:
    print("Acesso permitido")
else:
    print("Acesso negado")

#5- Cálculo média

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))

soma = nota1 + nota2 + nota3

media = soma / 3

if media >= 7:
    print("aprovado")

else:
    print("reprovado")

#6- 3 tres numeros em ordem decrescente

N1 = int(input('Digite um número: '))
N2 = int(input('Digite um número: '))
N3 = int(input('Digite um número: '))

numeros = [N1, N2, N3]

numeros.sort(reverse=True)

print(numeros)


#7- QUANTIDADE DE GASOLINA EM UMA VIAGEM

Tempo = int(input("Digite o tempo de sua viagem(em horas): "))
Velocidade = int(input("Digite a velocidade média de sua viagem(em km/h): "))


Distancia = Tempo * Velocidade


litros_usados = Distancia / 12

print("A velocidade media durante a viagem foi de ", Velocidade)
print("O tempo gasto na viagem foi de ", Tempo)
print("A distancia percorida durante a viagem foi de ", Distancia)
print("A quantidade de litros usada em sua viagem foi de(em ml):", litros_usados)
