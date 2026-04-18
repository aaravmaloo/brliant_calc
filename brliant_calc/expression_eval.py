import ast
import math
import operator


SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.FloorDiv: operator.floordiv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

SAFE_FUNCTIONS = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
    "exp": math.exp, "log": math.log, "log10": math.log10,
    "log2": math.log2, "sqrt": math.sqrt, "abs": abs,
    "ceil": math.ceil, "floor": math.floor,
    "round": round, "factorial": math.factorial,
    "gcd": math.gcd, "degrees": math.degrees, "radians": math.radians,
    "perm": math.perm, "comb": math.comb,
}

SAFE_CONSTANTS = {
    "pi": math.pi, "e": math.e, "tau": math.tau,
    "inf": math.inf,
}


def _eval_node(node):
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.Name):
        if node.id in SAFE_CONSTANTS:
            return SAFE_CONSTANTS[node.id]
        raise ValueError(f"Unknown variable or constant: {node.id}")
    elif isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type in SAFE_OPERATORS:
            return SAFE_OPERATORS[op_type](_eval_node(node.left), _eval_node(node.right))
        raise ValueError(f"Unsupported operator: {op_type}")
    elif isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type in SAFE_OPERATORS:
            return SAFE_OPERATORS[op_type](_eval_node(node.operand))
        raise ValueError(f"Unsupported unary operator: {op_type}")
    elif isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Function calls must be simple names")
        func_name = node.func.id
        if func_name in SAFE_FUNCTIONS:
            args = [_eval_node(arg) for arg in node.args]
            return SAFE_FUNCTIONS[func_name](*args)
        raise ValueError(f"Unknown function: {func_name}")
    else:
        raise ValueError(f"Unsupported expression type: {type(node)}")


def evaluate(expression):
    try:
        tree = ast.parse(expression.strip(), mode='eval')
        result = _eval_node(tree.body)
        return result
    except SyntaxError as e:
        return f"Syntax error: {e}"
    except Exception as e:
        return f"Error: {e}"

def evaluate_with_vars(expression, variables=None):
    if variables is None:
        variables = {}
    all_constants = {**SAFE_CONSTANTS, **variables}

    def _eval_with_vars(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Name):
            if node.id in all_constants:
                return all_constants[node.id]
            raise ValueError(f"Unknown variable: {node.id}")
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type in SAFE_OPERATORS:
                return SAFE_OPERATORS[op_type](_eval_with_vars(node.left), _eval_with_vars(node.right))
            raise ValueError(f"Unsupported operator: {op_type}")
        elif isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type in SAFE_OPERATORS:
                return SAFE_OPERATORS[op_type](_eval_with_vars(node.operand))
            raise ValueError(f"Unsupported unary operator: {op_type}")
        elif isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Function calls must be simple names")
            func_name = node.func.id
            if func_name in SAFE_FUNCTIONS:
                args = [_eval_with_vars(arg) for arg in node.args]
                return SAFE_FUNCTIONS[func_name](*args)
            raise ValueError(f"Unknown function: {func_name}")
        else:
            raise ValueError(f"Unsupported expression type: {type(node)}")

    try:
        tree = ast.parse(expression.strip(), mode='eval')
        result = _eval_with_vars(tree.body)
        return result
    except Exception as e:
        return f"Error: {e}"
