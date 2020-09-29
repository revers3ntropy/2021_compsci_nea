import program_listing.full.buttons as buttons
import program_listing.full.global_data as global_data
import program_listing.full.typing as typing
import program_listing.full.renderer as renderer

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : calc_profit_enter.py
#
#                                       Created : July 31, 2020
#
#                                   Last Update : July 31, 2020
#
# ------------------------------------------------------------------------------------------------
#
#   Controls the screren for if data still needs to be entered when calc profit buton is pressed.
#
# ------------------------------------------------------------------------------------------------
#
#	run - runs the main menu
#
# ================================================================================================
center_x = renderer.mid_x
center_y = renderer.mid_y

main_menu_button = buttons.StandardButton(center_x, center_y - 100, typing.retro_8x10, 'main menu')
enter_airport_details = buttons.StandardButton(center_x, center_y + 150, typing.retro_8x10, 'enter airport details')
enter_flight_details = buttons.StandardButton(center_x, center_y + 200, typing.retro_8x10, 'enter flight details')


# ================================================================================================
#  run -- runs and controls the menu option
#
#  INPUT:  none
#
#  RETURNS:  int - dependant on what options have been selected
#
#  CREATED: 28/07/2020
# ================================================================================================
def run():

	typing.write(typing.retro_8x10, 'Some data still needs to be entered:', (center_x, center_y))

	if main_menu_button.run():
		return global_data.main_menu

	if global_data.overseas_airport == '' or global_data.uk_airport == '':
		if enter_airport_details.run():
			return global_data.enter_airport_details

	if global_data.first_seats == 0 or global_data.airplane_type == -1:
		if enter_flight_details.run():
			return global_data.enter_flight_details

	return global_data.calc_profit_enter