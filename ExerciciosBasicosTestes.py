# Teste Unitario
import unittest

from Exercicios_Basicos import *

class TestesExemplos(unittest.TestCase):
    def testar_se_numero_eh_par(self):
        numero_a_ser_testado = 18
        self.assertTrue(numero_a_ser_testado % 2 == 0)

    def testar_conta(self):
         resultado = 15 + 5 + 25 + 7
         self.assertEqual(resultado, 52)

    def testar_classificar_idade(self):
        self.assertEqual(classificar_idade(10), 'Criança')
        self.assertEqual(classificar_idade(15), 'Adolescente')
        self.assertEqual(classificar_idade(34), 'Adulto')
        self.assertEqual(classificar_idade(150), 'Idade inválida')

    def testar_comparador_de_numeros(self):
        self.assertEqual(comparador_numero(10, 2), "O 10 é maior que o 2")
        self.assertEqual(comparador_numero(20, 30), "O 30 é maior que o 20")
        self.assertEqual(comparador_numero(5, 5), "Os valores 5 e 5 são os mesmos")


    def teste_Verificação(self):
          self.assertEqual( Verificação('a'), 'A letra digitada é uma vogal.')
          self.assertEqual( Verificação('s'), 'A letra digitada é uma consoante.')

    def teste_Comparação_de_Senhas(self):
        self.assertEqual( Comparação_de_Senhas("Tor15", "Tor15" ), 'Acesso permitido!')
        self.assertEqual(Comparação_de_Senhas("theo", "tor15"), 'Acesso negado!')

    def teste_Calculo_de_Media(self):
        self.assertEqual(Calculo_de_Media(10,10,10 ), 'O aluno está aprovado com média!')
        self.assertEqual(Calculo_de_Media(5, 5, 5), 'O aluno está reprovado com média!')


    def teste_Programa(self):
        self.assertEqual(organizar_numeros_descrescente(1,2,3), 'A lista dos números em ordem decrescente é: [3, 2, 1]')
        self.assertEqual(organizar_numeros_descrescente(4,1,2), 'A lista dos números em ordem decrescente é: [4, 2, 1]')

    def teste_calcular_litros_usados(self):
        self.assertEqual(calcular_litros_usados(12, 100), 'Foram utilizados 100.0L na viagem')

  
