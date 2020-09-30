import program_listing.full.global_data as global_data

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : clear_data.py
#
#                                       Created : July 28, 2020
#
#                                   Last Update : September 30, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                                       Clears all inputted data.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
#  global_data
#
# ------------------------------------------------------------------------------------------------
#
#	clear - clears all inputted data
#
# ================================================================================================


# ================================================================================================
#  clear -- Clears all inputted data
#
#      Resets all data which can be inputted by the user to hard-coded 'reset' values.
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 28/07/2020
# ================================================================================================
def clear():
	global_data.uk_airport = ''
	global_data.overseas_airport = ''
	global_data.airplane_type = -1
	global_data.first_seats = 0
	global_data.first_price = 0
	global_data.standard_price = 0
