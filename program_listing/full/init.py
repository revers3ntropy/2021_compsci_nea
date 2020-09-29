import program_listing.full.airport as airport
import program_listing.full.global_data as global_data
import program_listing.full.preset_controller as preset_controller

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : init.py
#
#                                       Created : July 25, 2020
#
#                                   Last Update : July 25, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                  Contains the function init, which is called to initialise the program.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
#	airports
#	global_data
#	renderer	- below
#
# ------------------------------------------------------------------------------------------------
#
#	init_airports - initialises airport objects
#	init 	      - initiliases the program
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
#  CREATED: 25/07/2020
# ================================================================================================
def init_airports(airport_data):
	for line in airport_data:
		data = tuple(line.split(","))
		global_data.list_of_airports.append(airport.Airport(data)) # initialses an airport from the data file

# ================================================================================================
#  init -- initialises the program
#
#      Called once when the program gets run, sets up the program for running.async
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 25/07/2020
# ================================================================================================
def init():

    with open('Airports.txt', 'r') as airport_data: # gets the file
        init_airports(airport_data)
