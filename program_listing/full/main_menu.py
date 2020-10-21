# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : main_menu.py
#
#                                       Created : July 28, 2020
#
#                                   Last Update : October 21, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                                    Controls the main menu.
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
import program_listing.full.buttons as buttons
import program_listing.full.global_data as global_data
import program_listing.full.typing as typing
import program_listing.full.clear_data as clear_data
import program_listing.full.renderer as renderer
#
# ------------------------------------------------------------------------------------------------
#
#	run
#	tick_stats
#
# ================================================================================================
center_x = renderer.mid_x
center_y = renderer.mid_y

quit_button = buttons.StandardButton(120, 30, typing.retro_8x10, 'quit')
clear_data_button = buttons.StandardButton(renderer.screen_x - 120, 30, typing.retro_8x10, 'clear')

save_to_preset = buttons.StandardButton(center_x - 100, center_y - 150, typing.retro_8x10, 'save')
load_preset = buttons.StandardButton(center_x + 100, center_y - 150, typing.retro_8x10, 'load')

calculate_profits_button = buttons.StandardButton(center_x, center_y - 100, typing.retro_8x10, 'calculate profits')

enter_airport_details = buttons.StandardButton(center_x, center_y + 150, typing.retro_8x10, 'enter airport details')

enter_flight_details = buttons.StandardButton(center_x, center_y + 200, typing.retro_8x10, 'enter flight details')


# ================================================================================================
#  tick_stats -- displays the current stats entered by the user onto the screen_x. Goes through
#                each global stat and check if something has been entered or not, and displays a
#                message accordingly.
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 28/07/2020
# ================================================================================================
def tick_stats():
    # UK airport
    if global_data.uk_airport != '':
        message = f'UK airport: {global_data.uk_airport}'
    else:
        message = 'Uk airport: N/A'
    typing.write(typing.retro_8x10, message, (renderer.mid_x, renderer.mid_y - 50))

    # Overseas airport
    if global_data.overseas_airport != '':
        message = f'Overseas airport: {global_data.overseas_airport}'
    else:
        message = 'Overseas airport: N/A'
    typing.write(typing.retro_8x10, message, (renderer.mid_x, renderer.mid_y - 20))

    # Airplane type
    if global_data.airplane_type != -1:
        message = f'Airplane type: {global_data.airplane_type}'
    else:
        message = 'Airplane type: N/A'
    typing.write(typing.retro_8x10, message, (renderer.mid_x, renderer.mid_y + 10))

    # Number of first class seats
    message = f'Number of First class seats: {global_data.first_seats}'
    typing.write(typing.retro_8x10, message, (renderer.mid_x, renderer.mid_y + 40))

    # First class seat price
    message = f'Price of first class seats: {global_data.first_price}'
    typing.write(typing.retro_8x10, message, (renderer.mid_x, renderer.mid_y + 70))

    # Standard class seat price
    message = f'standard class seat price: {global_data.standard_price}'
    typing.write(typing.retro_8x10, message, (renderer.mid_x, renderer.mid_y + 100))


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
    if quit_button.run():
        global_data.go = False

    if calculate_profits_button.run():
        return global_data.calc_profit_data

    if clear_data_button.run():
        clear_data.clear()

    if enter_airport_details.run():
        return global_data.enter_airport_details

    if enter_flight_details.run():
        return global_data.enter_flight_details

    if save_to_preset.run():
        return global_data.save

    if load_preset.run():
        return global_data.load

    tick_stats()

    return global_data.main_menu
