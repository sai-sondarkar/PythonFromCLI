import unittest
import fcs

class TestFcs( unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = fcs.fcs_text(text)
        self.assertEqual(result,'Python')
    
    def test_multiple_words(self):
        text = 'akash cibi'
        result = fcs.fcs_text(text)
        self.assertEqual(result,'Akash Cibi')

if __name__ == '__main__':
    unittest.main()
