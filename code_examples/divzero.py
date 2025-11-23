try:
    1/0
except ZeroDivisionError as e:
    raise RuntimeError("Cannot divide by zero") from None
