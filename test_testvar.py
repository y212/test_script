import unittest
import testvar


class Testing(unittest.TestCase):
    def test_test_var(self):
        x = testvar.main(['--name', 'bhanu_new', '--age', '21'])
        self.assertEqual(x, 'hellobhanu_new21')


if __name__=='__main__':
    unittest.main()