import unittest

from translator import english_to_french, french_to_english

class Test_EngTranslator(unittest.TestCase): 
    def test1e(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Yes'), 'Non')
        self.assertIsNone(english_to_french(None),None)

class Test_FrnTranslator(unittest.TestCase):     
    def test1f(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Non'), 'Yes')
        self.assertIsNone(english_to_french(None),None)

unittest.main()