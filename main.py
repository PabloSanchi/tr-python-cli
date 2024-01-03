import os, argparse
from core.lexer import CCTRLexer
from core.parser import CCTRParser
from core.range_mapper import RangeMapper

parser = argparse.ArgumentParser()

parser.add_argument("-ds", "--delsque", help="Delete and sequeeze")
parser.add_argument("-d", "--delete", help="Delete mode")
parser.add_argument("-s", "--squezee", help="Squeeze mode")
parser.add_argument("string1")
parser.add_argument("string2", nargs='*', default="", type=str)

args = parser.parse_args()

lexer = CCTRLexer()
parser = CCTRParser()

if args.delsque:
    print("Delete and squeeze mode")
elif args.delete:
    print("Delete mode")
elif args.squezee:
    print("Squeeze mode")
else:
    
    arg1 = args.string1
    arg2 = ''.join(args.string2)
    
    if not arg1 or not arg2:
        raise ValueError("Not enough arguments")
    
    try:
        src_range = parser.parse(lexer.tokenize(arg1))
        to_range = parser.parse(lexer.tokenize(arg2))
        range_mapper = RangeMapper(src_range, to_range)
        
        while True:
            try:
                user_input = input()
                output = range_mapper.execute(user_input)
                print(output)
            except:
                break
    except ValueError as err:
        os.error(err)