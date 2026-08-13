"""
Date & Time operations for Brliant Calculator.

Operations:
- add_days:     add (or subtract) days to/from a date
- add_months:   add (or subtract) months to/from a date
- diff_days:    days between two dates
- day_of_week:  weekday name of a date
- age:          age in years from a birth date
- julian_day:   Julian Day Number of a date
- is_leap_year: whether a year is a leap year
- week_number:  ISO week number of a date

All dates are accepted as YYYY-MM-DD (also YYYY/MM/DD, DD-MM-YYYY, etc.)
or the keyword "today".
"""

from datetime import date, datetime, timedelta


_DATE_FORMATS = (
    "%Y-%m-%d",
    "%Y/%m/%d",
    "%d-%m-%Y",
    "%d/%m/%Y",
    "%m/%d/%Y",
    "%Y%m%d",
)


def _parse_date(value):
    """Parse a user-provided date string into a date object."""
    if isinstance(value, date):
        return value
    s = str(value).strip()
    if s.lower() in ("today", "now"):
        return date.today()
    for fmt in _DATE_FORMATS:
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    raise ValueError(
        f"Invalid date '{value}'. Expected YYYY-MM-DD (or 'today')."
    )


def _to_int(value, name):
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        raise ValueError(f"'{value}' is not a valid integer for {name}.")


def add_days(date_str, days):
    """Return the date `days` days after (or before) `date_str`."""
    d = _parse_date(date_str)
    n = _to_int(days, "days")
    return d + timedelta(days=n)


def add_months(date_str, months):
    """Return the date `months` months after (or before) `date_str`.

    If the target month has fewer days than the source day, the result is
    clamped to the last day of the target month (e.g. Jan 31 + 1 month).
    """
    d = _parse_date(date_str)
    n = _to_int(months, "months")
    month_index = d.year * 12 + (d.month - 1) + n
    year, month_zero = divmod(month_index, 12)
    month = month_zero + 1
    last_day = _days_in_month(year, month)
    return date(year, month, min(d.day, last_day))


def _days_in_month(year, month):
    if month == 12:
        return (date(year + 1, 1, 1) - date(year, 12, 1)).days
    return (date(year, month + 1, 1) - date(year, month, 1)).days


def diff_days(date1, date2):
    """Return the number of days between date1 and date2 (date2 - date1)."""
    d1 = _parse_date(date1)
    d2 = _parse_date(date2)
    return (d2 - d1).days


def day_of_week(date_str):
    """Return the weekday name (e.g. 'Monday') of a date."""
    return _parse_date(date_str).strftime("%A")


def age(birth_date):
    """Return the age in whole years given a birth date."""
    birth = _parse_date(birth_date)
    today = date.today()
    years = today.year - birth.year
    if (today.month, today.day) < (birth.month, birth.day):
        years -= 1
    return years


def julian_day(date_str):
    """Return the Julian Day Number (JDN) of a date."""
    d = _parse_date(date_str)
    a = (14 - d.month) // 12
    y = d.year + 4800 - a
    m = d.month + 12 * a - 3
    return (
        d.day
        + (153 * m + 2) // 5
        + 365 * y
        + y // 4
        - y // 100
        + y // 400
        - 32045
    )


def is_leap_year(year):
    """Return True if `year` is a leap year."""
    y = _to_int(year, "year")
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


def week_number(date_str):
    """Return the ISO week number (1-53) of a date."""
    return _parse_date(date_str).isocalendar()[1]
