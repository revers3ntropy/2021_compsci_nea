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
#                                   Last Update : October 21, 2020
#
# ------------------------------------------------------------------------------------------------
#
#             This file contains the function tick, which is run every tick of the program.
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
import program_listing.full.renderer as renderer
import program_listing.full.global_data as g
import program_listing.full.cursor as cursor
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
#
# ------------------------------------------------------------------------------------------------
#
#	tick
#
# ================================================================================================

# The state machine holds two things: the ID for that state, and the file which contains the run
# function for the state.
state_machine = {
    g.main_menu: main_menu,
    g.enter_airport_details: airport_details,
    g.enter_flight_details: flight_details,
    g.get_info: get_info,
    g.calc_profit_info: calculate_profit_info,
    g.calc_profit_data: calculate_profit_data,
    g.calc_profit_enter: calculate_profit_enter,
    g.save: save,
    g.load: load
}


# ================================================================================================
#  tick -- run this every loop to step forwards one tick graphically and logically. Updates pygame
#          by refreshing the screen, and then filling it with the background colour.
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 25/07/2020
# ================================================================================================
def tick():
    g.session_tick += 1

    # updates the mouse click history, which means that you have to click on the button for it to
    # register as a click, rather than, for example, holding down on the mouse.
    cursor.update_mouse_clicked()

    # runs the current state function, which will sort out the graphics and logical side for each menu option
    g.session_state = state_machine[g.session_state].run()

    # pygame tick
    py.display.flip()
    renderer.clock.tick(renderer.run_FPS)
    renderer.screen.fill(renderer.background_colour)

    # updates the global sticky keys mod for typing smoothly
    if g.typing_sticky_keys > 0:
        g.typing_sticky_keys -= 1
