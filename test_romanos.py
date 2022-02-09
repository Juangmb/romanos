import unittest

from romanos import RomanError, arabigo_a_romano, romano_a_arabigo2

class RomanosFuncionesTest(unittest.TestCase):
    def test_arabigo_a_romano_sin_restas(self):
        self.assertEqual(arabigo_a_romano(36), "XXXVI")

    def test_arabigo_a_romano_con_restas(self):
        self.assertEqual(arabigo_a_romano(464), "CDLXIV")
    
    def test_arabigo_a_romano_solo_admite_enteros(self):
        with self.assertRaises(TypeError):
            arabigo_a_romano("lolailo")
    
    def test_arabigo_a_romano_solo_admite_enteros_positivos(self):
        with self.assertRaises(ValueError):
            arabigo_a_romano(-23)
    
class RomanosFuncionesAromanoTest(unittest.TestCase):
    def test_romano_a_arabigo_tres_repeticiones_OK(self):
        self.assertEqual(romano_a_arabigo2("III"), 3)
    
    def test_romano_a_arabigo_cuatro_repeticiones_ERROR(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo2("IIII")
    
    def test_romano_a_arabigo_5_no_resta(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo2("VX")
        with self.assertRaises(RomanError):
            romano_a_arabigo2("LC")
        with self.assertRaises(RomanError):
            romano_a_arabigo2("DM")
    
    def test_romano_a_arabigo_no_repetir_tras_resta(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo2("XXL")
    
    def test_romano_a_arabigo_solo_resta_inmediatos(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo2("IL")
        with self.assertRaises(RomanError):
            romano_a_arabigo2("IC")
        with self.assertRaises(RomanError):
            romano_a_arabigo2("ID")
        with self.assertRaises(RomanError):
            romano_a_arabigo2("IM")
        with self.assertRaises(RomanError):
            romano_a_arabigo2("XD")
        with self.assertRaises(RomanError):
            romano_a_arabigo2("XM")

    


"""
from romanos import arabigo_a_romano, romano_a_arabigo, romano_a_arabigo2

print(arabigo_a_romano(36))
print(arabigo_a_romano(44))

print(romano_a_arabigo2("MMCCCXXXIV"))
print(romano_a_arabigo2("MMMMM"))

print(romano_a_arabigo2("VVV"))
"""