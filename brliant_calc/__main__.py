import warnings
warnings.filterwarnings("ignore", message=".*found in sys.modules.*", category=RuntimeWarning)

import argparse
import sys
import shlex
import importlib
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.styles import Style
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.auto_suggest import AutoSuggest, Suggestion
from pygments.lexers.python import PythonLexer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

class safeargparser(argparse.ArgumentParser):
    def error(self, message):
        raise ValueError(message)

def lazy(name):
    return importlib.import_module(f"brliant_calc.{name}")

def execute_command(arguments, user_vars=None):
    try:
        if arguments.command in ["basic", "b"]:
            mod = lazy("basic_ops")
            func = getattr(mod, arguments.operation)
            nums = arguments.numbers
            if arguments.operation == "mod" and len(nums) != 2:
                console.print("[bold red]Error: mod requires exactly two arguments[/bold red]")
                return
            result = func(*nums)
            output = f"{result:g}" if isinstance(result, (int, float)) else str(result)
            console.print(Panel(output, title="Result", expand=False, style="bold green"))

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
                from convert_currency import CurrencyConverter
                c = CurrencyConverter()
                print("Exchange rates are updated automatically by the CurrencyConverter library.")

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
            elif arguments.operation in ["solve", "least_squares", "generalized_eigen", "solve_triangular"]:
                print(func(arguments.m1, arguments.b))
            elif arguments.operation == "sylvester":
                print(func(arguments.m1, arguments.b, arguments.c))
            elif arguments.operation == "power":
                print(func(arguments.m1, arguments.n))
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
            print(func(arguments.function, arguments.range, user_vars))

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

        elif arguments.command in ["convolve", "cnv"]:
            mod = lazy("advanced_ops")
            result = mod.convolve(arguments.signal, arguments.kernel)
            console.print(Panel(str(result), title="Convolution Result", expand=False, style="bold cyan"))

        elif arguments.command in ["numtheory", "nt"]:
            mod = lazy("number_theory")
            func = getattr(mod, arguments.operation)
            result = func(*arguments.args)
            console.print(Panel(str(result), title="Number Theory", expand=False, style="bold green"))

        elif arguments.command in ["combo", "cb"]:
            mod = lazy("combinatorics")
            func = getattr(mod, arguments.operation)
            result = func(*arguments.args)
            console.print(Panel(str(result), title="Combinatorics", expand=False, style="bold green"))

        elif arguments.command in ["stats", "st"]:
            mod = lazy("statistics_ext")
            func = getattr(mod, arguments.operation)
            if arguments.operation in ["correlation", "covariance", "weighted_mean"]:
                args_list = arguments.args
                if arguments.operation == "correlation":
                    mid = len(args_list) // 2
                    result = func(args_list[:mid], args_list[mid:])
                elif arguments.operation == "covariance":
                    mid = len(args_list) // 2
                    result = func(args_list[:mid], args_list[mid:])
                elif arguments.operation == "weighted_mean":
                    mid = len(args_list) // 2
                    result = func(args_list[:mid], args_list[mid:])
                else:
                    result = func(*args_list)
            elif arguments.operation in ["chi_square"]:
                vals = arguments.args
                mid = len(vals) // 2
                result = func(vals[:mid], vals[mid:])
            elif arguments.operation in ["moving_average"]:
                data = arguments.args[:-1]
                window = int(arguments.args[-1])
                result = func(data, window)
            elif arguments.operation in ["confidence_interval"]:
                result = func(*arguments.args)
            else:
                result = func(*arguments.args)
            console.print(Panel(str(result), title="Statistics", expand=False, style="bold green"))

        elif arguments.command in ["geo", "g"]:
            mod = lazy("geometry")
            func = getattr(mod, arguments.operation)
            result = func(*arguments.args)
            console.print(Panel(str(result), title="Geometry", expand=False, style="bold green"))

        elif arguments.command in ["fin", "f"]:
            mod = lazy("financial")
            func = getattr(mod, arguments.operation)
            if arguments.operation == "npv":
                rate = arguments.args[0]
                cashflows = arguments.args[1:]
                result = func(rate, cashflows)
            elif arguments.operation == "payback_period":
                result = func(arguments.args)
            else:
                result = func(*arguments.args)
            console.print(Panel(str(result), title="Financial", expand=False, style="bold green"))

        elif arguments.command in ["signal", "sig"]:
            mod = lazy("signal_processing")
            func = getattr(mod, arguments.operation)
            extra_args = arguments.args if arguments.args else []
            if arguments.operation in ["fft", "ifft", "autocorrelation"]:
                result = func(arguments.signal)
            elif arguments.operation in ["moving_average"]:
                result = func(arguments.signal, int(extra_args[0]) if extra_args else 3)
            elif arguments.operation in ["power_spectrum"]:
                sr = extra_args[0] if extra_args else 1.0
                result = func(arguments.signal, sr)
            elif arguments.operation in ["cross_correlation"]:
                result = func(arguments.signal, arguments.signal2 if arguments.signal2 else arguments.signal)
            elif arguments.operation in ["hamming_window", "hanning_window", "blackman_window"]:
                result = func(int(extra_args[0]) if extra_args else 8)
            elif arguments.operation in ["spectrogram_data"]:
                ws = int(extra_args[0]) if len(extra_args) > 0 else 4
                hs = int(extra_args[1]) if len(extra_args) > 1 else 2
                sr = extra_args[2] if len(extra_args) > 2 else 1.0
                result = func(arguments.signal, ws, hs, sr)
            else:
                result = func(arguments.signal)
            console.print(Panel(str(result), title="Signal Processing", expand=False, style="bold cyan"))

        elif arguments.command in ["calc", "cl"]:
            mod = lazy("calculus")
            func = getattr(mod, arguments.operation)
            if arguments.operation == "taylor_series":
                result = func(arguments.expression, arguments.variable, float(arguments.point), int(arguments.order))
            elif arguments.operation == "numerical_diff":
                result = func(arguments.expression, float(arguments.point), float(arguments.h), arguments.variable)
            elif arguments.operation == "numerical_integrate":
                result = func(arguments.expression, float(arguments.a), float(arguments.b), arguments.variable)
            elif arguments.operation == "series_sum":
                result = func(arguments.expression, int(arguments.start), int(arguments.end), arguments.variable)
            elif arguments.operation == "limit":
                result = func(arguments.expression, float(arguments.point), arguments.variable, arguments.direction)
            elif arguments.operation == "partial_diff":
                vars_list = arguments.variables.split(',') if arguments.variables else ['x']
                result = func(arguments.expression, *vars_list)
            elif arguments.operation == "maclaurin_series":
                result = func(arguments.expression, int(arguments.order), arguments.variable)
            elif arguments.operation == "gradient":
                vars_list = arguments.variables.split(',') if arguments.variables else None
                result = func(arguments.expression, vars_list)
            elif arguments.operation == "jacobian":
                vars_list = arguments.variables.split(',') if arguments.variables else None
                result = func(arguments.expression, vars_list)
            elif arguments.operation == "double_integrate":
                result = func(arguments.expression, arguments.var1, arguments.var2)
            else:
                result = func(arguments.expression, arguments.variable)
            console.print(Panel(str(result), title="Calculus", expand=False, style="bold green"))

        elif arguments.command in ["eqn", "eq"]:
            mod = lazy("equation_solver")
            func = getattr(mod, arguments.operation)
            if arguments.operation == "quadratic":
                result = func(*arguments.args[:3])
            elif arguments.operation == "cubic":
                result = func(*arguments.args[:4])
            elif arguments.operation == "polynomial_roots":
                result = func(arguments.args)
            elif arguments.operation in ["linear_system_2d", "simultaneous_2d"]:
                result = func(*arguments.args[:6])
            elif arguments.operation == "linear_system_3d":
                result = func(*arguments.args[:12])
            elif arguments.operation in ["bisection", "newton_raphson"]:
                result = func(arguments.expression, float(arguments.point))
            elif arguments.operation == "secant_method":
                result = func(arguments.expression, float(arguments.x0), float(arguments.x1))
            else:
                result = func(*arguments.args)
            console.print(Panel(str(result), title="Equation Solver", expand=False, style="bold green"))

        elif arguments.command in ["eval", "ev"]:
            mod = lazy("expression_eval")
            result = mod.evaluate(arguments.expression)
            console.print(Panel(str(result), title="Result", expand=False, style="bold green"))

        elif arguments.command in ["history", "hi"]:
            mod = lazy("history")
            func = getattr(mod, arguments.operation)
            if arguments.operation == "list":
                result = func(int(arguments.limit))
            elif arguments.operation == "recall":
                result = func(arguments.index)
            elif arguments.operation == "search":
                result = func(arguments.query)
            elif arguments.operation == "export":
                result = func(arguments.filepath)
            elif arguments.operation == "clear":
                result = func()
            elif arguments.operation == "stats":
                result = func()
            else:
                result = func()
            console.print(Panel(str(result), title="History", expand=False, style="bold cyan"))

    except Exception as e:
        console.print(f"[bold red]An error has occurred: {e}[/bold red]")

