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
# ================================================================================================

back_button = buttons.StandardButton(renderer.mid_x, renderer.mid_y - 100,
                                     typing.retro_8x10, 'back')
save_button = buttons.StandardButton(renderer.mid_x, renderer.mid_y,
                                     typing.retro_8x10,
                                     'save current as preset')


def preset_name_check(message):
    if len(message) > 0:
        for i in range(global_data.max_presets):
            if preset_controller.presets[i] != 0:
                if message == preset_controller.presets[i].name:
                    return False
        return True
    return False


preset_name_box = buttons.TextBoxWithCheck(renderer.mid_x, renderer.mid_y + 50,
                                           typing.retro_8x10, 'preset name',
                                           15, preset_name_check)


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
    if back_button.run():
        return global_data.main_menu

    preset_name_box.run()

    if save_button.run():
        if preset_name_box.correct:
            preset_controller.save_current_as_preset(preset_name_box.message)
            return global_data.main_menu

    return global_data.save
