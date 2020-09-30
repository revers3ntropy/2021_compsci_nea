import program_listing.full.global_data as global_data
import program_listing.full.buttons as buttons
import program_listing.full.typing as typing
import program_listing.full.renderer as renderer

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : file_name.py
#
#                                       Created : September 28, 2020
#
#                                   Last Update : September 30, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
# 	global_data
#	buttons
#	typing
#	renderer
#
# ------------------------------------------------------------------------------------------------
#
#	overseas_airport_checker - function passed into text-box to check if the message is viable
#	uk_airport_checker - function passed into text-box to check if the message is viable
#	run - runs this menu option
#
# ================================================================================================

mid_x = renderer.mid_x
mid_y = renderer.mid_y


def uk_airport_checker(message):
    message = message.lower()
    if message in ('lpl', 'boh'):
        return True
    return False


def overseas_airport_checker(message):
    message = str.lower(message)
    found = False
    for airport in global_data.list_of_airports:
        if str.lower(airport.code) == message:
            found = True

    if found:
        return True
    return False


overseas_airport_box = buttons.TextBoxWithCheck(mid_x, mid_y + 50, typing.retro_8x10, 'DEF', 3,
                                                overseas_airport_checker)

uk_airport_box = buttons.TextBoxWithCheck(mid_x, mid_y - 50, typing.retro_8x10, 'ABC', 3,
                                          uk_airport_checker)

save_button = buttons.StandardButton(mid_x, mid_y + 100, typing.retro_8x10, 'save and exit')


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
    typing.write(typing.retro_8x10, 'UK airport:', (renderer.mid_x, renderer.mid_y - 100))
    typing.write(typing.retro_8x10, 'Overseas airport:', (renderer.mid_x, renderer.mid_y))
    if save_button.run():
        if uk_airport_box.correct and overseas_airport_box.correct:
            global_data.uk_airport = uk_airport_box.run()
            global_data.overseas_airport = overseas_airport_box.run()
            return global_data.main_menu

    uk_airport_box.run()
    overseas_airport_box.run()

    return global_data.enter_airport_details
