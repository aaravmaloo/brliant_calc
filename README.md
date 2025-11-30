# Brliant Calculator

**Brliant Calculator** is a powerful, high-performance command-line interface (CLI) scientific calculator designed for developers, engineers, and power users who demand speed and efficiency.

Unlike traditional GUI calculators that require slow point-and-click interactions, Brliant Calculator allows you to perform complex calculations, vector math, physics simulations, and unit conversions instantly using simple keyboard commands. Once you master the syntax, it becomes significantly faster than any standard calculator app.

## Why Brliant Calculator?

*   **Speed**: Keep your hands on the keyboard. No mouse required.
*   **Efficiency**: Chain commands and process arguments faster than you can type them into a GUI.
*   **Power**: Built-in support for advanced mathematics, linear algebra (vectors), physics formulas, and real-time currency conversion.
*   **Scriptable**: easy to integrate into shell scripts or batch processes.

## Installation

Ensure you have Python installed. You will need `numpy` for vector and advanced math operations; Install CurrencyConverter for currency conversion.

```bash
pip install numpy
pip install CurrencyConverter
```

## Usage Guide

The general syntax is:
```bash
python main.py <category> <operation> [arguments...]
```

You can always append `--help` to any command to see available options.

### 1. Basic Arithmetic
Perform standard arithmetic operations with multiple numbers.

**Command:** `basic`
**Operations:** `add`, `sub`, `div`, `mul`, `mod`

Add numbers:
```bash
python main.py basic add 10 5 2
```

Multiply numbers:
```bash
python main.py basic mul 4 5 2
```

### 2. Advanced Mathematics
Access scientific functions including trigonometry, logarithms, and exponentials.

**Command:** `adv`
**Operations:** `sin`, `cos`, `tan`, `log` (ln), `log10`, `exp`, `pow`, `nth` (nth root), `fact` (factorial)

Calculate sine of 90 degrees (input in radians):
```bash
python main.py adv sin 1.5708
```

Calculate 2 to the power of 3:
```bash
python main.py adv pow 2 3
```

Calculate factorial of 5:
```bash
python main.py adv fact 5
```

### 3. Vector Operations
Perform linear algebra operations on vectors of any dimension (using `numpy`).

**Command:** `vector`
**Operations:** `dot_product`, `cross_product`, `magnitude`, `normalize`, `angle_between`

Calculate dot product of vectors [1, 2] and [3, 4]:
```bash
python main.py vector dot_product 1 2 3 4
```

Calculate magnitude of vector [3, 4]:
```bash
python main.py vector magnitude 3 4
```

Calculate angle between two vectors:
```bash
python main.py vector angle_between 1 0 0 1
```

### 4. Physics Formulas
Quickly solve common physics problems.

**Command:** `physics`
**Operations:** `force`, `kinetic_energy`, `potential_energy`, `ohms_law`, `work`, `speed`, `acceleration`

Calculate Force (F = ma):
```bash
python main.py physics force 10 5
```

Calculate Kinetic Energy:
```bash
python main.py physics kinetic_energy 50 10
```

### 5. Unit Conversions
Convert between metric and imperial units instantly.

**Command:** `units`
**Categories:** `length`, `mass`, `temperature`, `time`, `speed`

**Syntax:** `python main.py units <category> <value> <from_unit> <to_unit>`

Convert 5 kilometers to miles:
```bash
python main.py units length 5 km miles
```

Convert 100 Celsius to Fahrenheit:
```bash
python main.py units temperature 100 C F
```

### 6. Currency Conversion
Convert currencies using real-time exchange rates.

Update Rates:
```bash
python main.py curr upd
```

Convert 100 USD to INR:
```bash
python main.py convert USD INR 100
```

### 7. Select Function
For ease of use, you can type bcalc sel category_of_command to enter a shell mode that accepts commands that the category offers.
For example
``` bash
bcalc sel adv
adv > sin 1.5708
adv > cos 1.5708
(the shell keeps accepting calculations)
adv > exit (for exiting press q)
```

## Contributing
To contribute to this project, please fork this repo and create a pull request. If you want to be added as a contributor, please open an issue or contact me at [aaravmaloo06@gmail.com](mailto:aaravmaloo06@gmail.com).


## Help
To see a full list of commands and options:
```bash
python main.py --help
```
For specific module help:
```bash
python main.py vector --help
```
