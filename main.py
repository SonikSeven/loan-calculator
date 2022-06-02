import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()


def calculate():

    t = args.type
    m = int(args.payment) if args.payment is not None else -1
    p = int(args.principal) if args.principal is not None else -1
    n = int(args.periods) if args.periods is not None else -1
    i = float(args.interest) / 100 / 12 if args.interest is not None else -1

    initial = [x for x in [m, p, n, i] if x >= 0]
    if (t != "annuity" and t != "diff") or i == -1 or len(initial) < 3 or (t == "diff" and m >= 0):
        return print("Incorrect parameters")

    total = 0
    if t == "diff":
        for month in range(1, n + 1):
            d = p / n + i * (p - (p * (month - 1)) / n)
            total += math.ceil(d)
            print(f"Month {month}: payment is {math.ceil(d)}")
    elif n == -1:
        n = math.ceil(math.log(m / (m - i * p), i + 1))
        total = m * n
        n = math.floor(n // 12), n % 12
        s = "" if n[0] == 1 else "s", "" if n[1] == 1 else "s"
        a = "and" if n[0] != 0 and n[1] != 0 else ""
        years = f"{n[0]} year{s[0]} " if n[0] != 0 else ""
        months = f"and {n[1]} month{s[1]} " if n[1] != 0 else ""
        print("It will take " + years + a + months + "to repay this loan!")
    elif m == -1:
        m = math.ceil(p * (i * (1 + i) ** n) / ((1 + i) ** n - 1))
        total = m * n
        print(f"Your annuity payment = {m}!")
    elif p == -1:
        p = math.floor(m / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
        total = m * n
        print(f"Your loan principal = {p}!")
    print(f"Overpayment = {total - p}")


calculate()
