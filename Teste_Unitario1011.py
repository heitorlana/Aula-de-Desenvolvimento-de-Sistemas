import unittest
from seu_arquivo import (
    primos_no_intervalo,
    ordenar_sem_repeticao,
    soma_digitos,
    eh_palindromo,
    frequencia_palavras,
    media_lista
)

class TestFuncoes(unittest.TestCase):

    def test_primos_no_intervalo(self):
        self.assertEqual(primos_no_intervalo(10, 20), [11, 13, 17, 19])
        self.assertEqual(primos_no_intervalo(1, 5), [2, 3, 5])
        self.assertEqual(primos_no_intervalo(-10, 3), [2, 3])
        self.assertEqual(primos_no_intervalo(20, 10), [])

    def test_ordenar_sem_repeticao(self):
        self.assertEqual(ordenar_sem_repeticao([5, 2, 8, 2, 5, 1, 8]), [1, 2, 5, 8])
        self.assertEqual(ordenar_sem_repeticao([]), [])
        self.assertEqual(ordenar_sem_repeticao([3, 3, 3]), [3])

    def test_soma_digitos(self):
        self.assertEqual(soma_digitos(456), 15)
        self.assertEqual(soma_digitos(0), 0)
        self.assertEqual(soma_digitos(-123), 6)

    def test_eh_palindromo(self):
        self.assertTrue(eh_palindromo("A base do teto desaba"))
        self.assertTrue(eh_palindromo("Ovo"))
        self.assertFalse(eh_palindromo("Python"))

    def test_frequencia_palavras(self):
        texto = "Eu amo programar, e você ama programar também"
        resultado = frequencia_palavras(texto)

        self.assertEqual(resultado["eu"], 1)
        self.assertEqual(resultado["amo"], 1)
        self.assertEqual(resultado["programar,"], 1)
        self.assertEqual(resultado["e"], 1)
        self.assertEqual(resultado["você"], 1)
        self.assertEqual(resultado["ama"], 1)
        self.assertEqual(resultado["programar"], 1)
        self.assertEqual(resultado["também"], 1)

    def test_media_lista(self):
        self.assertEqual(media_lista([10, 20, 30, 40]), 25.0)
        self.assertEqual(media_lista([5]), 5)
        self.assertIsNone(media_lista([]))


if __name__ == "__main__":
    unittest.main()
