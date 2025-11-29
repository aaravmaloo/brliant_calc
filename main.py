import argparse
import sys
import shlex
from calculator import basic_ops, advanced_ops, vectors, physics_formulas, units

class safeargparser(argparse.ArgumentParser):
    def error(self, message):
        
        raise ValueError(message)

def execute_command(arguments):
    try:
        if arguments.command == "basic":
            operation = arguments.operation
            nums = arguments.numbers
            func = getattr(basic_ops, operation)
            
            if operation == "mod":
                if len(nums) != 2:
                    print("Error: mod requires exactly two arguments")
                    return
                result = func(*nums)
            else:
                result = func(*nums)
                
            if isinstance(result, (int, float)):
                print(f"{result:g}")  
            else:
                print(result)

        elif arguments.command == "adv":
            operation = arguments.operation
            nums = arguments.numbers   
            func = getattr(advanced_ops, operation)
            
            try:
                result = func(*nums)
            except TypeError as e:
                print(f"Error: {e}")
                return

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
            func = getattr(vectors, arguments.operation)
            comps = arguments.components
            
            if arguments.operation in ["dot_product", "cross_product", "angle_between"]:
                if len(comps) % 2 != 0:
                    print("Error: Vectors must have the same number of dimensions.")
                    return
                mid = len(comps) // 2
                v1 = comps[:mid]
                v2 = comps[mid:]
                result = func(v1, v2)
            else:
                result = func(comps)
                
            print(result)

        elif arguments.command == "physics":
            func = getattr(physics_formulas, arguments.operation)
            try:
                result = func(*arguments.args)
            except TypeError as e:
                print(f"Error: {e}")
                return
            print(result)

        elif arguments.command == "units":
            func = getattr(units, arguments.category)
            result = func(arguments.value, arguments.from_unit, arguments.to_unit)
            print(result)
            
    except Exception as e:
        print(f"An error occurred: {e}")

def run_shell(category, parser):
    print(f"Entering {category} mode. Type 'exit' to quit.")
    while True:
        try:
            user_input = input(f"{category} > ")
            if user_input.strip().lower() in ["exit", "quit"]:
                break
            if not user_input.strip():
                continue
            full_args = [category] + shlex.split(user_input)
            args = parser.parse_args(full_args)
            execute_command(args)
            
        except ValueError as e:
            print(f"Error: {e}")
        except SystemExit:
            pass
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    parser = safeargparser(description="A command-line advanced scientific calculator")
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
    advanced_parser.add_argument("operation", choices=["sin", "cos", "tan", "log", "exp", "nth", "pow", "log10", "fact"])
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

    sel_parser = subparser.add_parser("sel", help="Interactive shell")
    sel_parser.add_argument("category", choices=["basic", "adv", "curr", "convert", "vector", "physics", "units"])

    try:
        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit(1)

        arguments = parser.parse_args()

        if arguments.command == "sel":
            run_shell(arguments.category, parser)
        else:
            execute_command(arguments)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()