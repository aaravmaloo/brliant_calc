import math


def compound_interest(principal, rate, time, n=12):
    if n <= 0:
        return "Error: Compounding frequency must be positive."
    return principal * (1 + rate / (100 * n)) ** (n * time)

def simple_interest(principal, rate, time):
    return principal * (1 + rate / 100 * time)

def emi(principal, rate, months):
    if months <= 0:
        return "Error: Number of months must be positive."
    monthly_rate = rate / (12 * 100)
    if monthly_rate == 0:
        return principal / months
    emi_val = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
    return emi_val

def present_value(future_val, rate, time):
    return future_val / (1 + rate / 100) ** time

def future_value(principal, rate, time):
    return principal * (1 + rate / 100) ** time

def depreciation_straight_line(cost, salvage, life):
    if life <= 0:
        return "Error: Asset life must be positive."
    return (cost - salvage) / life

def npv(rate, cashflows):
    total = 0
    for i, cf in enumerate(cashflows):
        total += cf / (1 + rate / 100) ** i
    return total

def roi(cost, gain):
    if cost == 0:
        return "Error: Investment cost cannot be zero."
    return (gain - cost) / cost * 100

def payback_period(cashflows):
    cumulative = 0
    for i, cf in enumerate(cashflows):
        cumulative += cf
        if cumulative >= 0:
            if i == 0:
                return 0
            prev = cumulative - cf
            return i - 1 + abs(prev) / cf
    return "Error: Investment does not pay back within given period."

def inflation_adjusted_return(nominal_return, inflation_rate):
    return ((1 + nominal_return / 100) / (1 + inflation_rate / 100) - 1) * 100

def doubling_time(rate):
    if rate <= 0:
        return "Error: Rate must be positive."
    return math.log(2) / math.log(1 + rate / 100)

def annuity_payment(principal, rate, periods):
    if periods <= 0:
        return "Error: Periods must be positive."
    monthly_rate = rate / 100
    if monthly_rate == 0:
        return principal / periods
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -periods)
