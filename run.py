from etl.src import test_one
from etl.src1 import test_two

if __name__ == '__main__':
    stream = open("etl/src/test_one.py")
    read_file = stream.read()
    exec(read_file)
