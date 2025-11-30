import argparse
import sys
import shlex
import importlib

class safeargparser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)

def lazy(name):
    return importlib.import_module(f"brliant_calc.{name}")

def execute_command(arguments):
    try:
        if arguments.command in ["basic", "b"]:
            mod = lazy("basic_ops")
            func = getattr(mod, arguments.operation)
            nums = arguments.numbers
            if arguments.operation == "mod" and len(nums) != 2:
                print("Error: mod requires exactly two arguments")
                return
            result = func(*nums)
            print(f"{result:g}" if isinstance(result, (int, float)) else result)

        elif arguments.command in ["adv", "a"]:
            mod = lazy("advanced_ops")
            func = getattr(mod, arguments.operation)
            try:
                result = func(*arguments.numbers)
            except TypeError as e:
                print(f"Error: {e}")
                return
            print(f"{result:g}" if isinstance(result, (int, float)) else result)

        elif arguments.command in ["curr", "cr"]:
            if arguments.update == "upd":
                from currency_converter.app import get_curr_json
                get_curr_json()
                print("Exchange rates updated successfully.")

        elif arguments.command in ["convert", "cv"]:
            mod = importlib.import_module("brliant_calc.convert_currency")
            result = mod.convert_currency(arguments.from_currency, arguments.to_currency, arguments.amount)
            print(f"{arguments.amount} {arguments.from_currency} = {result:.2f} {arguments.to_currency}")

        elif arguments.command in ["vector", "v"]:
            mod = lazy("vectors")
            func = getattr(mod, arguments.operation)
            comps = arguments.components
            if arguments.operation in ["dot_product", "cross_product", "angle_between"]:
                if len(comps) % 2 != 0:
                    print("Error: Vectors must have the same number of dimensions.")
                    return
                mid = len(comps) // 2
                result = func(comps[:mid], comps[mid:])
            else:
                result = func(comps)
            print(result)

        elif arguments.command in ["physics", "p"]:
            mod = lazy("physics_formulas")
            func = getattr(mod, arguments.operation)
            try:
                result = func(*arguments.args)
            except TypeError as e:
                print(f"Error: {e}")
                return
            print(result)

        elif arguments.command in ["units", "u"]:
            mod = lazy("units")
            func = getattr(mod, arguments.category)
            print(func(arguments.value, arguments.from_unit, arguments.to_unit))

        elif arguments.command in ["matrix", "m"]:
            mod = lazy("matrix_ops")
            func = getattr(mod, arguments.operation)
            if arguments.operation == "mul":
                print(func(arguments.m1, arguments.m2))
            else:
                print(func(arguments.m1))

        elif arguments.command in ["complex", "cx"]:
            mod = lazy("complex_ops")
            func = getattr(mod, arguments.operation)
            if arguments.operation in ["add", "sub", "mul", "div"]:
                print(func(arguments.c1, arguments.c2))
            elif arguments.operation == "rect":
                print(func(arguments.c1, arguments.c2))
            else:
                print(func(arguments.c1))

        elif arguments.command in ["symbolic", "s"]:
            mod = lazy("symbolic_ops")
            func = getattr(mod, arguments.operation)
            if arguments.operation in ["diff", "integrate", "solve"]:
                print(func(arguments.expression, arguments.variable))
            else:
                print(func(arguments.expression))

        elif arguments.command in ["plot", "pl"]:
            mod = lazy("plotting")
            func = getattr(mod, arguments.operation)
            print(func(arguments.function, arguments.range))

        elif arguments.command in ["dim", "d"]:
            mod = lazy("dimensional_analysis")
            func = getattr(mod, arguments.operation)
            if arguments.operation == "evaluate_dim":
                print(func(arguments.expression))
            else:
                print(func(arguments.value, arguments.from_unit, arguments.to_unit))

        elif arguments.command in ["precise", "pr"]:
            mod = lazy("precision_ops")
            func = getattr(mod, arguments.operation)
            if "decimal" in arguments.operation:
                print(func(arguments.n1, arguments.n2, arguments.precision))
            else:
                print(func(arguments.n1, arguments.n2))

    except Exception as e:
        print(f"an error has occurred: {e}")

def run_shell(category, parser):
    print(f"Entering {category} mode. Type 'exit' to quit.")
    while True:
        try:
            line = input(f"{category} > ")
            if line.strip().lower() in ["exit", "quit"]:
                break
            if not line.strip():
                continue
            full = [category] + shlex.split(line)
            args = parser.parse_args(full)
            execute_command(args)
        except ValueError as e:
            print(f"error: {e}")
        except SystemExit:
            pass
        except Exception as e:
            print(f"an error has occurred: {e}")

