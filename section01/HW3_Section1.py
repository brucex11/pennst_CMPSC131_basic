#----------------------------------------------------------
# Name: Sophia Bandini
# E-mail Address: sophia.bandini@gmail.com
# Class: CMPSC 131 Section
# Project #: 3
# Due Date: 26 Sep 25
# Brief Project Description: Use Python selection structures (if, elif, else,
#  and nested conditionals) to build a menu-based ordering program that
#  simulates a coffee shop.
#----------------------------------------------------------

"""
.. py:currentmodule:: py_main.py

Runs a shell command.
"""
# import errno
import os
import sys


def main() -> int:
	"""
	Entry point for script.

	:rtype: int
	:returns: The resulting value from executing the desired command.
	"""

	# Greet the customer and ask for their name.
	greeting:str = 'Welcome to Python Cafe!\nWhat is your name? '

	rsp:str = input( greeting )

	cafe_response:str = f"Hello {rsp}! What would you like to order?"
	print( cafe_response )

	# Display a drink menu with at least three options (e.g., coffee, tea, smoothie).
	drink_menu_options = ( 'coffee', 'tea', 'smoothie' )
	for idx, drink in enumerate(drink_menu_options):
		print( f"{idx+1}. {drink}" )

	#	Let the customer select their drink.
	drink_choices = ('1','2','3')
	rsp = input( 'Enter 1, 2, or 3  ')
	if rsp not in drink_choices:
		print( 'Invalid choice. No drink for you!\nYour total is: $0.00' )
		return 0

	#	Ask the following questions based on their choice.
	order_summary: str = ''
	if rsp == '1':
		order_summary = for_coffee()
	elif rsp == '2':
		order_summary = for_tea()
	else:
		order_summary = for_smoothie()


	print( order_summary )
	return 0


def for_coffee() -> str:
	"""
	Ask if they want milk (yes/no).
	Assign a price based on the drink customization.
	"""
	order_summary: str = 'You ordered'
	rsp = input( 'Do you want milk (yes/no)?' )
	if rsp == 'yes':
		order_summary = f"{order_summary} Coffee with milk.\nYour total is: $3.50"
	elif rsp == 'no':
		order_summary = f"{order_summary} Black coffee.\nYour total is: $3.00"
	else:
		order_summary = 'Invalid coffee flavor selection. No drink for you!\nYour total is: $0.00'
	return order_summary


def for_smoothie() -> str:
	"""
	Assign a price based on the drink customization.
	small = $3.00, medium = $4.00, large = $5.00.
	"""
	order_summary: str = 'Invalid size. No drink for you!\nYour total is: $0.00'
	dict_sizes = { 'small': '$3.00', 'medium': '$4.00', 'large': '$5.00' }

	rsp = input( 'Choose size (small/medium/large): ' )

	# Check input is a key in the dictionary
	if rsp in dict_sizes:
		# Since the entry is valid, replace the order_summary
		order_summary = f"You ordered a {rsp} Smoothie.\nYour total is: {dict_sizes[rsp]}"

	return order_summary


def for_tea() -> str:
	"""
	Tea = $2.50
	"""
	return 'You ordered tea.\nYour total is: $2.50'


# This is useful when the "file" is to be run directly by python (and not imported)
if __name__ == "__main__":
	# print( 'Call ', __name__ )
	main()
else:
	print( "Do not run from import" )
