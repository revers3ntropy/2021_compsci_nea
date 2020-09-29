import program_listing.text.global_data as global_data

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : menu.py
#
#                                       Created : July 06, 2020
#
#                                   Last Update : July 25, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                        Contains the logic and display for the menu system.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
#	global_data
#
# ------------------------------------------------------------------------------------------------
#
#	clear_data			  - clears the data inputted by the user and allows them to re-input it
#	enter_airport_details - controls the 'enter airport details' menu option
#	enter_flight_details  - controls the 'enter flight details' menu option
#	calculate_profit	  - controls the 'calculate flight profit' menu option
#
# ================================================================================================

# ================================================================================================
#  clear_data -- resets the inputted data and allows the user to re-input it.
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 09/07/2020
# ================================================================================================
def clear_data():
	global_data.uk_airport = ''
	global_data.overseas_airport = None
	global_data.airplane_type = 0
	global_data.first_seats = 0
	global_data.first_price = 0
	global_data.standard_price = 0


# ================================================================================================
#  enter_airport_details -- controls the 'get airport details' menu option
#
#      Outputs the full name of the flight when the overseas airport code is given.
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 06/07/2020
# ================================================================================================
def enter_airport_details():

	# for entering the UK airport code

	valid_response = False
	while not valid_response:
		print('UK airport code (either LPL or BOH): ')
		uk_airport = input()

		if uk_airport in ('LPL', 'BOH'):  # if the code is valid
			valid_response = True
			global_data.uk_airport = uk_airport

		if not valid_response:
				print('Sorry, that is not a valid code, or the airport you are looking for does not exist.')
	else:

		# for entering the overseas airport code

		valid_response = False
		while not valid_response:
			print('Overseas airport code: ')
			overseas_airport = input()

			for i in global_data.list_of_airports:  # loops through all the possible airport codes,
												# and checks to see if the code matches
				if i.get_code() == overseas_airport:
					valid_response = True
					global_data.overseas_airport = i

					print('The name of the overseas airport is ' + str(i.get_name()) + '.')
				
			if not valid_response:
				print('Sorry, that is not a valid code, or the airport you are looking for does not exist.')


# ================================================================================================
#  enter_flight_details -- controls the 'enter flight details' menu option
#
#      
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 06/07/2020
# ================================================================================================
def enter_flight_details():
	valid_response = False
	while not valid_response:
		print()
		print('Type of aircraft to be used:')
		print()
		repsonse = input()
		if repsonse in ('medium narrow', 'large narrow', 'medium wide'):
			valid_response = True
			print()
			print('    -	Aircraft details:	-	')
			
			if repsonse == 'medium narrow':
				global_data.airplane_type = global_data.medium_narrow
			elif repsonse == 'large narrow':
				global_data.airplane_type = global_data.large_narrow
			elif repsonse == 'medium_wide':
				global_data.airplane_type = global_data.medium_wide

			aircraft_data = global_data.airplane_types_data[global_data.airplane_type]

			print('The running cost per km is ' + str(aircraft_data[global_data.running_cost]))
			print('The maximum range in km is ' + str(aircraft_data[global_data.max_range]))
			print('The maximum capasity is ' + str(aircraft_data[global_data.max_capasity]))
			print('The minimum first class seats is ' + str(aircraft_data[global_data.min_first_class]))

			valid_response = False
			while not valid_response:
				print()
				print('How many first class seats?')
				print()
				first_class_seats = int(input())
				if first_class_seats > 0:
					if first_class_seats < aircraft_data[global_data.min_first_class]:
						print('That is smaller than the minumum number of first class seats for that aircraft.')
					elif first_class_seats > aircraft_data[global_data.max_capasity] / 2:
						print('That is larger than the maximum number of first class seats for that aircraft.')
					else:
						global_data.first_seats = first_class_seats
						valid_response = True
						max_standard_seats = aircraft_data[global_data.max_capasity]
						number_of_standard_seats = max_standard_seats - first_class_seats / 2
						print('the number of standard class seats is ' + str(int(number_of_standard_seats)))
		else:
			print('Not a a valid type of aircraft, sorry')

# ================================================================================================
#  calculate_profit -- controls the 'calculate profit' menu option
#
#      
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 09/07/2020
# ================================================================================================
def calculate_cost():
	if global_data.uk_airport == '' or global_data.overseas_airport == None:
		print('Sorry, please enter flight details first')
	elif global_data.airplane_type == -1:
		print('Sorry, please enter airplane type first')
	elif global_data.first_seats == 0:
		print('Sorry, please enter the number of first class seats first')
	else:
		airplane_max = global_data.airplane_types_data[global_data.airplane_type][global_data.max_range]
		airport_dist = 0
		if global_data.uk_airport == 'LJL':
			airport_dist = global_data.overseas_airport.get_dist_LJL()
		else:
			airport_dist = global_data.overseas_airport.get_dist_BI()

		if airplane_max < int(airport_dist):
			print('Sorry, but the range of the selected airport is too short for the flight plan')

		else:
			found = False
			while not found:
				print('\n Please enter the price of a first class seat \n')
				price = input()
				try:
					price = float(price)
				except:
					pass
				if price < 0 or type(price) != float:
					print('error, please try again')
				else:
					found = True

			found = False
			while not found:
				print('\n Please enter the price of a standard class seat \n')
				price = input()
				try:
					price = float(price)
				except:
					pass
				if price < 0 or type(price) != float:
					print('error, please try again')
				else:
					found = True
			
			standard_seats = global_data.airplane_types_data[global_data.airplane_type][global_data.max_capasity] - global_data.first_seats * 2
			cost_per_seat = global_data.airplane_types_data[global_data.airplane_type][global_data.running_cost] * airport_dist / 100
			cost = cost_per_seat * (global_data.first_seats + standard_seats)
			income = global_data.first_seats * global_data.first_price + standard_seats * global_data.standard_price
			profit = income - cost

			print('The flight costs ' + str(cost_per_seat) + ' per seat.')
			print('The flight costs ' + str(cost) + ' in total.')
			print('The flight has a total income of ' + str(income) + '.')
			print("The flight's profit is " + str(profit) + '.')
		