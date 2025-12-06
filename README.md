# Brliant Calculator

A powerful, advanced command-line scientific calculator for engineers, scientists, and developers.

## Features

- **Basic Arithmetic**: Addition, subtraction, multiplication, division, modulo.
- **Advanced Math**: Trigonometry, logarithms, exponentials, factorials, powers.
- **Vector Operations**: Dot product, cross product, magnitude, normalization, angle between vectors.
- **Physics Formulas**: Force, kinetic energy, potential energy, Ohm's law, work, speed, acceleration.
- **Unit Conversions**: Length, mass, temperature, time, speed.
- **Currency Conversion**: Real-time currency exchange rates.
- **Matrix Operations**: Multiplication, determinant, inverse, eigenvalues/eigenvectors, transpose, rank.
- **Complex Numbers**: Arithmetic, polar/rectangular conversion, magnitude, phase.
- **Symbolic Math**: Algebraic simplification, differentiation, integration, equation solving.
- **Graphing**: 2D function plotting using Matplotlib.
- **Dimensional Analysis**: Unit-aware calculations and conversions.
- **Arbitrary Precision**: Exact rational arithmetic and high-precision decimal calculations.
- **Interactive Shell**: A dedicated shell mode for continuous calculations.

## Installation

```bash
pip install brliant_calc
```

## Custom Command Aliases

Create custom shortcuts for the calculator command (permanently installed, no PATH modification needed):

```bash

brliant_calc -changeCall bcalc 


brliant_calc -listAliases


brliant_calc -removeAlias bcalc 
```

**Note**: On Windows 11, if you don't have `sudo` installed, you can enable it in Settings → System → For developers → Enable sudo.

## Usage

Run the calculator using (assuming the registered alias is brliant_calc (default)) `brliant_calc <category> <operation> <numbers_sep_by_space>`

In these examples, I will be using the alias bcalc 

### Basic Operations
```bash
bcalc basic add 10 5
bcalc basic mul 2 3 4
```

### Advanced Math
```bash
bcalc adv sin 1.57
bcalc adv log10 100
```

### Matrix Operations
```bash
bcalc matrix mul "[[1,2],[3,4]]" --m2 "[[5,6],[7,8]]"
bcalc matrix det "[[1,2],[3,4]]"
bcalc matrix inv "[[1,2],[3,4]]"
```

### Complex Numbers
```bash
bcalc complex add "1+2j" --c2 "3+4j"
bcalc complex polar "1+1j"
```

### Symbolic Math
```bash
bcalc symbolic diff "x**2 + 2*x + 1" --variable "x"
bcalc symbolic integrate "sin(x)"
bcalc symbolic solve "x**2 - 4"
```

### Graphing

The plotting module uses a **secure AST parser** (no `eval()`) that supports nested expressions, mathematical functions, and constants.

> **⚠️ Important for Windows/PowerShell Users:**  
> Always wrap expressions in **double quotes** (`"`) to avoid shell parsing errors!

**Basic Plot:**
```bash
bcalc plot "sin(x)" --range "0,6.28"
```

**Nested Expressions:**
```bash

bcalc plot "sin(x**2 + pi)" --range "0,10"


bcalc plot "exp(-x) * cos(2*pi*x)" --range "0,5"


bcalc plot "log(x**2 + 1)" --range "0,10"


bcalc plot "sin(x) + cos(2*x)" --range "0,6.28"
bcalc plot "x**3 - 2*x**2 + x" --range "-2,3"
bcalc plot "sqrt(abs(x)) * sin(x)" --range "0,10"
```

**More Examples:**
```bash

bcalc plot "exp(-x/5)" --range "0,20"


bcalc plot "exp(-x**2)" --range "-3,3"


bcalc plot "sinh(x)" --range "-2,2"
bcalc plot "tanh(x)" --range "-5,5"


bcalc plot "sin(x) * cos(x)" --range "0,6.28"
bcalc plot "abs(sin(x))" --range "0,10"
```

**Supported Functions:**
- Trigonometric: `sin`, `cos`, `tan`, `arcsin`, `arccos`, `arctan`
- Hyperbolic: `sinh`, `cosh`, `tanh`
- Exponential/Log: `exp`, `log`, `log10`, `sqrt`
- Other: `abs`

**Constants:**
- `pi` (3.14159...)
- `e` (2.71828...)

**Variable:**
- `x` (plotting variable)

**Interactive Mode:**
```bash
bcalc sel plot
plot > plot sin(x) --range 0,6.28
plot > plot exp(-x) * cos(2*pi*x) --range 0,5
plot > exit
```

### Dimensional Analysis
```bash
bcalc dim evaluate_dim "5 * meter + 30 * centimeter"
bcalc dim convert_dim --value 100 --from_unit "km/h" --to_unit "m/s"
```

### Arbitrary Precision
```bash
bcalc precise add_fraction "1/3" "1/6"
bcalc precise div_decimal "1" "3" --precision 50
```

### Convolutions
```bash
bcalc convolve 1 2 3 -k 0.5 0.5
```

### Interactive Shell

Enter interactive mode for a modern shell experience with **smart autocomplete**, **syntax highlighting**, **inline suggestions**, and **variable storage**.

**Features:**
- **Context-Aware Suggestions**: Only shows commands valid for the current mode
- **Inline Ghost Text**: See complete usage examples as you type
- **Smart Argument Completion**: Suggests flags and structures (e.g., `[[` for matrices, `--range` for plots)
- **Right Arrow to Accept**: Press → to accept suggestions
- **Variable Storage**: Define variables that persist throughout your session

**Variable Storage:**
```bash
bcalc sel plot
plot > a = 2
Variable 'a' set to 2.0
plot > b = 3.14
Variable 'b' set to 3.14
plot > plot sin(a*x + b) --range 0,10
Plot displayed.
plot > vars
Stored Variables:
  a = 2.0
  b = 3.14
plot > exit
```

Variables are stored in memory until you exit the shell mode. You can use them in:
- Plot expressions: `plot sin(a*x)`, `plot x**2 + a*x + b`
- Any calculations within the session

**Example:**
```bash
bcalc sel matrix
matrix > mul 
```
When you type `mul ` and wait, you'll see a ghost text suggestion: `[[1,2],[3,4]] --m2 [[5,6],[7,8]]`

**Available Modes:**
```bash
bcalc sel basic      # Basic arithmetic
bcalc sel adv        # Advanced math (sin, cos, log, etc.)
bcalc sel matrix     # Matrix operations
bcalc sel complex    # Complex numbers
bcalc sel symbolic   # Symbolic math
bcalc sel plot       # Function plotting
bcalc sel vector     # Vector operations
bcalc sel physics    # Physics calculations
bcalc sel units      # Unit conversions
bcalc sel dim        # Dimensional analysis
bcalc sel precise    # Arbitrary precision
```

## Shortcuts
You can use the following short aliases for commands:
- `basic` -> `b`
- `adv` -> `a`
- `curr` -> `cr`
- `convert` -> `cv`
- `vector` -> `v`
- `physics` -> `p`
- `units` -> `u`
- `matrix` -> `m`
- `complex` -> `cx`
- `symbolic` -> `s`
- `plot` -> `pl`
- `dim` -> `d`
- `precise` -> `pr`
- `sel` -> `sh`

Example: `bcalc b add 1 2` is the same as `bcalc basic add 1 2`.


## Contributing
Contributions are welcome! Please submit a pull request or open an issue.

## License
MIT License
