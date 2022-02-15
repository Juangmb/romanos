import unittest
from romanNumber import RomanNumber

class RomanNumberTest(unittest.TestCase):
    def test_comparaciones_funcionan(self):
        once = RomanNumber(11)
        doce = RomanNumber(12)
        diez_mas_uno = RomanNumber(11)

        self.assertTrue(once < doce)
        self.assertFalse(doce < once)
        self.assertTrue(doce > once)
        self.assertFalse(once > doce)
        self.assertTrue(once <= diez_mas_uno)
        self.assertFalse(doce <= once)
        self.assertTrue(doce >= doce)
        self.assertFalse(diez_mas_uno >= doce)
    
    def test_operaciones_aritmeticas(self):
        once = RomanNumber(11)
        doce = RomanNumber(12)

        self.assertEqual(once + doce, RomanNumber(23))
        self.assertEqual(doce - once, RomanNumber(1))
        self.assertEqual(doce // once, RomanNumber(1))
        self.assertEqual(doce * once, RomanNumber(132))
        self.assertEqual(doce ** RomanNumber(2), RomanNumber(144))
        
