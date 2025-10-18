import argparse
from calculator import basic_ops

parser = argparse.ArgumentParser(description="A command-line advanced scientific calculator")

subparser = parser.add_subparsers(dest="command", help="available commands")

basic_parser = subparser.add_parser("basic", help="Basic arithmetic operations")
basic_parser.add_argument("operation", choices=["add", "sub", "div", "mul", "mod"])
basic_parser.add_argument("numbers", type=float, nargs="+")

arguments = parser.parse_args()

if arguments.command == "basic":
    if arguments.operation == "add":
        res = basic_ops.add(*arguments.numbers)
        print(f"{res:g}")