def main():
    parser = safeargparser(description="A command-line advanced scientific calculator")
    sub = parser.add_subparsers(dest="command")

    basic = sub.add_parser("basic", aliases=["b"])
    basic.add_argument("operation", choices=["add", "sub", "div", "mul", "mod"])
    basic.add_argument("numbers", type=float, nargs="+")
    
    curr = sub.add_parser("curr", aliases=["cr"])
    curr.add_argument("update", choices=["upd"])

    cv = sub.add_parser("convert", aliases=["cv"])
    cv.add_argument("from_currency")
    cv.add_argument("to_currency")
    cv.add_argument("amount", type=float)

    adv = sub.add_parser("adv", aliases=["a"])
    adv.add_argument("operation", choices=["sin", "cos", "tan", "log", "exp", "nth", "pow", "log10", "fact"])
    adv.add_argument("numbers", type=float, nargs="+")

    vec = sub.add_parser("vector", aliases=["v"])
    vec.add_argument("operation", choices=["dot_product", "cross_product", "magnitude", "normalize", "angle_between"])
    vec.add_argument("components", type=float, nargs="+")

    phy = sub.add_parser("physics", aliases=["p"])
    phy.add_argument("operation", choices=["force", "kinetic_energy", "potential_energy", "ohms_law", "work", "speed", "acceleration"])
    phy.add_argument("args", type=float, nargs="+")

    units = sub.add_parser("units", aliases=["u"])
    units.add_argument("category", choices=["length", "mass", "temperature", "time", "speed"])
    units.add_argument("value", type=float)
    units.add_argument("from_unit")
    units.add_argument("to_unit")

    matrix = sub.add_parser("matrix", aliases=["m"])
    matrix.add_argument("operation", choices=["mul", "det", "inv", "eig", "transpose", "rank"])
    matrix.add_argument("m1")
    matrix.add_argument("--m2")

    comp = sub.add_parser("complex", aliases=["cx"])
    comp.add_argument("operation", choices=["add", "sub", "mul", "div", "mag", "phase", "polar", "rect"])
    comp.add_argument("c1")
    comp.add_argument("--c2")

    sym = sub.add_parser("symbolic", aliases=["s"])
    sym.add_argument("operation", choices=["simplify", "diff", "integrate", "solve", "expand", "factor"])
    sym.add_argument("expression")
    sym.add_argument("--variable", default="x")

    plot = sub.add_parser("plot", aliases=["pl"])
    plot.add_argument("operation", choices=["plot"])
    plot.add_argument("function")
    plot.add_argument("--range", default="0,10")

    dim = sub.add_parser("dim", aliases=["d"])
    dim.add_argument("operation", choices=["evaluate_dim", "convert_dim"])
    dim.add_argument("expression", nargs="?")
    dim.add_argument("--value", type=float)
    dim.add_argument("--from_unit")
    dim.add_argument("--to_unit")

    pr = sub.add_parser("precise", aliases=["pr"])
    pr.add_argument("operation", choices=["add_fraction", "sub_fraction", "mul_fraction", "div_fraction", "add_decimal", "sub_decimal", "mul_decimal", "div_decimal"])
    pr.add_argument("n1")
    pr.add_argument("n2")
    pr.add_argument("--precision", type=int, default=28)

    sel = sub.add_parser("sel", aliases=["sh"])
    sel.add_argument("category", choices=["basic", "adv", "curr", "convert", "vector", "physics", "units"])

    # Handle alias management before normal argument parsing
    if len(sys.argv) > 1:
        if sys.argv[1] == "-changeCall" or sys.argv[1] == "--changeCall":
            if len(sys.argv) < 3:
                print("Usage: brliant_calc -changeCall <alias_name>")
                print("Example: brliant_calc -changeCall bcalc")
                sys.exit(1)
            
            from brliant_calc.alias_manager import create_alias
            alias_name = sys.argv[2]
            create_alias(alias_name)
            sys.exit(0)
        
        elif sys.argv[1] == "-removeAlias" or sys.argv[1] == "--removeAlias":
            if len(sys.argv) < 3:
                print("Usage: brliant_calc -removeAlias <alias_name>")
                sys.exit(1)
            
            from brliant_calc.alias_manager import remove_alias
            alias_name = sys.argv[2]
            remove_alias(alias_name)
            sys.exit(0)
        
        elif sys.argv[1] == "-listAliases" or sys.argv[1] == "--listAliases":
            from brliant_calc.alias_manager import list_aliases
            list_aliases()
            sys.exit(0)
    
    try:
        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit(1)
        args = parser.parse_args()
        if args.command in ["sel", "sh"]:
            run_shell(args.category, parser)
        else:
            execute_command(args)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
