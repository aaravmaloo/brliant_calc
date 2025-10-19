import argparse
from calculator import basic_ops

parser = argparse.ArgumentParser(description="A command-line advanced scientific calculator")

subparser = parser.add_subparsers(dest="command", help="available commands")

basic_parser = subparser.add_parser("basic", help="Basic arithmetic operations")
basic_parser.add_argument("operation", choices=["add", "sub", "div", "mul", "mod"])
basic_parser.add_argument("numbers", type=float, nargs="+")


advanced_parser = subparser.add_parser("adv", help="Advanced mathematical operations")
advanced_parser.add_argument("operation", choices=["sin", "cos", "tan", "log", "exp", "nth", "pow"])
advanced_parser.add_argument("numbers", type=float, nargs="+")

arguments = parser.parse_args()

if arguments.command == "basic":
    operation = arguments.operation
    nums = arguments.numbers

    func = getattr(basic_ops, operation)
    result = func(*nums)

    if isinstance(result, (int, float)):
        print(f"{result:g}")  
    else:
        print(result)
elif arguments.command == "adv":
    operation = arguments.operation
    nums = arguments.numbers   

    from calculator import advanced_ops
    func = getattr(advanced_ops, operation)
    result = func(*nums)     

    if isinstance(result, (int, float)):
        print(f"{result:g}")
    else:
        print(result)