class CommandAutoSuggest(AutoSuggest):
    def __init__(self, commands, arg_map=None, example_map=None):
        self.commands = commands
        self.arg_map = arg_map or {}
        self.example_map = example_map or {}

    def get_suggestion(self, buffer, document):
        text = document.text_before_cursor
        
       
        if ' ' not in text:
            val = text.strip()
            if not val:
                return None
            for cmd in self.commands:
                if cmd.startswith(val):
                    return Suggestion(cmd[len(val):])
            return None
            
        
        parts = text.split()
        if not parts:
            return None
            
        cmd = parts[0]
        if cmd not in self.commands:
            return None
            
        
        if len(parts) == 1 and text.endswith(' '):
            example = self.example_map.get(cmd)
            if example:
                return Suggestion(example)
        
        
        suggestions = self.arg_map.get(cmd, [])
        is_new_arg = text.endswith(' ')
        current_typing = "" if is_new_arg else parts[-1]
        
        for sugg in suggestions:
            if is_new_arg:
                return Suggestion(sugg)
            if sugg.startswith(current_typing) and sugg != current_typing:
                 return Suggestion(sugg[len(current_typing):])
                 
        return None
                 
        return None

def run_shell(category, parser):
  

    
    category_map = {
        'b': 'basic', 'a': 'adv', 'cr': 'curr', 'cv': 'convert', 'v': 'vector', 
        'p': 'physics', 'u': 'units', 'm': 'matrix', 'cx': 'complex', 
        's': 'symbolic', 'pl': 'plot', 'd': 'dim', 'pr': 'precise', 'cnv': 'convolve', 'sh': 'sel',
        'nt': 'numtheory', 'cb': 'combo', 'st': 'stats', 'g': 'geo', 'f': 'fin',
        'sig': 'signal', 'cl': 'calc', 'eq': 'eqn', 'ev': 'eval', 'hi': 'history'
    }
    canonical_category = category_map.get(category, category)

    full_completer_dict = {
        'basic': ['add', 'sub', 'mul', 'div', 'mod'],
        'b': ['add', 'sub', 'mul', 'div', 'mod'],
        'adv': ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'sinh', 'cosh', 'tanh', 'arcsinh', 'arccosh', 'arctanh', 'log', 'log10', 'log2', 'exp', 'sqrt', 'abs', 'nth', 'pow', 'fact', 'floor', 'ceil', 'round', 'trunc', 'sign', 'mean', 'median', 'std', 'var', 'min', 'max', 'sum', 'prod'],
        'a': ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'sinh', 'cosh', 'tanh', 'arcsinh', 'arccosh', 'arctanh', 'log', 'log10', 'log2', 'exp', 'sqrt', 'abs', 'nth', 'pow', 'fact', 'floor', 'ceil', 'round', 'trunc', 'sign', 'mean', 'median', 'std', 'var', 'min', 'max', 'sum', 'prod'],
        'curr': ['upd'],
        'cr': ['upd'],
        'convert': [],
        'cv': [],
        'vector': ['dot_product', 'cross_product', 'magnitude', 'normalize', 'angle_between'],
        'v': ['dot_product', 'cross_product', 'magnitude', 'normalize', 'angle_between'],
        'physics': ['force', 'kinetic_energy', 'potential_energy', 'ohms_law', 'work', 'speed', 'acceleration'],
        'p': ['force', 'kinetic_energy', 'potential_energy', 'ohms_law', 'work', 'speed', 'acceleration'],
        'units': ['length', 'mass', 'temperature', 'time', 'speed'],
        'u': ['length', 'mass', 'temperature', 'time', 'speed'],
        'matrix': ['mul', 'det', 'inv', 'eig', 'transpose', 'rank'],
        'm': ['mul', 'det', 'inv', 'eig', 'transpose', 'rank'],
        'complex': ['add', 'sub', 'mul', 'div', 'mag', 'phase', 'polar', 'rect'],
        'cx': ['add', 'sub', 'mul', 'div', 'mag', 'phase', 'polar', 'rect'],
        'symbolic': ['simplify', 'diff', 'integrate', 'solve', 'expand', 'factor'],
        's': ['simplify', 'diff', 'integrate', 'solve', 'expand', 'factor'],
        'plot': ['plot'],
        'pl': ['plot'],
        'dim': ['evaluate_dim', 'convert_dim'],
        'd': ['evaluate_dim', 'convert_dim'],
        'precise': ['add_fraction', 'sub_fraction', 'mul_fraction', 'div_fraction', 'add_decimal', 'sub_decimal', 'mul_decimal', 'div_decimal'],
        'pr': ['add_fraction', 'sub_fraction', 'mul_fraction', 'div_fraction', 'add_decimal', 'sub_decimal', 'mul_decimal', 'div_decimal'],
        'convolve': ['--kernel'],
        'cnv': ['--kernel'],
        'numtheory': ['is_prime', 'prime_factors', 'gcd', 'lcm', 'fibonacci', 'nth_prime', 'euler_totient', 'catalan', 'binomial', 'mod_inverse', 'prime_sieve', 'digit_sum', 'reverse_number', 'is_palindrome', 'collatz_steps', 'perfect_number_check', 'goldbach_partitions'],
        'nt': ['is_prime', 'prime_factors', 'gcd', 'lcm', 'fibonacci', 'nth_prime', 'euler_totient', 'catalan', 'binomial', 'mod_inverse', 'prime_sieve', 'digit_sum', 'reverse_number', 'is_palindrome', 'collatz_steps', 'perfect_number_check', 'goldbach_partitions'],
        'combo': ['permutation', 'combination', 'multiset_combination', 'derangement', 'stirling_second_kind', 'bell_number', 'partition_count', 'stars_and_bars', 'catalan_number', 'lah_number'],
        'cb': ['permutation', 'combination', 'multiset_combination', 'derangement', 'stirling_second_kind', 'bell_number', 'partition_count', 'stars_and_bars', 'catalan_number', 'lah_number'],
        'stats': ['mode', 'percentile', 'correlation', 'covariance', 'skewness', 'kurtosis', 'geometric_mean', 'harmonic_mean', 'z_score', 'chi_square', 'iqr', 'range_val', 'coefficient_of_variation', 'weighted_mean', 'moving_average', 'confidence_interval'],
        'st': ['mode', 'percentile', 'correlation', 'covariance', 'skewness', 'kurtosis', 'geometric_mean', 'harmonic_mean', 'z_score', 'chi_square', 'iqr', 'range_val', 'coefficient_of_variation', 'weighted_mean', 'moving_average', 'confidence_interval'],
        'geo': ['circle_area', 'circle_circumference', 'sphere_volume', 'sphere_surface_area', 'rectangle_area', 'rectangle_perimeter', 'triangle_area', 'triangle_area_sss', 'cylinder_volume', 'cylinder_surface_area', 'cone_volume', 'cone_surface_area', 'pyramid_volume', 'torus_volume', 'torus_surface_area', 'ellipse_area', 'ellipse_perimeter', 'distance_2d', 'distance_3d', 'midpoint_2d', 'arc_length', 'sector_area'],
        'g': ['circle_area', 'circle_circumference', 'sphere_volume', 'sphere_surface_area', 'rectangle_area', 'rectangle_perimeter', 'triangle_area', 'triangle_area_sss', 'cylinder_volume', 'cylinder_surface_area', 'cone_volume', 'cone_surface_area', 'pyramid_volume', 'torus_volume', 'torus_surface_area', 'ellipse_area', 'ellipse_perimeter', 'distance_2d', 'distance_3d', 'midpoint_2d', 'arc_length', 'sector_area'],
        'fin': ['compound_interest', 'simple_interest', 'emi', 'present_value', 'future_value', 'depreciation_straight_line', 'npv', 'roi', 'payback_period', 'inflation_adjusted_return', 'doubling_time', 'annuity_payment'],
        'f': ['compound_interest', 'simple_interest', 'emi', 'present_value', 'future_value', 'depreciation_straight_line', 'npv', 'roi', 'payback_period', 'inflation_adjusted_return', 'doubling_time', 'annuity_payment'],
        'signal': ['fft', 'ifft', 'moving_average', 'power_spectrum', 'autocorrelation', 'cross_correlation', 'hamming_window', 'hanning_window', 'blackman_window', 'spectrogram_data'],
        'sig': ['fft', 'ifft', 'moving_average', 'power_spectrum', 'autocorrelation', 'cross_correlation', 'hamming_window', 'hanning_window', 'blackman_window', 'spectrogram_data'],
        'calc': ['taylor_series', 'numerical_diff', 'numerical_integrate', 'series_sum', 'limit', 'partial_diff', 'double_integrate', 'maclaurin_series', 'gradient', 'jacobian'],
        'cl': ['taylor_series', 'numerical_diff', 'numerical_integrate', 'series_sum', 'limit', 'partial_diff', 'double_integrate', 'maclaurin_series', 'gradient', 'jacobian'],
        'eqn': ['quadratic', 'cubic', 'polynomial_roots', 'linear_system_2d', 'simultaneous_2d', 'linear_system_3d', 'bisection', 'newton_raphson', 'secant_method'],
        'eq': ['quadratic', 'cubic', 'polynomial_roots', 'linear_system_2d', 'simultaneous_2d', 'linear_system_3d', 'bisection', 'newton_raphson', 'secant_method'],
        'eval': ['evaluate'],
        'ev': ['evaluate'],
        'history': ['list', 'recall', 'search', 'export', 'clear', 'stats'],
        'hi': ['list', 'recall', 'search', 'export', 'clear', 'stats'],
    }
    
   
    CATEGORY_ARG_SUGGESTIONS = {
        'matrix': {
            'mul': ['"[["', '--m2'], 
            'det': ['"[["'],
            'inv': ['"[["'],
            'eig': ['"[["'],
            'transpose': ['"[["'],
            'rank': ['"[["'],
        },
        'plot': {
            'plot': ['--range'],
        },
        'convolve': {
            'convolve': ['--kernel'],
        },
        'complex': {
            'add': ['--c2'],
            'sub': ['--c2'],
            'mul': ['--c2'],
            'div': ['--c2'],
            'rect': ['--c2'],
        },
        'precise': {
             'div_decimal': ['--precision'],
        },
        'dim': {
             'convert_dim': ['--value', '--from_unit', '--to_unit'],
        },
        'symbolic': {
             'diff': ['--variable'],
             'integrate': ['--variable'],
        },
        
        'basic': {},
        'adv': {},
        'vector': {},
        'physics': {},
        'units': {},
        'curr': {},
    }
    
    arg_suggestions = CATEGORY_ARG_SUGGESTIONS.get(canonical_category, {})
 
    CATEGORY_EXAMPLES = {
        'basic': {
            'add': '10 5', 'sub': '10 5', 'mul': '2 3 4', 'div': '10 2', 'mod': '10 3'
        },
        'adv': {
            'sin': '1.57', 'cos': '0', 'tan': '0.785', 'arcsin': '0.5', 'arccos': '0.5', 'arctan': '1',
            'sinh': '1', 'cosh': '0', 'tanh': '0.5', 'arcsinh': '1', 'arccosh': '2', 'arctanh': '0.5',
            'log': '100', 'log10': '100', 'log2': '8', 'exp': '1', 'sqrt': '16', 'abs': '-5',
            'nth': '8 3', 'pow': '2 3', 'fact': '5',
            'floor': '3.7', 'ceil': '3.2', 'round': '3.14159 2', 'trunc': '3.9', 'sign': '-42',
            'mean': '1 2 3 4 5', 'median': '1 2 3 4 5', 'std': '1 2 3 4 5', 'var': '1 2 3',
            'min': '5 2 8 1 9', 'max': '5 2 8 1 9', 'sum': '1 2 3 4 5', 'prod': '2 3 4'
        },
        'vector': {
            'dot_product': '1 2 3 4 5 6', 'cross_product': '1 0 0 0 1 0', 
            'magnitude': '3 4', 'normalize': '3 4', 'angle_between': '1 0 0 1'
        },
        'physics': {
            'force': '10 9.8', 
            'kinetic_energy': '10 5', 
            'potential_energy': '10 5', 
            'ohms_law': '2 10', 
            'work': '10 5', 
            'speed': '100 9.8',
            'acceleration': '10 2 0' 
        },
        'units': {
            'length': '100 meter kilometer', 'mass': '1000 gram kilogram', 
            'temperature': '100 celsius fahrenheit', 'time': '60 minute second', 'speed': '100 km/h m/s'
        },
        'matrix': {
            'mul': '[[1,2],[3,4]] --m2 [[5,6],[7,8]]',
            'det': '[[1,2],[3,4]]',
            'inv': '[[1,2],[3,4]]',
            'eig': '[[1,0],[0,1]]',
            'transpose': '[[1,2],[3,4]]',
            'rank': '[[1,2],[3,4]]'
        },
        'complex': {
            'add': '1+2j --c2 3+4j', 'sub': '1+2j --c2 3+4j', 'mul': '1+2j --c2 3+4j', 
            'div': '1+2j --c2 3+4j', 'mag': '3+4j', 'phase': '1+1j', 
            'polar': '1+1j', 'rect': '1.414 0.785'
        },
        'symbolic': {
            'simplify': 'x**2 + 2*x + 1', 'diff': 'x**2+1 --variable x', 
            'integrate': 'sin(x) --variable x', 'solve': 'x**2-4', 
            'expand': '(x+1)**2', 'factor': 'x**2-1'
        },
        'plot': {
            'plot': 'sin(x) --range 0,10'
        },
        'dim': {
            'evaluate_dim': '5*meter + 30*centimeter',
            'convert_dim': '--value 100 --from_unit km/h --to_unit m/s'
        },
        'precise': {
            'add_fraction': '1/3 1/6', 'sub_fraction': '1/2 1/3', 'mul_fraction': '1/2 1/3', 'div_fraction': '1/2 1/3',
            'add_decimal': '1.1 2.2', 'sub_decimal': '2.2 1.1', 'mul_decimal': '1.1 2.2', 'div_decimal': '1 3 --precision 50'
        },
        'curr': {
            'upd': ''
        },
        'convert': {
        
        }, 
        'convolve': {
             
        },
        'numtheory': {
            'is_prime': '17', 'prime_factors': '60', 'gcd': '12 18 24', 'lcm': '4 6 8',
            'fibonacci': '10', 'nth_prime': '5', 'euler_totient': '12', 'catalan': '5',
            'binomial': '10 3', 'mod_inverse': '3 11', 'prime_sieve': '50',
            'digit_sum': '12345', 'reverse_number': '1234', 'is_palindrome': '12321',
            'collatz_steps': '27', 'perfect_number_check': '28', 'goldbach_partitions': '10'
        },
        'combo': {
            'permutation': '5 3', 'combination': '10 4', 'multiset_combination': '3 5',
            'derangement': '4', 'stirling_second_kind': '5 3', 'bell_number': '5',
            'partition_count': '5', 'stars_and_bars': '10 3', 'catalan_number': '4', 'lah_number': '5 3'
        },
        'stats': {
            'mode': '1 2 2 3 4', 'percentile': '1 2 3 4 5 75', 'correlation': '1 2 3 4 5 2 4 5 4 5',
            'covariance': '1 2 3 2 4 6', 'skewness': '1 2 3 4 5', 'kurtosis': '1 2 3 4 5 6',
            'geometric_mean': '2 4 8', 'harmonic_mean': '1 2 4', 'z_score': '85 75 10',
            'chi_square': '10 20 30 15 25 35', 'iqr': '1 2 3 4 5 6 7',
            'range_val': '3 7 2 9 5', 'coefficient_of_variation': '10 12 14 16',
            'weighted_mean': '80 90 70 0.3 0.5 0.2', 'moving_average': '1 2 3 4 5 3',
            'confidence_interval': '10 12 14 16 18'
        },
        'geo': {
            'circle_area': '5', 'circle_circumference': '5', 'sphere_volume': '3',
            'sphere_surface_area': '3', 'rectangle_area': '5 10', 'rectangle_perimeter': '5 10',
            'triangle_area': '6 4', 'triangle_area_sss': '3 4 5', 'cylinder_volume': '3 10',
            'cylinder_surface_area': '3 10', 'cone_volume': '3 5', 'cone_surface_area': '3 5',
            'pyramid_volume': '20 10', 'torus_volume': '5 2', 'torus_surface_area': '5 2',
            'ellipse_area': '5 3', 'ellipse_perimeter': '5 3', 'distance_2d': '0 0 3 4',
            'distance_3d': '0 0 0 1 2 2', 'midpoint_2d': '0 0 6 8', 'arc_length': '5 90',
            'sector_area': '5 90'
        },
        'fin': {
            'compound_interest': '1000 5 3', 'simple_interest': '1000 5 3', 'emi': '100000 8 12',
            'present_value': '1000 5 3', 'future_value': '1000 5 3',
            'depreciation_straight_line': '10000 2000 5', 'npv': '10 -1000 300 400 500',
            'roi': '1000 1500', 'payback_period': '-5000 1000 1500 2000 2500',
            'inflation_adjusted_return': '8 3', 'doubling_time': '7', 'annuity_payment': '10000 5 12'
        },
        'signal': {
            'fft': '1 2 3 4', 'ifft': '10+0j 0+0j 0+0j 0+0j', 'moving_average': '1 2 3 4 5 2',
            'power_spectrum': '1 2 3 4', 'autocorrelation': '1 2 3 4',
            'cross_correlation': '1 2 3', 'hamming_window': '8', 'hanning_window': '8',
            'blackman_window': '8', 'spectrogram_data': '1 2 3 4 5 6 7 8 4 2'
        },
        'calc': {
            'taylor_series': 'sin(x) --variable x --point 0 --order 6',
            'numerical_diff': 'x**2+1 --point 3 --h 0.0001',
            'numerical_integrate': 'x**2 --a 0 --b 1',
            'series_sum': '1/n**2 --start 1 --end 100',
            'limit': 'sin(x)/x --point 0',
            'partial_diff': 'x**2*y+y**3 --variables x,y',
            'double_integrate': 'x*y --var1 x --var2 y',
            'maclaurin_series': 'exp(x) --order 8',
            'gradient': 'x**2+y**2+z**2 --variables x,y,z',
            'jacobian': 'x*y,y*z --variables x,y,z'
        },
        'eqn': {
            'quadratic': '1 -3 2', 'cubic': '1 -6 11 -6', 'polynomial_roots': '1 -6 11 -6',
            'linear_system_2d': '2 3 8 5 1 11', 'simultaneous_2d': '1 1 3 2 1 5',
            'linear_system_3d': '1 1 1 6 0 2 5 -4 2 5 3 27',
            'bisection': 'x**3-x-2 --point 1', 'newton_raphson': 'x**2-2 --point 1.5',
            'secant_method': 'x**3-x-2 --x0 1 --x1 2'
        },
        'eval': {
            'evaluate': '2**10 + sqrt(144) * sin(pi/2)'
        },
        'history': {
            'list': '--limit 10', 'recall': '--index 1', 'search': '--query add',
            'export': '--filepath history.json', 'clear': '', 'stats': ''
        }
    }
    
    
    command_examples = CATEGORY_EXAMPLES.get(canonical_category, {})
    
    
    valid_commands = full_completer_dict.get(category, [])
   
    valid_commands.extend(['exit', 'quit'])
    
    
    category_completer_dict = {cmd: None for cmd in valid_commands}
    
    completer = NestedCompleter.from_nested_dict(category_completer_dict)
    
    style = Style.from_dict({
        'completion-menu.completion': 'bg:#008888 #ffffff',
        'completion-menu.completion.current': 'bg:#00aaaa #000000',
        'scrollbar.background': 'bg:#88aaaa',
        'scrollbar.button': 'bg:#222222',
        'prompt': '#00ffff bold',
    })
    
    session = PromptSession(
        completer=completer, 
        style=style, 
        lexer=PygmentsLexer(PythonLexer),
        auto_suggest=CommandAutoSuggest(valid_commands, arg_suggestions, command_examples),
        complete_while_typing=False
    )

    console.print(f"[bold cyan]Entering {canonical_category} mode. Type 'exit' to quit.[/bold cyan]")
    
    variables = {}

    while True:
        try:
            line = session.prompt(f"{canonical_category} > ")
            
            if line.strip().lower() in ["exit", "quit"]:
                break
            if not line.strip():
                continue
            
            if line.strip().lower() == "vars":
                if variables:
                    console.print("[bold cyan]Stored Variables:[/bold cyan]")
                    for var, val in variables.items():
                        console.print(f"  {var} = {val}")
                else:
                    console.print("[yellow]No variables stored[/yellow]")
                continue
            
            if '=' in line and not any(op in line for op in ['==', '!=', '<=', '>=']):
                parts = line.split('=', 1)
                var_name = parts[0].strip()
                var_value = parts[1].strip()
                
                try:
                    if var_value.replace('.','',1).replace('-','',1).isdigit():
                        variables[var_name] = float(var_value)
                    else:
                        variables[var_name] = var_value
                    console.print(f"[green]Variable '{var_name}' set to {variables[var_name]}[/green]")
                    continue
                except Exception as e:
                    console.print(f"[red]Error setting variable: {e}[/red]")
                    continue
            
            
            tokens = shlex.split(line)
            substituted_tokens = []
            for token in tokens:
                if token in variables:
                    substituted_tokens.append(str(variables[token]))
                else:
                    substituted_tokens.append(token)
            
            full = [category] + substituted_tokens
            args = parser.parse_args(full)
            execute_command(args, variables)
            
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        except Exception as e:
            console.print(f"[bold red]An error has occurred: {e}[/bold red]")

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
    adv.add_argument("operation", choices=[
        "sin", "cos", "tan", "arcsin", "arccos", "arctan",
        "sinh", "cosh", "tanh", "arcsinh", "arccosh", "arctanh",
        "log", "log10", "log2", "exp", "sqrt", "abs",
        "nth", "pow", "fact",
        "floor", "ceil", "round", "trunc", "sign",
        "mean", "median", "std", "var", "min", "max", "sum", "prod"
    ])
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
    matrix.add_argument("operation", choices=[
        "mul", "det", "inv", "eig", "transpose", "rank",
        "lu", "qr", "cholesky", "svd", "solve", "least_squares",
        "null_space", "condition_number", "exp", "sylvester",
        "generalized_eigen", "power", "det_via_lu", "inv_via_lu",
        "log", "sqrt", "polar", "solve_triangular"
    ])
    matrix.add_argument("m1")
    matrix.add_argument("--m2")
    matrix.add_argument("--b")
    matrix.add_argument("--c")
    matrix.add_argument("--n", type=int)

    comp = sub.add_parser("complex", aliases=["cx"])
    comp.add_argument("operation", choices=["add", "sub", "mul", "div", "mag", "phase", "polar", "rect"])
    comp.add_argument("c1")
    comp.add_argument("--c2")

    sym = sub.add_parser("symbolic", aliases=["s"])
    sym.add_argument("operation", choices=["simplify", "diff", "integrate", "solve", "expand", "factor"])
    sym.add_argument("expression")
    sym.add_argument("--variable", default="x")

    plot = sub.add_parser("plot", aliases=["pl"])
    plot.add_argument("operation", nargs='?', default="plot", choices=["plot"])
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

    cnv = sub.add_parser("convolve", aliases=["cnv"])
    cnv.add_argument("signal", type=float, nargs="+", help="Input signal values")
    cnv.add_argument("--kernel", "-k", type=float, nargs="+", required=True, help="Kernel values for convolution")

    nt = sub.add_parser("numtheory", aliases=["nt"])
    nt.add_argument("operation", choices=[
        "is_prime", "prime_factors", "gcd", "lcm", "fibonacci", "nth_prime",
        "euler_totient", "catalan", "binomial", "mod_inverse", "prime_sieve",
        "digit_sum", "reverse_number", "is_palindrome", "collatz_steps",
        "perfect_number_check", "goldbach_partitions"
    ])
    nt.add_argument("args", type=float, nargs="+")

    cb = sub.add_parser("combo", aliases=["cb"])
    cb.add_argument("operation", choices=[
        "permutation", "combination", "multiset_combination", "derangement",
        "stirling_second_kind", "bell_number", "partition_count",
        "stars_and_bars", "catalan_number", "lah_number"
    ])
    cb.add_argument("args", type=float, nargs="+")

    st = sub.add_parser("stats", aliases=["st"])
    st.add_argument("operation", choices=[
        "mode", "percentile", "correlation", "covariance", "skewness",
        "kurtosis", "geometric_mean", "harmonic_mean", "z_score", "chi_square",
        "iqr", "range_val", "coefficient_of_variation", "weighted_mean",
        "moving_average", "confidence_interval"
    ])
    st.add_argument("args", type=float, nargs="+")

    geo = sub.add_parser("geo", aliases=["g"])
    geo.add_argument("operation", choices=[
        "circle_area", "circle_circumference", "sphere_volume", "sphere_surface_area",
        "rectangle_area", "rectangle_perimeter", "triangle_area", "triangle_area_sss",
        "cylinder_volume", "cylinder_surface_area", "cone_volume", "cone_surface_area",
        "pyramid_volume", "torus_volume", "torus_surface_area", "ellipse_area",
        "ellipse_perimeter", "distance_2d", "distance_3d", "midpoint_2d",
        "arc_length", "sector_area"
    ])
    geo.add_argument("args", type=float, nargs="+")

    fin = sub.add_parser("fin", aliases=["f"])
    fin.add_argument("operation", choices=[
        "compound_interest", "simple_interest", "emi", "present_value",
        "future_value", "depreciation_straight_line", "npv", "roi",
        "payback_period", "inflation_adjusted_return", "doubling_time",
        "annuity_payment"
    ])
    fin.add_argument("args", type=float, nargs="+")

    sig = sub.add_parser("signal", aliases=["sig"])
    sig.add_argument("operation", choices=[
        "fft", "ifft", "moving_average", "power_spectrum", "autocorrelation",
        "cross_correlation", "hamming_window", "hanning_window", "blackman_window",
        "spectrogram_data"
    ])
    sig.add_argument("signal", type=float, nargs="+")
    sig.add_argument("--signal2", type=float, nargs="+")
    sig.add_argument("--args", type=float, nargs="*")

    cl = sub.add_parser("calc", aliases=["cl"])
    cl.add_argument("operation", choices=[
        "taylor_series", "numerical_diff", "numerical_integrate", "series_sum",
        "limit", "partial_diff", "double_integrate", "maclaurin_series",
        "gradient", "jacobian"
    ])
    cl.add_argument("expression")
    cl.add_argument("--variable", default="x")
    cl.add_argument("--point", default="0")
    cl.add_argument("--order", default="6")
    cl.add_argument("--h", default="1e-7")
    cl.add_argument("--a", default="0")
    cl.add_argument("--b", default="1")
    cl.add_argument("--start", default="1")
    cl.add_argument("--end", default="100")
    cl.add_argument("--direction", default="+", choices=["+", "-"])
    cl.add_argument("--variables", default=None)
    cl.add_argument("--var1", default="x")
    cl.add_argument("--var2", default="y")

    eq = sub.add_parser("eqn", aliases=["eq"])
    eq.add_argument("operation", choices=[
        "quadratic", "cubic", "polynomial_roots", "linear_system_2d",
        "simultaneous_2d", "linear_system_3d", "bisection", "newton_raphson",
        "secant_method"
    ])
    eq.add_argument("args", type=float, nargs="*")
    eq.add_argument("--expression")
    eq.add_argument("--point", default="0")
    eq.add_argument("--x0", default="0")
    eq.add_argument("--x1", default="1")

    ev = sub.add_parser("eval", aliases=["ev"])
    ev.add_argument("expression")

    hi = sub.add_parser("history", aliases=["hi"])
    hi.add_argument("operation", choices=["list", "recall", "search", "export", "clear", "stats"])
    hi.add_argument("--limit", default="20")
    hi.add_argument("--index", default="1")
    hi.add_argument("--query", default="")
    hi.add_argument("--filepath", default="history.json")

    sel = sub.add_parser("sel", aliases=["sh"])
    sel.add_argument("category", choices=[
        "basic", "b", 
        "adv", "a", 
        "curr", "cr", 
        "convert", "cv", 
        "vector", "v", 
        "physics", "p", 
        "units", "u",
        "matrix", "m",
        "complex", "cx",
        "symbolic", "s",
        "plot", "pl",
        "dim", "d",
        "precise", "pr",
        "convolve", "cnv",
        "numtheory", "nt",
        "combo", "cb",
        "stats", "st",
        "geo", "g",
        "fin", "f",
        "signal", "sig",
        "calc", "cl",
        "eqn", "eq",
        "eval", "ev",
        "history", "hi"
    ])

    
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
        
        elif sys.argv[1] == "-runtests" or sys.argv[1] == "--runtests":
            import unittest
            import os
            tests_dir = os.path.join(os.path.dirname(__file__), '..', 'tests')
            if not os.path.exists(tests_dir):
                print("Error: tests directory not found")
                sys.exit(1)
            
            loader = unittest.TestLoader()
            suite = loader.discover(tests_dir, pattern='test_*.py')
            runner = unittest.TextTestRunner(verbosity=2)
            result = runner.run(suite)
            sys.exit(0 if result.wasSuccessful() else 1)
        
        elif sys.argv[1] == "-version" or sys.argv[1] == "--version" or sys.argv[1] == "-v":
            try:
                from importlib.metadata import version
                print(f"brliant_calc version {version('brliant_calc')}")
            except Exception:
                print("brliant_calc version 3.0.0")
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
