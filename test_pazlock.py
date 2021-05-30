import unittest
import pazlock

class TestPazlock(unittest.TestCase):
    def test_lock(self):
        '''Test lock string foo with key bar '''
        str_value = 'foo'
        key = 'bar'
        result = pazlock.lock_password(str_value, key)
        self.assertEqual(result, '0200208225')
    def test_unlock(self):
        '''Test unlock number 0200208225 with key bar '''
        locked_value = '0200208225'
        key = 'bar'
        result = pazlock.unlock_password(locked_value, key)
        self.assertEqual(result, 'foo')

if __name__ == '__main__':
    unittest.main()