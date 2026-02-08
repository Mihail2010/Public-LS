from lark import Lark, Transformer
from grammar import GRAMMAR
from NumberTransformer import NumTransformer
import sys

def main():
    parser = Lark(GRAMMAR, start='start', parser='lalr')
    transformer = NumTransformer()

    CODE = '''
    write(324234);
    write("rerere");
    '''
     

    tree = parser.parse(CODE)
    result = transformer.transform(tree)
    print(f"{result}")
        
if __name__ == "__main__":
    main()
