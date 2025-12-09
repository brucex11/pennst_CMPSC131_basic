#----------------------------------------------------------
# Name: Sophia Bandini
# E-mail Address: sophia.bandini@gmail.com
# Class: CMPSC 131 Section
# Project #: 9
# Due Date: 12 Dec 25
# Brief Project Description: 
# Write a class named Car that has the following private data attributes: 
# * year_model (for the car’s year model)
# * make (for the make of the car)
# * speed (for the car’s current speed)
# The car class should have an__init__ method that accepts the car’s year model and make as arguments. These values
# should be assigned to the object’s year_model and make data attributes. The  __init__ method should also assign 0
# to the speed data attribute.
# The class should also have the following methods:
# * accelerate: The accelerate method should add 5 to the speed data attribute each time it is called.
# * brake: The brake method should subtract 5 from the speed data attribute each time it is called.
# * get_make: The get_make method should return the value of the make data attribute.
# * get_year: The get_year method should return the value of the year_model data attribute.
# * get_speed: The get_speed method should return the current speed.
# * __str__ : The __str__ method should return a string indicating the state of the object. For example,
#    the function should return Current speed: 5, assuming that the value of the speed data attribute is 5.
# 
# 
# Next, write a program that creates a Car object then calls get_make and get_year methods and displays the car’s year,
# model, and make. The program should then call the accelerate method five times. After each call to the accelerate
# method, display the current speed of the car.  Then call the brake method five times. After each call to the brake
# method, display the current speed of the car.
#----------------------------------------------------------


# import os
# import sys

class Car():
	"""
	"""

	# attributes using property decorator
# 	@property
# 	def year(self):
# 		return self._year
# 	@property
# 	def make(self):
# 		return self._make
# 	@property
# 	def model(self):
# 		return self._model
# 	def __str__( self ):
# 		"""Utilize the property decorator as getter method.

# 		Returns:
# 				str: object's year, make, and model
# 		"""
# 		return f"Car info:\n\
# Make: {self.make} {self.model}\n\
# Year: {self.year}"


	# Getter methods per assignment description.
	def get_year( self ):
		return self._year
	def get_make( self ):
		return self._make
	def get_model( self ):
		return self._model
	def get_speed( self ):
		return self.speed

	def __str__( self ):
		return f"Car info:\n\
Make: {self.get_make()} {self.get_model()}\n\
Year: {self.get_year()}"


	# ---- class methods ---------------------------------------------------------
	def accelerate( self ):
		"""add 5 to the speed data attribute each time it is called.
		"""
		self.speed += 5
		print( f"Current speed: {self.get_speed()}" )

	def brake( self ):
		"""subtract 5 to the speed data attribute each time it is called.
		"""
		self.speed -= 5
		print( f"Current speed: {self.get_speed()}" )



	def __init__( self, year, make, model ):
		"""_summary_

		Args:
				year (int): year of manufacture
				make (str): car's make
				model (str): car's model
		"""
		self._year = year
		self._make = make
		self._model = model

		self.speed:int = 0


def main() -> int:
	"""
	Entry point for script.

	Runtime with output:
	> python HW9.py
	Car info:
	Make: Honda Accord
	Year: 2010
	car is accelerating:
	Current speed: 5
	Current speed: 10
	Current speed: 15
	Current speed: 20
	Current speed: 25

	car is braking:
	Current speed: 20
	Current speed: 15
	Current speed: 10
	Current speed: 5
	Current speed: 0

	:rtype: int
	:returns: The resulting value from executing the desired command.
	"""

	car = Car( 2010, 'Honda', 'Accord' )
	print( car )

	print( 'car is accelerating:' )
	for i in range(0,5):
		car.accelerate()

	print( '\ncar is braking:' )
	for i in range(0,5):
		car.brake()

	return 0

# This is useful when the "file" is to be run directly by python (and not imported)
if __name__ == "__main__":
	# print( 'Call ', __name__ )
	main()
else:
	print( "Do not run from import" )
