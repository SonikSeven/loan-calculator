# Loan Calculator

This GitHub project contains a `Loan Calculator` program written in Python. It can calculate different aspects of a loan such as the monthly payment, the principal amount, and the time to repay the loan, based on user input. It supports both annuity and differentiated payments.

## Description

The Loan Calculator uses command-line arguments to receive input data. It has functionalities to compute various loan parameters:

- Annuity payments: Monthly payment amounts in case of an annuity loan.
- Differentiated payments: Month-by-month payment breakdown for differentiated payment loans.
- Principal loan amount: Original loan balance before interest.
- Loan repayment time: Total time to repay the loan.

The calculator uses the following parameters for calculations:

- `--type`: The type of payment: "annuity" or "diff" (differentiated).
- `--payment`: The monthly payment amount.
- `--principal`: The loan's principal amount.
- `--periods`: The number of months needed to repay the loan.
- `--interest`: The annual interest rate (without the percent sign).

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/loan-calculator.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## Usage Example

Here's an example of how to calculate differentiated payments on a loan with a principal of 500,000 over 8 months with an interest rate of 7.8%:

```
python main.py --type=diff --principal=500000 --periods=8 --interest=7.8
```

## Error Handling

The calculator will print "Incorrect parameters" if:

- The `--type` parameter is neither "annuity" nor "diff".
- The interest rate is not provided.
- Less than three parameters are provided.
- There's an attempt to calculate differentiated payments but the monthly payment is also specified.
  
## License

This project is licensed under the [MIT License](LICENSE.txt).

## Note

This calculator is for educational purposes and should not be used for financial advice. It's a practical tool for understanding how loan parameters affect repayment terms.
