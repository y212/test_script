# import sys
# from os import path, read
# from pathlib import Path
# p = path.join(str(Path(__file__).resolve().parents[1]))
# sys.path.insert(0, p)

import unittest
from etl.src import one,test_testvar,testvar
from etl.src1 import two,test_two


class Testing(unittest.TestCase):
    def test_one(self):
        x = one.yash(5,6)
        print('testing one')
        self.assertEqual(x,11)
        


if __name__=='__main__':
    unittest.main()
    