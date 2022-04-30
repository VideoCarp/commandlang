from lark import Lark
parser = None
with open("grammar.ebnf") as f:
    parser = Lark(f.read(), start="program")

def parse(code):
    return parser.parse(code)
