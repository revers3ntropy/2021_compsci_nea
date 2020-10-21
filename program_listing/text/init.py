# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : init.py
#
#                                       Created : July 06, 2020
#
#                                   Last Update : July 06, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                  Contains the function init, which is called to initialise the program.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
import program_listing.text.airport as airport
import program_listing.text.global_data as global_data
#
# ------------------------------------------------------------------------------------------------
#
#	init_airports
#	init
#
# ================================================================================================

# ================================================================================================
#  init_airports -- initialises all airport objects
#
#      Called once when the program gets run, adds to the global list of Airport objects.
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 06/07/2020
# ================================================================================================
def init_airports(airport_data):
	for line in airport_data:
		data = tuple(line.split(","))
		global_data.list_of_airports.append(airport.Airport(data))
		# creates an airport from the data file, and adds it to the global list

# ================================================================================================
#  init -- initialises the program
#
#      Called once when the program gets run, sets up the program for running.
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 06/07/2020
# ================================================================================================
def init():
	with open('Airports.txt', 'r') as airport_data: # gets the file
		init_airports(airport_data)
