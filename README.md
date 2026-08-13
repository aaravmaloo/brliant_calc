# Brliant Calculator

Once you learn the syntax, Brliant Calculator becomes **significantly faster** than traditional GUI calculators or reaching for your mouse.

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-3.0.0-brightgreen.svg)]()

---

## Quick Start

### Installation

```bash
pip install brliant_calc
```

### Examples

```bash
bcalc basic add 5 10 15
bcalc adv sin 1.57
bcalc adv mean 10 20 30 40 50
bcalc eval "2**10 + sqrt(144) * sin(pi/2)"
bcalc nt is_prime 17
bcalc g circle_area 5
```

### Create a Custom Alias

Make it even faster by creating a short alias:

```bash
bcalc -changeCall bc
```

---

## Core Features

### **Comprehensive Mathematics**

**Basic Arithmetic**
```bash
bcalc basic add 10 5 3         
bcalc basic mul 2 3 4         
bcalc basic div 100 4        
```

**Trigonometry & Hyperbolic Functions**
```bash
bcalc adv sin 1.57           
bcalc adv arcsin 0.5          
bcalc adv sinh 1              
```

**Logarithms & Exponentials**
```bash
bcalc adv log 100              
bcalc adv log10 1000          
bcalc adv log2 256            
bcalc adv exp 2               
```

**Statistics**
```bash
bcalc adv mean 10 20 30 40     
bcalc adv std 2 4 6 8 10       
bcalc adv median 1 3 5 7 9   
bcalc adv max 15 42 8 23        
```

**Rounding & Precision**
```bash
bcalc adv floor 3.7             
bcalc adv ceil 3.2              
bcalc adv round 3.14159 2       
bcalc adv sqrt 256              
```

### **Matrix Operations**

```bash
bcalc matrix mul "[[1,2],[3,4]]" --m2 "[[5,6],[7,8]]"
bcalc matrix det "[[1,2],[3,4]]"
bcalc matrix inv "[[1,2],[3,4]]"
bcalc matrix eig "[[1,2],[3,4]]"
```

### **Complex Numbers**

```bash
bcalc complex add "1+2j" --c2 "3+4j"        
bcalc complex mul "2+3j" --c2 "1-1j"        
bcalc complex polar "1+1j"                   
bcalc complex mag "3+4j"                     
```

### **Function Plotting**

Visualize mathematical functions with secure AST parsing:

```bash
bcalc plot "sin(x)" --range "0,6.28"
bcalc plot "sin(x**2 + pi)" --range "0,10"
bcalc plot "exp(-x) * cos(2*pi*x)" --range "0,5"
bcalc plot "x**3 - 2*x**2 + x" --range "-2,3"
```

**Supported Functions**: `sin`, `cos`, `tan`, `exp`, `log`, `sqrt`, `abs`, and all hyperbolic variants  
**Constants**: `pi`, `e`

### **Symbolic Mathematics**

```bash
bcalc symbolic diff "x**2 + 2*x + 1" --variable x
bcalc symbolic integrate "sin(x)" --variable x
bcalc symbolic solve "x**2 - 4" --variable x
bcalc symbolic simplify "(x+1)**2"
```

### **Unit Conversions**

```bash
bcalc units length 1000 meter kilometer     
bcalc units temperature 100 celsius fahrenheit 
bcalc units mass 1 kilogram pound           
```

### **Currency Conversion**

```bash
bcalc curr upd
bcalc convert USD EUR 100
```

---

## New Features (v4.1) 

### 1. **Number Theory** (`numtheory` / `nt`)

Primality, factorization, and integer math:

```bash
bcalc nt is_prime 17              # True
bcalc nt prime_factors 60          # [2, 2, 3, 5]
bcalc nt gcd 12 18 24             # 6
bcalc nt lcm 4 6 8                # 24
bcalc nt fibonacci 10             # 55
bcalc nt nth_prime 5              # 11
bcalc nt euler_totient 12         # 4
bcalc nt catalan 5                # 42
bcalc nt binomial 10 3           # 120
bcalc nt mod_inverse 3 11         # 4
bcalc nt prime_sieve 50           # all primes up to 50
bcalc nt digit_sum 12345          # 15
bcalc nt is_palindrome 12321      # True
bcalc nt collatz_steps 27         # 111
bcalc nt perfect_number_check 28  # True
bcalc nt goldbach_partitions 10   # [(3, 7), (5, 5)]
```

