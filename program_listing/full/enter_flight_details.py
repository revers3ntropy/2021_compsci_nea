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
#                                     File Name : file_name.py
#
#                                       Created : month 00, 2020
#
#                                   Last Update : month 00, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                            Controls the enter flight details menu option.
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

# ================================================================================================
#  run -- runs and controls the menu option
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 28/07/2020
# ================================================================================================
mid_x = renderer.mid_x
mid_y = renderer.mid_y


def first_seats_checker(message):
    try:
        number = int(message)
        if number == 0:
            return True
        elif number > global_data.airplane_types_data[global_data.airplane_type][global_data.min_first_class]:
            if number < global_data.airplane_types_data[global_data.airplane_type][global_data.max_capacity] / 2:
                return True
    except:
        pass
        print('error at enter_flight_details.first_seat_checker')
    return False


first_seats_box = buttons.TextBoxWithCheck(mid_x, mid_y + 50, typing.retro_8x10, '000', 3,
                                           first_seats_checker)

medium_narrow_button = buttons.StandardButton(mid_x, mid_y - 150, typing.retro_8x10,
                                              'Medium narrow')
large_narrow_button = buttons.StandardButton(mid_x, mid_y - 100, typing.retro_8x10, 'Large narrow')
medium_wide_button = buttons.StandardButton(mid_x, mid_y - 50, typing.retro_8x10, 'Medium wide')

get_info_button = buttons.StandardButton(mid_x, mid_y - 250, typing.retro_8x10, 'get info')

save_button = buttons.StandardButton(mid_x, mid_y + 200, typing.retro_8x10, 'save and exit')


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
    if medium_narrow_button.run():
        global_data.airplane_type = global_data.medium_narrow
    if large_narrow_button.run():
        global_data.airplane_type = global_data.large_narrow
    if medium_wide_button.run():
        global_data.airplane_type = global_data.medium_wide

    typing.write(typing.retro_8x10, 'Number of first class seats:',
                 (renderer.mid_x, renderer.mid_y))
    if save_button.run():
        if first_seats_box.correct and global_data.airplane_type != -1:
            global_data.first_seats = first_seats_box.run()
            return global_data.main_menu

    first_seats_box.run()

    if global_data.airplane_type == -1:
        message = 'n/a'
    elif global_data.airplane_type == 0:
        message = 'medium narrow'
    elif global_data.airplane_type == 1:
        message = 'large narrow'
    elif global_data.airplane_type == 2:
        message = 'medium wide'
    else:
        message = f'Error: airplane type is {global_data.airplane_type}'

    typing.write(typing.retro_8x10, 'Airplane type: ' + message,
                 (renderer.mid_x, renderer.mid_y - 200))

    if global_data.airplane_type != -1:
        if get_info_button.run():
            return global_data.get_info

    return global_data.enter_flight_details
