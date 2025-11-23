import argparse
from calculator import basic_ops

parser = argparse.ArgumentParser(description="A command-line advanced scientific calculator")

subparser = parser.add_subparsers(dest="command", help="available commands")

basic_parser = subparser.add_parser("basic", help="Basic arithmetic operations")
basic_parser.add_argument("operation", choices=["add", "sub", "div", "mul", "mod"])
basic_parser.add_argument("numbers", type=float, nargs="+")


currency_parser = subparser.add_parser("curr", help="Currency conversion operations")
currency_parser.add_argument("update", choices=["upd"], help="Update currency exchange rates")

convert_parser = subparser.add_parser("convert", help="Convert currency")
convert_parser.add_argument("from_currency", type=str, help="Source currency code (e.g., USD)")
convert_parser.add_argument("to_currency", type=str, help="Target currency code (e.g., INR)")
convert_parser.add_argument("amount", type=float, help="Amount to convert")

advanced_parser = subparser.add_parser("adv", help="Advanced mathematical operations")
advanced_parser.add_argument("operation", choices=["sin", "cos", "tan", "log", "exp", "nth", "pow", "log10", "fact", ])
advanced_parser.add_argument("numbers", type=float, nargs="+")

vector_parser = subparser.add_parser("vector", help="Vector operations")
vector_parser.add_argument("operation", choices=["dot_product", "cross_product", "magnitude", "normalize", "angle_between"])
vector_parser.add_argument("components", type=float, nargs="+", help="Vector components")

physics_parser = subparser.add_parser("physics", help="Physics formulas")
physics_parser.add_argument("operation", choices=["force", "kinetic_energy", "potential_energy", "ohms_law", "work", "speed", "acceleration"])
physics_parser.add_argument("args", type=float, nargs="+", help="Arguments for the formula")

units_parser = subparser.add_parser("units", help="Unit conversions")
units_parser.add_argument("category", choices=["length", "mass", "temperature", "time", "speed"])
units_parser.add_argument("value", type=float, help="Value to convert")
units_parser.add_argument("from_unit", type=str, help="Source unit")
units_parser.add_argument("to_unit", type=str, help="Target unit")

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

elif arguments.command == "convert":
    from calculator.convert_currency import convert_currency
    result = convert_currency(arguments.from_currency, arguments.to_currency, arguments.amount)
    print(f"{arguments.amount} {arguments.from_currency} = {result:.2f} {arguments.to_currency}")

elif arguments.command == "vector":
    from calculator import vectors
    func = getattr(vectors, arguments.operation)
    result = func(*arguments.components)
    print(result)

elif arguments.command == "physics":
    from calculator import physics_formulas
    func = getattr(physics_formulas, arguments.operation)
    result = func(*arguments.args)
    print(result)

elif arguments.command == "units":
    from calculator import units
    func = getattr(units, arguments.category)
    result = func(arguments.value, arguments.from_unit, arguments.to_unit)
    print(result)