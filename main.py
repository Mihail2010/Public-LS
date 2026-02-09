from lark import Lark, Transformer
from grammar import GRAMMAR
from NumberTransformer import NumTransformer
import sys

def main():
    parser = Lark(GRAMMAR, start='start', parser='lalr')
    transformer = NumTransformer()

    CODE = '''
        if (2 < 1) {
            write("HELLO IF");
        }
    '''


    tree = parser.parse(CODE)
    result = transformer.transform(tree)
    print(f"{result}")


if __name__ == "__main__":
    main()
