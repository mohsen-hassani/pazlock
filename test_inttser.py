import unittest
import inttser

class TestInttser(unittest.TestCase):
    def test_str2int(self):
        '''Test if string value returns it coresponding number '''
        str_value = 'Fo0B@|\\'
        result = inttser.int_representation(str_value)
        self.assertEqual(result, '070111048066064124092')
    def test_int2str(self):
        '''Test if number in str_value returns it coresponding string '''
        str_value = '070111048066064124092'
        result = inttser.str_representation(str_value)
        self.assertEqual(result, 'Fo0B@|\\')

if __name__ == '__main__':
    unittest.main()