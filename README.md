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
```bash
bcalc plot plot "sin(x)" --range "0,6.28"
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
Enter the interactive mode to run multiple commands without restarting. The shell now features **smart autocomplete** and **syntax highlighting**.
```bash
bcalc sel basic
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
