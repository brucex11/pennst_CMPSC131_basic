#----------------------------------------------------------
# Name: Sophia Bandini
# E-mail Address: sophia.bandini@gmail.com
# Class: CMPSC 131 Section
# Project #: 8
# Due Date: 21 Nov 25
# Brief Project Description: write a program that helps a teacher analyze
#  student grades using two-dimensional lists.
# The program will store:
# *	A one-dimensional list for student names
# *	A two-dimensional list for test scores
# Each row in the 2-D list represents a student’s scores on several tests.
# Program will calculate and display individual averages, test averages,
#  and identify top-performing students.

# Author's NOTE:
# By design, this codeset is not implemented in the most effecient manner;
# each requirement is implemented in its own function.

#----------------------------------------------------------


# import os
# import sys


def main() -> int:
	"""
	Entry point for script.

	:rtype: int
	:returns: The resulting value from executing the desired command.
	"""

	# 1. Create a 1D list containing the names of 5 students
	students = ["Alison", "Barry", "Carlos", "Danny", "Ersa"]

	# 2. Create a 2-D list to store each student’s test scores
	scores = [
			[88, 92, 79, 93],
			[76, 85, 83, 89],
			[90, 91, 92, 95],
			[69, 74, 81, 70],
			[84, 86, 88, 90]]


	display_table_of_scores_with_average( students=students, scores=scores )
	print()
	calculate_and_display_average_score_for_each_test( scores=scores )
	print()
	calculate_and_display_top_student( students=students, scores=scores )
	print()
	calculate_and_display_class_average( scores=scores )
	print()
	display_their_test_scores_and_average( students=students, scores=scores )

	return 0



def calculate_and_display_average_score_for_each_test( scores ):
	"""
	Test 1 average: 81.40
	Test 2 average: 85.60
	...

	Args:
		scores: 2-D List of student test scores

	"""
	# use the length of the first row of scores to set the range of
	# indexes for each row of scores
	for idx in range(len(scores[0])):

		# Collect the values in the column
		column_values = [row[idx] for row in scores]

		average = sum(column_values) / len(column_values)
		print( f"Test {idx+1} average: {average}" )


def calculate_and_display_class_average( scores ):
	"""
	Calculate the average of all students's averages.

	Print "Class average score = {avg}."
	...

	Args:
		scores: 2-D List of student test scores

	"""
	list_of_average_scores = []
	# avg_score = 0

	# calc the averages for each student and save them in their own list
	for row in scores:
		avg_score = sum( row ) / len( row )
		list_of_average_scores.append( avg_score )

	# get the average of the average-scores
	avg_of_avgs = sum( list_of_average_scores ) / len( list_of_average_scores )
	print( f"Class average score = {avg_of_avgs}." )


def calculate_and_display_top_student( students, scores ):
	"""
	Determine the student with the highest average test-score.
	Load the average scores into a List/array, find the array-index to the
	highest score, and use that index to get the student's name.

	Print "Carlos has highest average of 92.0."
	...

	Args:
		students: List of their names
		scores: 2-D List of student test scores

	"""
	list_of_average_scores = []
	avg_score = 0

	for idx, name in enumerate( students ):
		for score in scores[idx]:
			# calc the average and save it
			avg_score = sum(scores[idx]) / len(scores[idx])
		list_of_average_scores.append( avg_score )

	# get the highest score from the list of scores and its index
	high_score = max(list_of_average_scores)
	high_score_idx = list_of_average_scores.index(high_score)
	print( f"{students[high_score_idx]} has highest average of {high_score}." )


def display_table_of_scores_with_average( students, scores ):
	"""
	Student        Test1  Test2  Test3  Test4  Average
	----------------------------------------------------
	Alice          88     92     79     93     88.00
	...

	Args:
		students: List of their names
		scores: 2-D List of student test scores

	"""
	print( f"Student\t\tTest1\tTest2\tTest3\tTest4\tAverage" )
	print( '----------------------------------------------------' )
	for idx, name in enumerate( students ):
		print( f"{name}\t\t", end="" )
		for score in scores[idx]:
			print( f"{score}\t", end="" )
		# calc the average and display it
		average = sum(scores[idx]) / len(scores[idx])
		print( f"{average}" )
		# print()


def display_their_test_scores_and_average( students, scores ):
	"""
	Prompt the user for which student's test scores and average to display.
	Based on the input, display only that student.

	Student        Test1  Test2  Test3  Test4  Average
	----------------------------------------------------
	Alice          88     92     79     93     88.00

	Args:
		students: List of their names
		scores: 2-D List of student test scores

	"""

	select_student:str = 'Select a student to view their record:'
	print( select_student )
	for idx, name in enumerate( students ):
		print( f"{idx}. {name}" )

	rsp:int = int( input( 'Select student by number: ' ) )

	# check response is between 0 and 4 inclusive for valid index into arrays.
	if 0 <= rsp <= 4:
		pass
	else:
		print( 'Invalid student.' )
		return

	print( f"Student\t\tTest1\tTest2\tTest3\tTest4\tAverage" )
	print( '----------------------------------------------------' )
	print( f"{students[rsp]}\t\t", end="" )
	for score in scores[rsp]:
		print( f"{score}\t", end="" )
	# calc the average and display it
	average = sum(scores[rsp]) / len(scores[rsp])
	print( f"{average}" )



# This is useful when the "file" is to be run directly by python (and not imported)
if __name__ == "__main__":
	# print( 'Call ', __name__ )
	main()
else:
	print( "Do not run from import" )
