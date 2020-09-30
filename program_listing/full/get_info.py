import program_listing.full.global_data as global_data
import program_listing.full.renderer as renderer
import program_listing.full.buttons as buttons
import program_listing.full.typing as typing

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : get_info.py
#
#                                       Created : July 30, 2020
#
#                                   Last Update : September 30, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                Controls the menu option 'get info', found in 'calculate profits'.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
# 	global_data
#	renderer
#	buttons
#	typing
#
# ------------------------------------------------------------------------------------------------
#
#	run - runs this menu option
#
# ================================================================================================

back_button = buttons.StandardButton(renderer.mid_x, renderer.mid_y + 250, typing.retro_8x10,
                                     'back')


# ================================================================================================
#  run -- runs and controls the menu option
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 28/07/2020
# ================================================================================================
def run():
    info = global_data.airplane_types_data[global_data.airplane_type]

    message = 'running cost: ' + str(info[global_data.running_cost])
    typing.write(typing.retro_8x10, message, (renderer.mid_x, renderer.mid_y - 100))
    message = 'maximum range: ' + str(info[global_data.max_range])
    typing.write(typing.retro_8x10, message, (renderer.mid_x, renderer.mid_y - 50))
    message = 'maximum capacity: ' + str(info[global_data.max_capacity])
    typing.write(typing.retro_8x10, message, (renderer.mid_x, renderer.mid_y))
    message = 'minimum first class seats: ' + str(info[global_data.min_first_class])
    typing.write(typing.retro_8x10, message, (renderer.mid_x, renderer.mid_y + 50))

    if back_button.run():
        return global_data.enter_flight_details

    return global_data.get_info
