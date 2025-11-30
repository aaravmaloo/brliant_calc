import argparse
import sys
import shlex

import basic_ops, advanced_ops, vectors, physics_formulas, units, matrix_ops, complex_ops, symbolic_ops, plotting, dimensional_analysis, precision_ops

class safeargparser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)

def execute_command(arguments):
    try:
        if arguments.command in ["basic", "b"]:
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

        elif arguments.command in ["adv", "a"]:
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

        elif arguments.command in ["curr", "cr"]:
            if arguments.update == "upd":
                from currency_converter.app import get_curr_json
                result = get_curr_json()
                print("Exchange rates updated successfully.") 

        elif arguments.command in ["convert", "cv"]:
            from calculator.convert_currency import convert_currency
            result = convert_currency(arguments.from_currency, arguments.to_currency, arguments.amount)
            print(f"{arguments.amount} {arguments.from_currency} = {result:.2f} {arguments.to_currency}")

        elif arguments.command in ["vector", "v"]:
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

        elif arguments.command in ["physics", "p"]:
            func = getattr(physics_formulas, arguments.operation)
            try:
                result = func(*arguments.args)
            except TypeError as e:
                print(f"Error: {e}")
                return
            print(result)

        elif arguments.command in ["units", "u"]:
            func = getattr(units, arguments.category)
            result = func(arguments.value, arguments.from_unit, arguments.to_unit)
            print(result)

        elif arguments.command in ["matrix", "m"]:
            func = getattr(matrix_ops, arguments.operation)
            if arguments.operation in ["mul"]:
                result = func(arguments.m1, arguments.m2)
            else:
                result = func(arguments.m1)
            print(result)

        elif arguments.command in ["complex", "cx"]:
            func = getattr(complex_ops, arguments.operation)
            if arguments.operation in ["add", "sub", "mul", "div"]:
                result = func(arguments.c1, arguments.c2)
            elif arguments.operation == "rect":
                result = func(arguments.c1, arguments.c2) # c1=r, c2=phi
            else:
                result = func(arguments.c1)
            print(result)

        elif arguments.command in ["symbolic", "s"]:
            func = getattr(symbolic_ops, arguments.operation)
            if arguments.operation in ["diff", "integrate", "solve"]:
                result = func(arguments.expression, arguments.variable)
            else:
                result = func(arguments.expression)
            print(result)

        elif arguments.command in ["plot", "pl"]:
            func = getattr(plotting, arguments.operation)
            result = func(arguments.function, arguments.range)
            print(result)

        elif arguments.command in ["dim", "d"]:
            func = getattr(dimensional_analysis, arguments.operation)
            if arguments.operation == "evaluate_dim":
                result = func(arguments.expression)
            else:
                result = func(arguments.value, arguments.from_unit, arguments.to_unit)
            print(result)

        elif arguments.command in ["precise", "pr"]:
            func = getattr(precision_ops, arguments.operation)
            if "decimal" in arguments.operation:
                result = func(arguments.n1, arguments.n2, arguments.precision)
            else:
                result = func(arguments.n1, arguments.n2)
            print(result)
            
    except Exception as e:
        print(f"an error has occurred: {e}")

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
            print(f"error: {e}")
        except SystemExit:
            pass
        except Exception as e:
            print(f"an error has occurred: {e}")

