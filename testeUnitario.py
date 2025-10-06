import unittest

class TestesExemplos(unittest.TestCase):
    def testar_se_numero_eh_par(self):
        numero_a_ser_testado = 18
        self.assertTrue(numero_a_ser_testado % 2 == 0)

    def testar_conta(self):
        resultado = 15 + 5 + 25 + 7
        self.assertEqual(resultado, 52)

if __name__ == "__main__":
    unittest.main()

# 3 testes diferentes

def testar_Se_Numero_é_menor_que_zero(self):
    n= 2
    self.assertTrue(n < 0)

def test_soma_positivos(self):
            resultado = soma(5, 3)
            self.assertEqual(resultado, 8)

def MULTIPLICAÇÃO(self):
        resultado = 10 * 2
        self.assertEqual(resultado, 20)
