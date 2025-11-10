#Função: Número Primos em Intervalo
def primos_no_intervalo(a, b):
    primos = []
    for n in range(a, b + 1):
        
        if n > 1:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    break
            else:
                primos.append(n)
    return primos

#Função: Ordena e Remove Duplicatas
def ordenar_sem_repeticao(lista):
    sem_repeticao = set(lista)
    lista_ordenada = sorted(sem_repeticao)
    
    return lista_ordenada

# Função: Soma dos Digitos 
def soma_digitos(n):
    texto_numero = str(abs(n))   
    soma_total = 0
    for digito_texto in texto_numero:
        digito_inteiro = int(digito_texto)
        soma_total = soma_total + digito_inteiro    
    return soma_total

# Função: Palíndromo
def eh_palindromo(texto):
    t_sem_espaco = texto.replace(" ", "")
    t_limpo = t_sem_espaco.lower()
    t_invertido = t_limpo[::-1]  
    return t_limpo == t_invertido

# Função: Frequência de Palavras
def frequencia_palavras(texto):
    freq = {}
    palavras = texto.lower().split()
    for palavra in palavras:
        contagem_atual = freq.get(palavra, 0)
        freq[palavra] = contagem_atual + 1
    return freq

# Função: Frequência de Palavras
def media_lista(lista):
    if not lista:
        return None
    soma = sum(lista)
    quantidade = len(lista)
    return soma / quantidade


# Função: Média dos Elementos 
print("--- 1. Primos no Intervalo (10 a 20) ---")
print(f"Resultado: {primos_no_intervalo(10, 20)}") # Deve retornar [11, 13, 17, 19]

print("\n--- 2. Ordenar e Remover Duplicatas ---")
lista_com_duplicatas = [5, 2, 8, 2, 5, 1, 8]
print(f"Lista Original: {lista_com_duplicatas}")
print(f"Resultado: {ordenar_sem_repeticao(lista_com_duplicatas)}") # Deve retornar [1, 2, 5, 8]

print("\n--- 3. Soma dos Dígitos ---")
print(f"Soma dos dígitos de 456: {soma_digitos(456)}") # Deve retornar 4 + 5 + 6 = 15

print("\n--- 4. Palíndromo ---")
frase_palindromo = "A base do teto desaba"
print(f"'{frase_palindromo}' é palíndromo? {eh_palindromo(frase_palindromo)}") # Deve retornar True

print("\n--- 5. Frequência de Palavras ---")
texto_exemplo = "Eu amo programar, e você ama programar também"
print(f"Frequência: {frequencia_palavras(texto_exemplo)}")
# Deve retornar {'eu': 1, 'amo': 2, 'programar,': 2, 'e': 1, 'você': 1, 'também': 1}

print("\n--- 6. Média dos Elementos ---")
lista_numeros = [10, 20, 30, 40]
print(f"Média de {lista_numeros}: {media_lista(lista_numeros)}") # Deve retornar 100 / 4 = 25.0
print(f"Média de lista vazia: {media_lista([])}") # Deve retornar None
