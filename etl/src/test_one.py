import unittest
import one


class Testing(unittest.TestCase):
    def test_one(self):
        x = one.yash(5,6)
        print('testing one')
        self.assertEqual(x,11)
        


if __name__=='__main__':
    unittest.main()