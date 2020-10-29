import time
import pygame as py

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
#                                     File Name : calc_profit_data.py
#
#                                       Created : July 31, 2020
#
#                                   Last Update : September 30, 2020
#
# ------------------------------------------------------------------------------------------------
#
#              Enter the required info for the menu option 'calculate profit'.
#
# ------------------------------------------------------------------------------------------------
#
#	run - runs this menu option
#
# ================================================================================================
"""
                                         Joseph Coppin
                                  Computer Science GSCE Coursework

Description of file

Global Functions:

Imports:                                                                                         """


def price_checker(price):
    try:
        price = int(price)
        if 10000 > price > 0:
            return True
    except:
        pass

    return False


first_price_box = buttons.TextBoxWithCheck(renderer.mid_x, renderer.mid_y, typing.retro_8x10, '', 4, price_checker)
standard_price_box = buttons.TextBoxWithCheck(renderer.mid_x, renderer.mid_y + 100, typing.retro_8x10, '', 4, price_checker)

next_button = buttons.StandardButton(renderer.mid_x, renderer.mid_y + 200, typing.retro_8x10, 'next')


def find_overseas_airport():
    for i in global_data.list_of_airports:
        if i.code == global_data.overseas_airport:
            return i


def run_normal_menu():
    first_price_box.run()
    standard_price_box.run()

    typing.write(typing.retro_8x10, 'Price of a first class ticket:', (renderer.mid_x, renderer.mid_y - 50))
    typing.write(typing.retro_8x10, 'Price of a standard class ticket:', (renderer.mid_x, renderer.mid_y + 50))

    if next_button.run():
        global_data.first_price = first_price_box.run()
        global_data.standard_price = standard_price_box.run()
        return True

    return False


# ================================================================================================
#  run -- runs and controls the menu option
#
#  INPUT:  none
#
#  RETURNS:  what menu is should go to next
#
#  CREATED: 28/07/2020
# ================================================================================================
def run():
    if global_data.airplane_type == -1 or global_data.uk_airport == '' or global_data.overseas_airport == '' or global_data.first_seats == 0:
        return global_data.calc_profit_enter

    elif global_data.first_price != 0 and global_data.standard_price != 0:
        return global_data.calc_profit_info

    else:
        airplane_max = global_data.airplane_types_data[global_data.airplane_type][global_data.max_range]

        if global_data.uk_airport == 'lpl':
            airport_dist = find_overseas_airport().dist_LJL
        else:
            airport_dist = find_overseas_airport().dist_BI

        if airplane_max < int(airport_dist):
            typing.write(typing.retro_8x10, 'The range of the selected', (renderer.mid_x, renderer.mid_y - 50))
            typing.write(typing.retro_8x10, 'airplane is too short for', (renderer.mid_x, renderer.mid_y))
            typing.write(typing.retro_8x10, 'the flight plan', (renderer.mid_x, renderer.mid_y + 50))
            py.display.flip()
            time.sleep(5)
            return global_data.main_menu

        else:
            if run_normal_menu():
                return global_data.calc_profit_info

    return global_data.calc_profit_data
