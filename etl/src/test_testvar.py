import unittest
from etl.src.testvar import main


class Testing(unittest.TestCase):
    def test_test_var(self):
        x = main(['--name', 'bhanu_new', '--age', '21'])
        self.assertEqual(x, 'hellobhanu_new21')


if __name__=='__main__':
    unittest.main()