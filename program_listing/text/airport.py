# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : airport.py
#
#                                       Created : July 06, 2020
#
#                                   Last Update : July 06, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                                   Contains the class 'Airport'.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:

#
# ------------------------------------------------------------------------------------------------
#
# class 'Airport' functions:
#	__init__
#
# ================================================================================================

class Airport:
    # ================================================================================================
    #  __init__ -- initialises the object Airport
    #
    #  INPUT:  self
    #		   data - a tuple which contains the following information:
    #			   code     - the airport's code, a three letter code
    #			   name     - the airport's name
    #		       dist_LJL - the distance from Liverpool John Lennon British airport
    #		       dist_BI  - the distance from Bournemouth International British airport
    #
    #  RETURNS:  none
    #
    #  CREATED: 06/07/2020
    # ================================================================================================
    def __init__(self, data):
        self.code = data[0]
        self.name = data[1]
        self.dist_LJL = data[2]
        self.dist_BI = data[3]