### 2. **Combinatorics** (`combo` / `cb`)

Counting, arrangements, and partitions:

```bash
bcalc cb permutation 5 3           # 60
bcalc cb combination 10 4          # 210
bcalc cb multiset_combination 3 5  # 35
bcalc cb derangement 4             # 9
bcalc cb stirling_second_kind 5 3  # 25
bcalc cb bell_number 5             # 52
bcalc cb partition_count 5         # 7
bcalc cb stars_and_bars 10 3       # 66
bcalc cb catalan_number 4          # 14
bcalc cb lah_number 5 3            # 120
```

### 3. **Extended Statistics** (`stats` / `st`)

Advanced descriptive and inferential stats:

```bash
bcalc st mode 1 2 2 3 4                    # 2
bcalc st percentile 1 2 3 4 5 75            # 75th percentile
bcalc st correlation 1 2 3 4 5 2 4 5 4 5   # Pearson r
bcalc st covariance 1 2 3 2 4 6             # sample covariance
bcalc st skewness 1 2 3 4 5                # distribution skewness
bcalc st kurtosis 1 2 3 4 5 6              # excess kurtosis
bcalc st geometric_mean 2 4 8              # 4.0
bcalc st harmonic_mean 1 2 4               # 1.714
bcalc st z_score 85 75 10                  # (85-75)/10 = 1.0
bcalc st chi_square 10 20 30 15 25 35      # chi-squared statistic
bcalc st iqr 1 2 3 4 5 6 7                 # interquartile range
bcalc st range_val 3 7 2 9 5               # 7
bcalc st coefficient_of_variation 10 12 14 16
bcalc st weighted_mean 80 90 70 0.3 0.5 0.2
bcalc st moving_average 1 2 3 4 5 3        # 3-period moving avg
bcalc st confidence_interval 10 12 14 16 18 # 95% CI
```

### 4. **Geometry** (`geo` / `g`)

Shapes, distances, and spatial calculations:

```bash
bcalc g circle_area 5                # 78.54
bcalc g circle_circumference 5       # 31.42
bcalc g sphere_volume 3              # 113.1
bcalc g sphere_surface_area 3        # 113.1
bcalc g rectangle_area 5 10          # 50
bcalc g rectangle_perimeter 5 10     # 30
bcalc g triangle_area 6 4            # 12
bcalc g triangle_area_sss 3 4 5      # 6 (Heron's formula)
bcalc g cylinder_volume 3 10         # 282.7
bcalc g cylinder_surface_area 3 10
bcalc g cone_volume 3 5
bcalc g cone_surface_area 3 5
bcalc g pyramid_volume 20 10
bcalc g torus_volume 5 2
bcalc g torus_surface_area 5 2
bcalc g ellipse_area 5 3
bcalc g ellipse_perimeter 5 3
bcalc g distance_2d 0 0 3 4          # 5.0
bcalc g distance_3d 0 0 0 1 2 2      # 3.0
bcalc g midpoint_2d 0 0 6 8          # (3, 4)
bcalc g arc_length 5 90
bcalc g sector_area 5 90
```

### 5. **Financial Math** (`fin` / `f`)

Interest, loans, investments, and depreciation:

```bash
bcalc f compound_interest 1000 5 3        # compound interest
bcalc f simple_interest 1000 5 3          # simple interest
bcalc f emi 100000 8 12                   # monthly EMI
bcalc f present_value 1000 5 3            # PV of future amount
bcalc f future_value 1000 5 3             # FV of present amount
bcalc f depreciation_straight_line 10000 2000 5
bcalc f npv 10 -1000 300 400 500          # net present value
bcalc f roi 1000 1500                      # return on investment
bcalc f payback_period -5000 1000 1500 2000 2500
bcalc f inflation_adjusted_return 8 3
bcalc f doubling_time 7                    # years to double
bcalc f annuity_payment 10000 5 12
```

### 6. **Signal Processing** (`signal` / `sig`)

FFT, correlations, windows, and spectral analysis:

