# Advent of code 2023 Day x
# Solution by: https://github.com/smuuule
import sys, argparse
from solution import part1, part2

def main(argv):
    
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--input", type=str, help="input file for solution", required=True)
    argParser.add_argument("-p", "--part", type=int, help="part number (default: 1)", default=1, choices=[1,2])
    
    args = argParser.parse_args()

    with open(args.input, "r") as input_file:
        input = input_file.read()
        
    if args.part == 1:
        output = part1(input)
    elif args.part == 2:
        output = part2(input)
        
    print(output)

if __name__ == '__main__':
    main(sys.argv[1:])