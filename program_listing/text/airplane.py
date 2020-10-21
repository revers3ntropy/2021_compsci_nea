# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : airplane.py
#
#                                       Created : July 06, 2020
#
#                                   Last Update : July 06, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                                  Contains the class 'Airplane'.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
import program_listing.text.global_data as global_data


#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================

class Airplane:
    # ================================================================================================
    #  __init__ -- initialises the object Airport
    #
    #  INPUT: airplane_type - which type of airplane it is
    #
    #  RETURNS:  none
    #
    #  CREATED: 06/07/2020
    # ================================================================================================
    def __init__(self, airplane_type):
        type_data = global_data.airplane_types_data[airplane_type]

        self.running_cost = type_data[global_data.running_cost]
        self.max_range = type_data[global_data.max_range]
        self.max_capacity = type_data[global_data.max_capacity]
        self.min_first_class = type_data[global_data.min_first_class]