def main():
    parser = safeargparser(description="A command-line advanced scientific calculator")
    subparser = parser.add_subparsers(dest="command", help="available commands")

    basic_parser = subparser.add_parser("basic", aliases=["b"], help="Basic arithmetic operations")
    basic_parser.add_argument("operation", choices=["add", "sub", "div", "mul", "mod"])
    basic_parser.add_argument("numbers", type=float, nargs="+")

    currency_parser = subparser.add_parser("curr", aliases=["cr"], help="Currency conversion operations")
    currency_parser.add_argument("update", choices=["upd"], help="Update currency exchange rates")


    convert_parser = subparser.add_parser("convert", aliases=["cv"], help="Convert currency")
    convert_parser.add_argument("from_currency", type=str, help="Source currency code (e.g., USD)")
    convert_parser.add_argument("to_currency", type=str, help="Target currency code (e.g., INR)")
    convert_parser.add_argument("amount", type=float, help="Amount to convert")

    advanced_parser = subparser.add_parser("adv", aliases=["a"], help="Advanced mathematical operations")
    advanced_parser.add_argument("operation", choices=["sin", "cos", "tan", "log", "exp", "nth", "pow", "log10", "fact"])
    advanced_parser.add_argument("numbers", type=float, nargs="+")


    vector_parser = subparser.add_parser("vector", aliases=["v"], help="Vector operations")
    vector_parser.add_argument("operation", choices=["dot_product", "cross_product", "magnitude", "normalize", "angle_between"])
    vector_parser.add_argument("components", type=float, nargs="+", help="Vector components")

    physics_parser = subparser.add_parser("physics", aliases=["p"], help="Physics formulas")
    physics_parser.add_argument("operation", choices=["force", "kinetic_energy", "potential_energy", "ohms_law", "work", "speed", "acceleration"])
    physics_parser.add_argument("args", type=float, nargs="+", help="Arguments for the formula")

    units_parser = subparser.add_parser("units", aliases=["u"], help="Unit conversions")
    units_parser.add_argument("category", choices=["length", "mass", "temperature", "time", "speed"])

    units_parser.add_argument("value", type=float, help="Value to convert")
    units_parser.add_argument("from_unit", type=str, help="Source unit")
    units_parser.add_argument("to_unit", type=str, help="Target unit")

    matrix_parser = subparser.add_parser("matrix", aliases=["m"], help="Matrix operations")
    matrix_parser.add_argument("operation", choices=["mul", "det", "inv", "eig", "transpose", "rank"])
    
    matrix_parser.add_argument("m1", type=str, help="First matrix (e.g. '[[1,2],[3,4]]')")
    matrix_parser.add_argument("--m2", type=str, help="Second matrix for binary operations", required=False)

    complex_parser = subparser.add_parser("complex", aliases=["cx"], help="Complex number operations")
    complex_parser.add_argument("operation", choices=["add", "sub", "mul", "div", "mag", "phase", "polar", "rect"])
    complex_parser.add_argument("c1", type=str, help="First complex number (e.g. '1+2j') or r for rect")
    complex_parser.add_argument("--c2", type=str, help="Second complex number or phi for rect", required=False)

    symbolic_parser = subparser.add_parser("symbolic", aliases=["s"], help="Symbolic math operations")
    symbolic_parser.add_argument("operation", choices=["simplify", "diff", "integrate", "solve", "expand", "factor"])

    symbolic_parser.add_argument("expression", type=str, help="Mathematical expression (e.g. 'x**2 + 2*x + 1')")
    symbolic_parser.add_argument("--variable", type=str, help="Variable for calculus/solving (default: x)", default="x")



    plot_parser = subparser.add_parser("plot", aliases=["pl"], help="Graphing operations")
    plot_parser.add_argument("operation", choices=["plot"])

    plot_parser.add_argument("function", type=str, help="Function to plot (e.g. 'sin(x)')")
    plot_parser.add_argument("--range", type=str, help="X range 'start,end' (default: 0,10)", default="0,10")

    dim_parser = subparser.add_parser("dim", aliases=["d"], help="Dimensional analysis")
    dim_parser.add_argument("operation", choices=["evaluate_dim", "convert_dim"])
    dim_parser.add_argument("expression", type=str, help="Expression with units (e.g. '5 * meter + 30 * centimeter')", nargs="?")


    dim_parser.add_argument("--value", type=float, help="Value for conversion")
    dim_parser.add_argument("--from_unit", type=str, help="Source unit")
    dim_parser.add_argument("--to_unit", type=str, help="Target unit")


    precise_parser = subparser.add_parser("precise", aliases=["pr"], help="Arbitrary precision arithmetic")
    precise_parser.add_argument("operation", choices=["add_fraction", "sub_fraction", "mul_fraction", "div_fraction", "add_decimal", "sub_decimal", "mul_decimal", "div_decimal"])


    precise_parser.add_argument("n1", type=str, help="First number")
    precise_parser.add_argument("n2", type=str, help="Second number")
    precise_parser.add_argument("--precision", type=int, help="Precision for decimal operations (default: 28)", default=28)

    sel_parser = subparser.add_parser("sel", aliases=["sh"], help="Interactive shell")
    sel_parser.add_argument("category", choices=["basic", "adv", "curr", "convert", "vector", "physics", "units"])

 

    try:
        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit(1)

        arguments = parser.parse_args()



        if arguments.command in ["sel", "sh"]:
            run_shell(arguments.category, parser)
        else:
            execute_command(arguments)



    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)



if __name__ == "__main__":
    main()