```bash
bcalc sig fft 1 2 3 4                      # Fast Fourier Transform
bcalc sig ifft 10 0 0 0                    # Inverse FFT
bcalc sig moving_average 1 2 3 4 5 --args 3
bcalc sig power_spectrum 1 2 3 4           # frequency vs power
bcalc sig autocorrelation 1 2 3 4          # self-correlation
bcalc sig cross_correlation 1 2 3 --signal2 2 3 4
bcalc sig hamming_window --args 8           # Hamming window
bcalc sig hanning_window --args 8           # Hanning window
bcalc sig blackman_window --args 8          # Blackman window
bcalc sig spectrogram_data 1 2 3 4 5 6 7 8 --args 4 2
```

### 7. **Calculus** (`calc` / `cl`)

Taylor series, numerical methods, limits, and multivariate:

```bash
bcalc cl taylor_series "sin(x)" --variable x --point 0 --order 6
bcalc cl numerical_diff "x**2+1" --point 3 --h 0.0001
bcalc cl numerical_integrate "x**2" --a 0 --b 1
bcalc cl series_sum "1/n**2" --start 1 --end 100 --variable n
bcalc cl limit "sin(x)/x" --point 0
bcalc cl partial_diff "x**2*y+y**3" --variables x,y
bcalc cl double_integrate "x*y" --var1 x --var2 y
bcalc cl maclaurin_series "exp(x)" --order 8
bcalc cl gradient "x**2+y**2+z**2" --variables x,y,z
bcalc cl jacobian "x*y,y*z" --variables x,y,z
```

### 8. **Equation Solver** (`eqn` / `eq`)

Algebraic and numerical root finding:

```bash
bcalc eq quadratic 1 -3 2                    # x²-3x+2=0 → x=1,2
bcalc eq cubic 1 -6 11 -6                    # x³-6x²+11x-6=0
bcalc eq polynomial_roots 1 -6 11 -6         # from coefficients
bcalc eq linear_system_2d 2 3 8 5 1 11      # 2x+3y=8, 5x+y=11
bcalc eq simultaneous_2d 1 1 3 2 1 5        # x+y=3, 2x+y=5
bcalc eq linear_system_3d 1 1 1 6 0 2 5 -4 2 5 3 27
bcalc eq bisection "x**3-x-2" --point 1     # numerical root
bcalc eq newton_raphson "x**2-2" --point 1.5
bcalc eq secant_method "x**3-x-2" --x0 1 --x1 2
```

### 9. **Expression Evaluator** (`eval` / `ev`)

Direct math expression evaluation with safe AST parsing:

```bash
bcalc ev "2**10 + sqrt(144) * sin(pi/2)"     # 1024 + 12 = 1036
bcalc ev "factorial(5) + comb(10,3)"          # 120 + 120 = 240
bcalc ev "log(e) + log10(100)"                # 1 + 2 = 3
bcalc ev "gcd(12,8) * lcm(4,6)"              # 4 * 12 = 48
```

**Supported**: All standard math functions (`sin`, `cos`, `sqrt`, `log`, `exp`, ...), constants (`pi`, `e`, `tau`), operators (`+`, `-`, `*`, `/`, `**`, `//`, `%`), and `factorial`, `gcd`, `comb`, `perm`.

### 10. **Calculation History** (`history` / `hi`)

Persistent history with search, export, and stats:

```bash
bcalc hi list --limit 10          # show last 10 entries
bcalc hi recall --index 1        # recall specific entry
bcalc hi search --query "add"     # search by keyword
bcalc hi export --filepath out.json  # export to JSON
bcalc hi clear                    # wipe history
bcalc hi stats                    # usage statistics
```

---

## New in v3.1 — Scientific Expansion

### 11. **Probability & Distributions** (`prob` / `pb`)

PDFs, CDFs, and statistical tests:

```bash
bcalc pb normal_pdf 0 --mu 0 --sigma 1     # standard normal PDF
bcalc pb normal_cdf 1.96                   # ~0.975
bcalc pb binomial_pmf 5 10 0.5            # 5 heads in 10 flips
bcalc pb poisson_pmf 2 3                   # k=2, lambda=3
bcalc pb exponential_pdf 1 2               # x=1, lambda=2
bcalc pb t_test_1samp 1 2 3 4 5 3.0        # data... popmean
bcalc pb t_test_ind 1 2 3 2 3 4            # group1... group2
bcalc pb sample_normal 10 0 1              # 10 random samples
```

### 12. **Digital Logic** (`logic` / `lg`)

Base conversions and boolean algebra:

