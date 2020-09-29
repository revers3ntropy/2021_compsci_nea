import program_listing.full.renderer as renderer
import program_listing.full.global_data as global_data
import program_listing.full.curser as curser
import program_listing.full.calc_profit_info as calculate_profit_info
import program_listing.full.calc_profit_enter as calculate_profit_enter
import program_listing.full.calc_profit_data as calculate_profit_data
import program_listing.full.enter_airport_details as airport_details
import program_listing.full.enter_flight_details as flight_details
import program_listing.full.get_info as get_info
import program_listing.full.main_menu as main_menu
import program_listing.full.save as save
import program_listing.full.load as load
import pygame as py

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : tick.py
#
#                                       Created : July 25, 2020
#
#                                   Last Update : July 28, 2020
#
# ------------------------------------------------------------------------------------------------
#
#             This file contains the function tick, which is run every tick of the program.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
#	renderer
#	global_data
#	calculate_profit
#	enter_airport_details
#	enter_flight_details
#	get_info
#	main_menu
#	pygame
#
# ------------------------------------------------------------------------------------------------
#
#	tick - gets run once every tick
#
# ================================================================================================


# ================================================================================================
#  tick -- run this every loop to step forwards one tick graphically and logically
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 25/07/2020
# ================================================================================================
def tick():

    global_data.session_tick += 1

    curser.update_mouse_clicked()

    # renderer.curser()

    state = global_data.session_state

    ###########################

    if state == global_data.main_menu:
        global_data.session_state = main_menu.run()

    elif state == global_data.enter_airport_details:
        global_data.session_state = airport_details.run()

    elif state == global_data.enter_flight_details:
        global_data.session_state = flight_details.run()

    elif state == global_data.get_info:
        global_data.session_state = get_info.run()

    elif state == global_data.calc_pofit_info:
        global_data.session_state = calculate_profit_info.run()

    elif state == global_data.calc_profit_data:
        global_data.session_state = calculate_profit_data.run()

    elif state == global_data.calc_profit_enter:
        global_data.session_state = calculate_profit_enter.run()

    elif state == global_data.save:
        global_data.session_state = save.run()

    elif state == global_data.load:
        global_data.session_state = load.run()
        
    else:
        print("Error report: state is " + str(state))

    ##########################

    py.display.set_caption('Joseph Coppin NEA 2020-2021')
    py.display.flip()
    renderer.clock.tick(renderer.run_FPS)

    renderer.screen.fill(renderer.background_colour)

    if global_data.typing_sticky_keys > 0:
        global_data.typing_sticky_keys -= 1