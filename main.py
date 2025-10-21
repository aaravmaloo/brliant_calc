import argparse
from calculator import basic_ops

parser = argparse.ArgumentParser(description="A command-line advanced scientific calculator")

subparser = parser.add_subparsers(dest="command", help="available commands")

basic_parser = subparser.add_parser("basic", help="Basic arithmetic operations")
basic_parser.add_argument("operation", choices=["add", "sub", "div", "mul", "mod"])
basic_parser.add_argument("numbers", type=float, nargs="+")


currency_parser = subparser.add_parser("curr", help="Currency conversion operations")
currency_parser.add_argument("update", choices=["upd"], help="Update currency exchange rates")

advanced_parser = subparser.add_parser("adv", help="Advanced mathematical operations")
advanced_parser.add_argument("operation", choices=["sin", "cos", "tan", "log", "exp", "nth", "pow", "log10", "fact", ])
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


elif arguments.command == "curr":
    if arguments.update == "upd":
        from currency_converter.app import get_curr_json
        result = get_curr_json()
        print("Exchange rates updated successfully.") 
        