```bash
bcalc lg base_convert 255 10 16            # FF
bcalc lg base_convert 1010 2 10            # 10
bcalc lg truth_table "A & (B | C)"         # generate full table
bcalc lg simplify_boolean "A & A | B"      # A | B
bcalc lg bitwise_and 12 7                  # 4
bcalc lg bitwise_xor 12 7                  # 11
```

### 13. **Information Theory** (`info` / `it`)

Entropy and distance metrics:

```bash
bcalc it shannon_entropy 0.5 0.5           # 1.0 bit
bcalc it kl_divergence 0.5 0.5 0.1 0.9     # relative entropy
bcalc it hamming_distance 1011 1101        # 2
bcalc it levenshtein_distance kitten sitting # 3
bcalc it cross_entropy 0.5 0.5 0.4 0.6
bcalc it mutual_information "[[0.25, 0.25], [0.25, 0.25]]"
```

### 14. **Numerical Analysis** (`numerical` / `nm`)

Interpolation and ODE solvers:

```bash
bcalc nm polynomial_fit 1 2 3 1 4 9 2      # x... y... degree
bcalc nm lagrange_interpolation 1 2 3 1 4 9 2.5
bcalc nm cubic_spline_interpolation 1 2 3 4 1 8 27 64 2.5
bcalc nm rk4_solve --func_str "t*y" --y0 1 --t_start 0 --t_end 1 --steps 10
bcalc nm newton_interpolation 1 2 3 1 4 9 2.5
```

### 15. **Chemistry** (`chemistry` / `ch`)

Molar mass and gas laws:

```bash
bcalc ch molar_mass H2O                    # 18.015
bcalc ch molar_mass H2SO4                  # 98.079
bcalc ch ideal_gas_law --p 1 --v 22.4 --n 1 # Solve for T
bcalc ch molarity 0.5 2.0                  # 0.25 M
bcalc ch ph_from_h 1e-7                    # 7.0
bcalc ch h_from_ph 3.0                     # 0.001

# Solution chemistry, stoichiometry & kinetics
bcalc ch dilution 6 0.5 1.5                # M1V1=M2V2 → V2 = 2.0
bcalc ch molality 2 0.5                    # 4.0 mol/kg
bcalc ch mole_fraction 2 3                 # 0.4
bcalc ch limiting_reagent 10 2 6 1         # reagent 1 limiting
bcalc ch percent_yield 8 10                # 80.0%
bcalc ch boiling_point_elevation 0.5 0.512 # 0.256 °C
bcalc ch freezing_point_depression 0.5 1.86
bcalc ch osmotic_pressure 0.1 298          # Π = MRT (atm)
bcalc ch henderson_hasselbalch 4.76 10     # pH = pKa + log10(ratio)
bcalc ch half_life 0.1                     # t½ = ln(2)/k
bcalc ch radioactive_decay 100 0.1 5       # N = N₀·e^(-kt)
bcalc ch density 50 25                     # 2.0 g/mL
bcalc ch ppm_to_concentration 100 58.44    # 0.001711 mol/L
bcalc ch molarity_to_ppm 0.1 58.44         # 5844 ppm
```

**Note**: `limiting_reagent` takes alternating (amount, coefficient) pairs, e.g. `10 2 6 1` means reagent 1 has 10 mol with coefficient 2, reagent 2 has 6 mol with coefficient 1. `osmotic_pressure` expects temperature in Kelvin.

### 16. **Date & Time** (`datetime` / `dt`)

Date arithmetic, weekdays, and calendar math:

```bash
bcalc dt add_days 2024-01-15 30            # 2024-02-14
bcalc dt add_days today -7                 # one week ago
bcalc dt add_months 2024-01-31 1           # 2024-02-29 (clamped)
bcalc dt diff_days 2024-01-01 2024-12-31   # 365 (date2 - date1)
bcalc dt day_of_week 2024-07-04            # Thursday
bcalc dt age 2000-01-01                    # age in whole years
bcalc dt julian_day 2000-01-01              # 2451545
bcalc dt is_leap_year 2024                 # True
bcalc dt week_number 2024-01-01            # 1 (ISO week)
```

**Date formats**: `YYYY-MM-DD` (also `YYYY/MM/DD`, `DD-MM-YYYY`, `DD/MM/YYYY`, `MM/DD/YYYY`) or the keyword `today`.

---

## Interactive Shell Mode

```bash
bcalc sel basic
basic > x = 5
Variable 'x' set to 5.0
basic > y = 120
Variable 'y' set to 120.0
basic > mul x y
600
basic > div x y
0.0416667
basic > vars
Stored Variables:
  x = 5.0
  y = 120.0
basic > exit
```

