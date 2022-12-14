import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from MiListener import MiListener
from MiVisitor import MiVisitor

def main(argv):
    archivo = "./input/programa.c"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    miListener = MiListener()
    miVisitor = MiVisitor()
    parser.addParseListener(miListener)
    tree = parser.program()
    miVisitor.visitProgram(tree)
    #print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)