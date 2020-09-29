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
#                                   Last Update : August 24, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                                   Contains the class 'Airport'.
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
	#		   data - a tuple which contains the following inforamtion:
	#			   code     - the airport's code, a three letter code
	#			   name     - the airports's name
	#		       dist_LJL - the distance from Liverpool John Lennon British airport
	#		       dist_BI  - the distance from Bourrnemouth International British airport
    #
    #  RETURNS:  none
    # ================================================================================================
	def __init__(self, data):
		self.code = data[0].lower()
		self.name = data[1].lower()
		self.dist_LJL = int(data[2])
		self.dist_BI = int(data[3])
