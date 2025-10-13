# Testes 
def classificar_idade(idade):
    if idade <12 and idade >=1:
       return 'Criança'
    elif idade >= 12 and idade <=17:
       return 'Adolescente'
    elif idade >= 18 and idade <= 100:
        return 'Adulto'
    else:
        return 'Idade inválida'


# Exercício MAior de dois números

def comparador_numero(n1, n2):
    if n1 > n2:
        return f"O {n1} é maior que o {n2}"
    elif n2 > n1:
        return f"O {n2} é maior que o {n1}"
    else:
        return f"Os valores {n1} e {n2} são os mesmos"


# 3. Verificação de Vogal ou Consoante

def Verificação(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return (f'A letra digitada é uma vogal.')
    else:
        return (f'A letra digitada é uma consoante.')

# 4. Comparação de Senhas
# Solicite ao usuário que defina uma senha e, em seguida, peça para confirmá-la. Caso as senhas sejam iguais, exiba “Acesso permitido”, senão, exiba “Senhas não coincidem”.

def Comparação_de_Senhas(senha1,senhaConfirmada):
    if(senha1 == senhaConfirmada):
        return('Acesso permitido!')
    else:
        return('Acesso negado!')

# 5. Cálculo de Média e Aprovação
# Peça ao usuário para digitar três notas e calcule a média. Se a média for maior ou igual a 7, o aluno está aprovado, caso contrário, está reprovado.


def Calculo_de_Media(nota1, nota2, nota3,):

 media = (nota1 + nota2 + nota3) / 3

 if media >= 7 and media <= 10:
    return f'O aluno está aprovado com média!'
 elif media < 7 and media >= 0:
    return f'O aluno está reprovado com média!'
 else:
    return 'Média inválida!'

# 6. Escreva um programa que leia 3 números inteiros e imprima na tela os valores em ordem decrescente

def organizar_numeros_descrescente(numero1, numero2, numero3):

 listaDeNumeros = [numero1, numero2, numero3]

 return(f'A lista dos números em ordem decrescente é: {sorted(listaDeNumeros,reverse=True)}')

# 7. Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz
# 	12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média.
# 	Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
# 	Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a
# 	fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média,
# 	tempo gasto, a distância percorrida e a quantidade de litros utilizada na viagem. Dica: trabalhe com valores reais.

def calcular_litros_usados(tempoGasto, velocidadeMedia):

    distancia = tempoGasto * velocidadeMedia
    litrosUsados = distancia / 12
    return f'Foram utilizados {litrosUsados}L na viagem'
