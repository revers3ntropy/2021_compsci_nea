# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : tick.py
#
#                                       Created : July 06, 2020
#
#                                   Last Update : July 25, 2020
#
# ------------------------------------------------------------------------------------------------
#
#             This file contains the function tick, which is run every tick of the program.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
import program_listing.text.global_data as global_data
import program_listing.text.menu as menu
#
# ------------------------------------------------------------------------------------------------
#
#	tick - gets run once every tick
#
# ================================================================================================


# ================================================================================================
#  tick -- run this every loop to step forwards one tick graphically and logically
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 06/07/2020
# ================================================================================================
def tick():
	print('\n What would you like to do?')
	print("You can 'calculate flight profit', 'enter airport details', 'enter flight details', 'clear data' or 'quit' ")
	option = input()
	if option == 'quit':
		global_data.go = False
	elif option == 'calculate flight profit':
		menu.calculate_cost()
	elif option == 'enter airport details':
		menu.enter_airport_details()
	elif option == 'enter flight details':
		menu.enter_flight_details()
	elif option == 'clear data':
		menu.clear_data()