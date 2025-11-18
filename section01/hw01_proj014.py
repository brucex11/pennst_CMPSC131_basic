"""
Name: Sophia Bandini
E-mail Address: sophia.bandini@gmail.com
Class: CMPSC 131 Section
Project #: 14
Due Date: 9/12/25
Brief Project Description:
Write a Python program for programing project # 14 (Compound Interest) on page 116.
The output should be rounded to two decimal places of precision.
Assume the user will enter valid data.
This program calculates the ending principal in a bank account after compounding the interest.


Sample Run:
-----------------------------------------------
Enter the starting principal: 10000
Enter the annual interest rate: 2
How many times per year is the interest compounded? 12
For how many years will the account earn interest? 15
-----------------------------------------------

Actual Run:

(.venvPy3-12-0) C:\SourceCode\GitHub\pennst\CMPSC131_basic\section01>python hw01_proj014.py -h
ENTRYPOINT: Module: 'C:\SourceCode\GitHub\pennst\CMPSC131_basic\section01\hw01_proj014.py'; function: 'main'
usage: hw01_proj014.py options
        Sample run:
        (.venvPy3-12-0) > hw01_proj014.py  --initial-principal 10000  --interest-rate 2  --compounding 12  --years 15

       [-h] [-p INITIAL_PRINCIPAL] [-i INTEREST_RATE] [-c COMPOUNDING] [-y YEARS]

options:
  -h, --help            show this help message and exit
  -p INITIAL_PRINCIPAL, --initial-principal INITIAL_PRINCIPAL
                        Initial account balance
  -i INTEREST_RATE, --interest-rate INTEREST_RATE
                        Annual interest rate
  -c COMPOUNDING, --compounding COMPOUNDING
                        Times per year is the interest compounded
  -y YEARS, --years YEARS
                        Total years that account earns interest

(.venvPy3-12-0) C:\SourceCode\GitHub\pennst\CMPSC131_basic\section01>python hw01_proj014.py -p 10000 -i 2 -c 12 -y 15
ENTRYPOINT: Module: 'C:\SourceCode\GitHub\pennst\CMPSC131_basic\section01\hw01_proj014.py'; function: 'main'
principal: $10000.0
annual_rate: 0.02%
compounding: 12.0 times per year
total years: 15.0
At the end of 15 years, you will have $13495.22.

"""

from inspect import currentframe

import argparse
# import errno
import os
import sys


def main() -> int:
	"""
	Entry point for script.

	:rtype: int
	:returns: The resulting value from executing the desired command.
	"""

	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__file__}'; function: '{fcn_name}'" )

	parse_the_args()
	new_bal:float = calc_new_balance(
		principal=args.initial_principal,
		rate=args.interest_rate,
		compounding=args.compounding,
		years=args.years
	)

	print( f"At the end of {args.years} years, you will have ${new_bal}." )

	return 0


def calc_new_balance( principal:str, rate:str, compounding:str, years:str ) -> float:
	"""
	Based on the principal, interest-rate, compounding, calculate the account new
	balance after X years.

	Convert the parameters to float-type prior to calculation.

	Parameters
	----------
	principal : string
		Initial account balance.
	rate : string
		Annual interest rate.
	compounding : string
		Times per year is the interest compounded.
	years : string
		Total years that account earns interest.

	Returns
	-------
	float
		New account balance rounded to two decimal places of precision.

	"""

	# print( f"args cmd line: {args}" )

	# Convert parameter strings to float-type.
	prin:float = float(principal)
	annual_rate:float = float(rate) / 100.0
	times_per_year:float = float(compounding)
	yrs:float = float(years)
	print( f"principal: ${prin}" )
	print( f"annual_rate: {annual_rate}%" )
	print( f"compounding: {times_per_year} times per year" )
	print( f"total years: {yrs}" )

	new_balance:float = prin * ( 1 + (annual_rate / times_per_year) ) ** (times_per_year * yrs)
	new_balance = round(new_balance,2)
	return new_balance



def parse_the_args() -> None:
	"""
	Handle all switches on the command line.
	"""
	# Get the basename for current module (file).
	fname:str = os.path.basename(__file__)

	desc=f"""{fname} options
	Sample run:
	(.venvPy3-12-0) > {fname}  --initial-principal 10000  --interest-rate 2  --compounding 12  --years 15
	"""

	parser = argparse.ArgumentParser( prog=desc )
	# The REST
	parser.add_argument( "-p", "--initial-principal", help="Initial account balance" )
	parser.add_argument( "-i", "--interest-rate", help="Annual interest rate" )
	parser.add_argument( "-c", "--compounding", help="Times per year is the interest compounded" )
	parser.add_argument( "-y", "--years", help="Total years that account earns interest" )

	# No switches, not even -h
	if len( sys.argv ) == 1:
		parser.print_help( sys.stderr )
		sys.exit(1)
	global args
	args = parser.parse_args()
	# print( f"args cmd line: {args}" )


# This is useful when the "file" is to be run directly by python (and not imported)
if __name__ == "__main__":
	# print( 'Call ', __name__ )
	main()
else:
	print( "Do not run from import" )