### Variable Storage

Define variables once, use them everywhere:

```bash
bcalc sel plot
plot > a = 2
plot > b = 3.14
plot > plot sin(a*x + b) --range 0,10
Plot displayed.
```

Variables work in **all modes**:
- Arithmetic: `mul x y`, `add a b c`
- Advanced math: `sin x`, `pow x 2`
- Plotting: `sin(a*x)`, `x**2 + b*x + c`

## Advanced Examples

### Physics Calculations

```bash
bcalc physics force 10 9.8              
bcalc physics kinetic_energy 5 10       
bcalc physics ohms_law 2 10             
```

### Vector Operations

```bash
bcalc vector dot_product 1 2 3 4 5 6    
bcalc vector cross_product 1 0 0  0 1 0 
bcalc vector magnitude 3 4             
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

---

## Command Aliases

Create shorter commands:

```bash
bcalc -changeCall bc
bc basic add 5 10
bc adv sin 1.57
bcalc -listAliases
bcalc -removeAlias bc
```

---

## Shortcuts

| Command | Shortcut |
|---------|----------|
| `basic` | `b` |
| `adv` | `a` |
| `matrix` | `m` |
| `complex` | `cx` |
| `symbolic` | `s` |
| `plot` | `pl` |
| `vector` | `v` |
| `physics` | `p` |
| `units` | `u` |
| `dim` | `d` |
| `precise` | `pr` |
| `curr` | `cr` |
| `convolve` | `cnv` |
| `numtheory` | `nt` |
| `combo` | `cb` |
| `stats` | `st` |
| `geo` | `g` |
| `fin` | `f` |
| `signal` | `sig` |
| `calc` | `cl` |
| `eqn` | `eq` |
| `eval` | `ev` |
| `history` | `hi` |
| `prob` | `pb` |
| `logic` | `lg` |
| `info` | `it` |
| `numerical` | `nm` |
| `chemistry` | `ch` |
| `datetime` | `dt` |
| `sel` | `sh` |

**Example**: `bcalc b add 5 10` instead of `bcalc basic add 5 10`

---

## Full Operation Reference

### Basic Arithmetic
`add`, `sub`, `mul`, `div`, `mod`

### Advanced Math
**Trigonometric**: `sin`, `cos`, `tan`, `arcsin`, `arccos`, `arctan`  
**Hyperbolic**: `sinh`, `cosh`, `tanh`, `arcsinh`, `arccosh`, `arctanh`  
**Logarithms**: `log`, `log10`, `log2`  
**Powers**: `exp`, `pow`, `nth`, `sqrt`  
**Rounding**: `floor`, `ceil`, `round`, `trunc`, `abs`, `sign`  
**Statistics**: `mean`, `median`, `std`, `var`, `min`, `max`, `sum`, `prod`  
**Other**: `fact`

### Probability & Distributions
`normal_pdf`, `normal_cdf`, `normal_ppf`, `binomial_pmf`, `binomial_cdf`, `poisson_pmf`, `poisson_cdf`, `exponential_pdf`, `t_test_1samp`, `t_test_ind`, `sample_normal`, `sample_binomial`

### Digital Logic
`base_convert`, `truth_table`, `simplify_boolean`, `bitwise_and`, `bitwise_or`, `bitwise_xor`, `bitwise_not`

### Information Theory
`shannon_entropy`, `kl_divergence`, `hamming_distance`, `levenshtein_distance`, `cross_entropy`, `mutual_information`

### Numerical Analysis
`polynomial_fit`, `lagrange_interpolation`, `cubic_spline_interpolation`, `rk4_solve`, `newton_interpolation`

### Chemistry
`molar_mass`, `ideal_gas_law`, `molarity`, `ph_from_h`, `h_from_ph`, `dilution`, `molality`, `mole_fraction`, `limiting_reagent`, `percent_yield`, `boiling_point_elevation`, `freezing_point_depression`, `osmotic_pressure`, `henderson_hasselbalch`, `half_life`, `radioactive_decay`, `density`, `ppm_to_concentration`, `molarity_to_ppm`

### Date & Time
`add_days`, `add_months`, `diff_days`, `day_of_week`, `age`, `julian_day`, `is_leap_year`, `week_number`

### Number Theory
`is_prime`, `prime_factors`, `gcd`, `lcm`, `fibonacci`, `nth_prime`, `euler_totient`, `catalan`, `binomial`, `mod_inverse`, `prime_sieve`, `digit_sum`, `reverse_number`, `is_palindrome`, `collatz_steps`, `perfect_number_check`, `goldbach_partitions`

### Combinatorics
`permutation`, `combination`, `multiset_combination`, `derangement`, `stirling_second_kind`, `bell_number`, `partition_count`, `stars_and_bars`, `catalan_number`, `lah_number`

### Extended Statistics
`mode`, `percentile`, `correlation`, `covariance`, `skewness`, `kurtosis`, `geometric_mean`, `harmonic_mean`, `z_score`, `chi_square`, `iqr`, `range_val`, `coefficient_of_variation`, `weighted_mean`, `moving_average`, `confidence_interval`

### Geometry
`circle_area`, `circle_circumference`, `sphere_volume`, `sphere_surface_area`, `rectangle_area`, `rectangle_perimeter`, `triangle_area`, `triangle_area_sss`, `cylinder_volume`, `cylinder_surface_area`, `cone_volume`, `cone_surface_area`, `pyramid_volume`, `torus_volume`, `torus_surface_area`, `ellipse_area`, `ellipse_perimeter`, `distance_2d`, `distance_3d`, `midpoint_2d`, `arc_length`, `sector_area`

### Financial Math
`compound_interest`, `simple_interest`, `emi`, `present_value`, `future_value`, `depreciation_straight_line`, `npv`, `roi`, `payback_period`, `inflation_adjusted_return`, `doubling_time`, `annuity_payment`

### Signal Processing
`fft`, `ifft`, `moving_average`, `power_spectrum`, `autocorrelation`, `cross_correlation`, `hamming_window`, `hanning_window`, `blackman_window`, `spectrogram_data`

### Calculus
`taylor_series`, `numerical_diff`, `numerical_integrate`, `series_sum`, `limit`, `partial_diff`, `double_integrate`, `maclaurin_series`, `gradient`, `jacobian`

### Equation Solver
`quadratic`, `cubic`, `polynomial_roots`, `linear_system_2d`, `simultaneous_2d`, `linear_system_3d`, `bisection`, `newton_raphson`, `secant_method`

### Expression Evaluator
`evaluate`

### History
`list`, `recall`, `search`, `export`, `clear`, `stats`

### Matrix Operations
`mul`, `det`, `inv`, `eig`, `transpose`, `rank`, `lu`, `qr`, `cholesky`, `svd`, `solve`, `least_squares`, `null_space`, `condition_number`, `exp`, `sylvester`, `generalized_eigen`, `power`, `det_via_lu`, `inv_via_lu`, `log`, `sqrt`, `polar`, `solve_triangular`

### Complex Numbers
`add`, `sub`, `mul`, `div`, `mag`, `phase`, `polar`, `rect`

### Symbolic Math
`simplify`, `diff`, `integrate`, `solve`, `expand`, `factor`

### Vector Operations
`dot_product`, `cross_product`, `magnitude`, `normalize`, `angle_between`

### Physics
`force`, `kinetic_energy`, `potential_energy`, `ohms_law`, `work`, `speed`, `acceleration`

---

## Contributing

Feel free to submit a Pull Request!

---

## Advanced Matrix Solvers

The CLI supports 24 advanced matrix solvers:

**LU Decomposition**
```bash
bcalc matrix lu "[[4,3],[6,3]]"
```

**QR Decomposition**
```bash
bcalc matrix qr "[[1,2],[3,4]]"
```

**Cholesky Decomposition**
```bash
bcalc matrix cholesky "[[4, 12], [12, 37]]"
```

**Singular Value Decomposition (SVD)**
```bash
bcalc matrix svd "[[1, 0], [0, 1]]"
```

**Solve Linear Systems**
```bash
bcalc matrix solve "[[3, 1], [1, 2]]" --b "[9, 8]"
```

**Matrix Exponential**
```bash
bcalc matrix exp "[[0, 1], [-1, 0]]"
```

**Generalized Eigenvalues**
```bash
bcalc matrix generalized_eigen "[[1, 2], [3, 4]]" --b "[[5, 6], [7, 8]]"
```

**Polar Decomposition**
```bash
bcalc matrix polar "[[1, 2], [3, 4]]"
```
