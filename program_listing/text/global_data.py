# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : globals.py
#
#                                       Created : July 02, 2020
#
#                                   Last Update : July 25, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                                       Contains all global variables and constants.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:

#
# ------------------------------------------------------------------------------------------------
#
#	none
#
# ================================================================================================

go = True  # should the program run or not?

list_of_airports = []

# inputted data:
uk_airport = ''
overseas_airport = ''
airplane_type = -1
first_seats = 0
first_price = 0
standard_price = 0

# setting the types of airplanes as ints for use in the data dict:
medium_narrow = 0	
large_narrow = 1
medium_wide = 2

# variables for each type of airplane
running_cost = 0
max_range = 1
max_capacity = 2
min_first_class = 3

# fixed data for each type of airplane
airplane_types_data = {  
	medium_narrow: {
		running_cost: 8,
		max_range: 2650,
		max_capacity: 180,
		min_first_class: 8
	},
	large_narrow: {
		running_cost: 7,
		max_range: 5600,
		max_capacity: 220,
		min_first_class: 10
	},
	medium_wide: {
		running_cost: 5,
		max_range: 4050,
		max_capacity: 406,
		min_first_class: 14
	}
}