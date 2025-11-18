#----------------------------------------------------------
# Name: Sophia Bandini
# E-mail Address: sophia.bandini@gmail.com
# Class: CMPSC 131 Section
# Project #: 6
# Due Date: 31 Oct 25
# Brief Project Description: Design a single Python program that demonstrates
# recursion by performing four mathematical operations using recursive functions:
# 1. Calculating a factorial of a non-negative integer
# 2. Summing integer numbers from 1 to n
# 3. Raising a number to a power (assume the exponent is a nonnegative integer)
# 4. Calculating the sum of the digits of a positive integer
# Each operation must be implemented as a recursive function.
#----------------------------------------------------------


# import os
# import sys


def main() -> int:
	"""
	Entry point for script.

	:rtype: int
	:returns: The resulting value from executing the desired command.
	"""

	# Greet the customer and ask for their name.
	greeting:str = f"""Recursive Math Toolkit\n----------------------
	1. Factorial
	2. Sum of numbers
	3. Power (exponent)
	4. Sum of digits
	5. Exit
	Enter your choice (1-5): 
	"""

	recursion_choices = ('1','2','3','4')

	while(True):
		rsp:str = input( greeting )
		if rsp == '5':
			break
		if rsp not in recursion_choices:
			print( 'Invalid choice, try again' )
			continue

		if rsp == '3':
			ibase:int = int(input( 'Enter base: ' ))
			iexp:int = int(input( 'Enter exponent: ' ))
			rslt = calc_power( ibase, iexp )
			print( f"{ibase} to the power of {iexp} is {rslt}." )

		if rsp == '4':
			idigits:int = int(input( 'Enter a positive integer: ' ))
			rslt = calc_sum_of_digits( idigits )
			print( f"Sum of digits is {rslt}." )

	return 0



def calc_power( ibase:int, iexp:int ) -> int:
	"""
	Args:
		ibase: base for power calculation (positive integer)
		iexp: exponent for power calculation (positive integer)

	Return: ibase^iexp
	"""
	# Anything to the power of 0 is 1
	if iexp == 0:
		return 1
	# Recursion: decrement the exponent each time through; when the exponent
	# reaches 0, the recursion is complete.
	return ibase * calc_power(ibase, iexp - 1)


def calc_sum_of_digits( idigits:int ) -> int:
	"""
	Args:
		idigits: a positive integer

	Return: sum of each individual digits for the input integer (parameter)
	"""
	# Base case: when n is 0, sum of digits is 0
	if idigits == 0:
		return 0
	# Recursive case: add the last digit to the sum of the rest
	return (idigits % 10) + calc_sum_of_digits( idigits // 10 )

# This is useful when the "file" is to be run directly by python (and not imported)
if __name__ == "__main__":
	# print( 'Call ', __name__ )
	main()
else:
	print( "Do not run from import" )
