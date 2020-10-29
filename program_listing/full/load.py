"""
                                         Joseph Coppin
                                  Computer Science GSCE Coursework

Controls the menu option to load a preset

Global Functions:
    refresh_buttons
    run

Imports:                                                                                         """
import program_listing.full.global_data as global_data
import program_listing.full.renderer as renderer
import program_listing.full.buttons as buttons
import program_listing.full.typing as typing
import program_listing.full.preset_controller as preset_controller


play_buttons = {}
delete_buttons = {}
back_button = buttons.StandardButton(110, 30,
                                     typing.retro_8x10, 'back')

no_preset_message = 'no preset'


# ================================================================================================
#  refresh_buttons -- runs and controls the menu option
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 28/07/2020
# ================================================================================================
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
                preset_controller.save_data()

    return global_data.load
