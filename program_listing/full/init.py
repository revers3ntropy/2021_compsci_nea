"""
                                         Joseph Coppin
                                  Computer Science GSCE Coursework

Contains the function init, which is called to initialise the program.

Global Functions:
    init_airports
    init

Imports:                                                                                         """
import program_listing.full.airport as airport
import program_listing.full.global_data as g


# ================================================================================================
#  init_airports -- initialises all airport objects. Called once when the program gets run, adds to
#                   the global list of Airport objects.
#
#  INPUT:  airport_data - the data to be loaded in
#
#  RETURNS:  none
#
#  CREATED: 25/07/2020
# ================================================================================================
def init_airports(airport_data):
    for line in airport_data:
        data = tuple(line.split(","))
        g.list_of_airports.append(
            airport.Airport(data))  # initialises an airport from the data file


# ================================================================================================
#  init -- initialises the program. Called once when the program gets run, sets up the program for
#  running.
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 25/07/2020
# ================================================================================================
def init():
    with open('Airports.txt', 'r') as airport_data:  # gets the file
        init_airports(airport_data)
