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
#  none
#
# ------------------------------------------------------------------------------------------------
#
# class 'Airport' functions:
#	__init__
#	get_code     - return the airport's three letter code
#	get_name     - returns the airport's name
#	get_dist_LJL - returns the distance between this airport and LJL
#	get_dist_BI  - returns the distance between this airport and BI
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
    #
    #  CREATED: 06/07/2020
    # ================================================================================================
	def __init__(self, data):
		self.code = data[0]
		self.name = data[1]
		self.dist_LJL = data[2]
		self.dist_BI = data[3]

	# ================================================================================================
    #  get_code -- returns the airport's code
    #
    #  INPUT:  self
    #
    #  RETURNS:  code - string - three letter ID code for airport
    #
    #  CREATED: 06/07/2020
    # ================================================================================================
	def get_code(self):
		return self.code

	# ================================================================================================
    #  get_name -- returns the airport's name
    #
    #  INPUT:  self
    #
    #  RETURNS:  name - string - name of the airport
    #
    #  CREATED: 06/07/2020
    # ================================================================================================
	def get_name(self):
		return self.name

	# ================================================================================================
    #  get_dist_LJL -- returns dist_LJL
    #
    #  INPUT:  self
    #
    #  RETURNS:  dist_LJL - int - distance between this airport and LJL
    #
    #  CREATED: 06/07/2020
    # ================================================================================================
	def get_dist_LJL(self):
		return self.dist_LJL

	# ================================================================================================
    #  get_dist_BI -- returns dist_BI
    #
    #  INPUT:  self
    #
    #  RETURNS:  dist_LJL - int - distance between this airport and BI
    #
    #  CREATED: 06/07/2020
    # ================================================================================================
	def get_dist_BI(self):
		return self.dist_BI