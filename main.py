import argparse
import sys

from core.lexer import CCTRLexer
from core.parser import CCTRParser
from core.range_deleter import RangeDeleter
from core.range_mapper import RangeMapper
from core.range_pipeline import RangePipeline
from core.range_squeezer import RangeSqueezer
from utils.user_reader import execute_reader

parser = argparse.ArgumentParser()

parser.add_argument("-ds", "--delsque", action='store_true', help="Delete and squeeze")
parser.add_argument("-d", "--delete", action='store_true', help="Delete mode")
parser.add_argument("-s", "--squeeze", action='store_true', help="Squeeze mode")

parser.add_argument("string1", nargs='?', default=None)
parser.add_argument("string2", nargs='*', default=None, type=str)

args = parser.parse_args()

lexer = CCTRLexer()
parser = CCTRParser()

def main():

    if args.delsque or args.delete or args.squeeze:
        if args.string1 is None:
            raise ValueError("Not enough arguments. One string is required for this mode.")

        arg1 = args.string1
        arg2 = ''.join(args.string2) if args.string2 else None

        if args.delsque:
            del_range = parser.parse(lexer.tokenize(arg1))
            sqz_range = parser.parse(lexer.tokenize(arg2))

            range_deleter = RangeDeleter(del_range)
            range_squeezer = RangeSqueezer(sqz_range)

            range_pipeline = RangePipeline([range_deleter, range_squeezer])

            execute_reader(range_pipeline)

        elif args.squeeze:
            src_range = parser.parse(lexer.tokenize(arg1))
            range_squeezer = RangeSqueezer(src_range)

            execute_reader(range_squeezer)
        elif args.delete:
            src_range = parser.parse(lexer.tokenize(arg1))
            range_deleter = RangeDeleter(src_range)

            execute_reader(range_deleter)
    else:

        arg1 = args.string1
        arg2 = ''.join(args.string2) if args.string2 else None

        if not arg1 or not arg2:
            raise ValueError("Not enough arguments. Two strings are required for this mode.")

        src_range = parser.parse(lexer.tokenize(arg1))
        to_range = parser.parse(lexer.tokenize(arg2))
        range_mapper = RangeMapper(src_range, to_range)

        execute_reader(range_mapper)


if __name__ == "__main__":
    try:
        main()
    except ValueError:
        sys.exit(1)
