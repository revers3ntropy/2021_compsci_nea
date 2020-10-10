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
#                                     File Name : calc_profit_info.py
#
#                                       Created : July 31, 2020
#
#                                   Last Update : September 30, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                  Displays the info for the menu option 'calculate profit'.
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
#	run - runs this menu option
#
# ================================================================================================

main_menu_button = buttons.StandardButton(
    renderer.mid_x, renderer.mid_y + 200, typing.retro_8x10, 'main menu'
)


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
    typing.write(typing.retro_8x10, 'Route stats:', (renderer.mid_x, renderer.mid_y - 175))

    if main_menu_button.run():
        return global_data.main_menu

    def find_overseas_airport(airport_code):
        for airport in global_data.list_of_airports:
            if airport.code == airport_code:
                return airport

    if global_data.uk_airport == 'LJL':
        airport_dist = find_overseas_airport(global_data.overseas_airport).dist_LJL
    else:
        airport_dist = find_overseas_airport(global_data.overseas_airport).dist_BI

    standard_seats = int(
        global_data.airplane_types_data[global_data.airplane_type][global_data.max_capacity]) - int(
        global_data.first_seats) * 2
    cost_per_seat = global_data.airplane_types_data[global_data.airplane_type][
                        global_data.running_cost] * airport_dist / 100
    cost = float(cost_per_seat) * (float(global_data.first_seats) + float(standard_seats))
    income = float(global_data.first_seats) * float(
        global_data.first_price) + standard_seats * float(global_data.standard_price)
    profit = income - cost

    typing.write(typing.retro_8x10, f'The flight costs {cost_per_seat} per seat', (renderer.mid_x, renderer.mid_y - 100))
    typing.write(typing.retro_8x10, f'The flight costs {cost} in total', (renderer.mid_x, renderer.mid_y - 50))
    typing.write(typing.retro_8x10, f'The total income of {income}', (renderer.mid_x, renderer.mid_y))
    typing.write(typing.retro_8x10, f'The profit is {profit}', (renderer.mid_x, renderer.mid_y + 50))

    return global_data.calc_profit_info
