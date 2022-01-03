import argparse


def test1(name, age):
    return "hello" + name + age


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--name")
    parser.add_argument("--age")
    t = parser.parse_args(args)
    return test1(t.name, t.age)


if __name__=='__main__':
    print(main())