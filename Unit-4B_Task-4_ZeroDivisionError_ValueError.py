try:
    num = float(input("Enter numerator: "))  # int or float
    den = float(input("Enter denominator: "))
    print("Quotient:", num / den)
except ZeroDivisionError:
    print("Denominator cannot be zero.")
except ValueError:
    print("Please enter valid numbers.")
    