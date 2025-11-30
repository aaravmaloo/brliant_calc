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

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: Requires `numpy`, `sympy`, `matplotlib`, `pint`.*

## Usage

Run the calculator using `python main.py [command] [arguments]`.

### Basic Operations
```bash
python main.py basic add 10 5
python main.py basic mul 2 3 4
```

### Advanced Math
```bash
python main.py adv sin 1.57
python main.py adv log10 100
```

### Matrix Operations
```bash
python main.py matrix mul "[[1,2],[3,4]]" --m2 "[[5,6],[7,8]]"
python main.py matrix det "[[1,2],[3,4]]"
python main.py matrix inv "[[1,2],[3,4]]"
```

### Complex Numbers
```bash
python main.py complex add "1+2j" --c2 "3+4j"
python main.py complex polar "1+1j"
```

### Symbolic Math
```bash
python main.py symbolic diff "x**2 + 2*x + 1" --variable "x"
python main.py symbolic integrate "sin(x)"
python main.py symbolic solve "x**2 - 4"
```

### Graphing
```bash
python main.py plot plot "sin(x)" --range "0,6.28"
```

### Dimensional Analysis
```bash
python main.py dim evaluate_dim "5 * meter + 30 * centimeter"
python main.py dim convert_dim --value 100 --from_unit "km/h" --to_unit "m/s"
```

### Arbitrary Precision
```bash
python main.py precise add_fraction "1/3" "1/6"
python main.py precise div_decimal "1" "3" --precision 50
```

### Interactive Shell
Enter the interactive mode to run multiple commands without restarting:
```bash
python main.py sel basic
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue.

## License
MIT License
