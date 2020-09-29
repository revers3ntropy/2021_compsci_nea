import program_listing.full.global_data as global_data
import program_listing.full.renderer as renderer
import program_listing.full.buttons as buttons
import program_listing.full.typing as typing
import program_listing.full.preset_controller as preset_controller

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
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
# global_function_1 - what this function does
#
# class 'myFirstClass' functions:
#	__init__
#	function_1 - whatever this function does
#
# ================================================================================================
play_buttons = {}
delete_buttons = {}
back_button = buttons.StandardButton(110, 30,
                                     typing.retro_8x10, 'back')

no_preset_message = 'no preset'


def refresh_buttons():
    global play_buttons
    global delete_buttons

    for i in range(global_data.max_presets):

        delete_buttons[i] = 0
        if preset_controller.presets[i] != 0:

            play_buttons[i] = buttons.StandardButton(
                renderer.mid_x, renderer.mid_y + i * 50 - 200,
                typing.retro_8x10, preset_controller.presets[i].name)
            delete_buttons[i] = buttons.StandardButton(
                renderer.mid_x + 300, renderer.mid_y + i * 50 - 200,
                typing.retro_8x10, 'delete')

        else:

            play_buttons[i] = buttons.StandardButton(
                renderer.mid_x, renderer.mid_y + i * 50 - 200,
                typing.retro_8x10, no_preset_message)


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
    global delete_buttons
    global play_buttons

    refresh_buttons()
    if back_button.run():
        return global_data.main_menu

    for i in range(global_data.max_presets):

        if play_buttons[i].run() is not None:
            if play_buttons[i].message != no_preset_message:
                preset_controller.load_in_preset(i)
                return global_data.main_menu

        if delete_buttons[i] != 0:
            if delete_buttons[i].run() is not None:
                preset_controller.presets[i] = 0

    return global_data.load
