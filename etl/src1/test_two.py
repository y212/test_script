import unittest
from etl.src1 import two


class Testing(unittest.TestCase):
    def test_two(self):
        x = two.yash(5,6)
        print('testing two')
        self.assertEqual(x,30)
        


if __name__=='__main__':
    unittest.main()