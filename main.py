<<<<<<< HEAD

import pygame as py

import program_listing.text.global_data as text_globals
import program_listing.text.init as text_init
import program_listing.text.tick as text_tick

import program_listing.full.global_data as full_globals
import program_listing.full.init as full_init
import program_listing.full.tick as full_tick

=======
import global_data
import init
import tick
>>>>>>> origin/master

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : main.py
#
#                                       Created : July 02, 2020
#
#                                   Last Update : August 26, 2020
#
# ------------------------------------------------------------------------------------------------
#
<<<<<<< HEAD
#	This file gets run to run the program. it first checks if you want to run the progrm normally 
#	or text-based, and hen runs it dependant on the answer. 
=======
>>>>>>> origin/master
#	This file gets run to run the program. I have decided that I will try to seperate any 
#	functions larger than 15 lines or 5 if statements as a general rule, and that this file will 
#	contain as little as possible as it cannot be moved into the program listing.
#
#	I have decided that I will try to seperate any functions larger than 15 lines or 5 if 
#	statements as a general rule, and that this file will contain as little as possible as it 
#	cannot be moved into the program listing.
#
# ------------------------------------------------------------------------------------------------
#
# Class 'Program' functions:
#	__init__
#	__init_program - calls the initiliase function in the init file
#	__main_loedop    - runs the main loop for the program
#	run_program    - runs the program from the begining
# ================================================================================================

class Program:
	def __init__(self):
		self.type = False

	# ================================================================================================
	#  __init_program -- initlises the selected program type
	#
	#  INPUT:  none
	#
	#  RETURNS:  none
	# ================================================================================================
	def __init_program(self):
		print('initilising program...')

		if self.type == 'text':
			text_init.init()

		elif self.type == 'full':
			full_init.init()

		else:
			print(f'Error: program type is {self.type}, which is not valid')
	
	# ================================================================================================
	#  __main_loop -- runs the main loop for the selected program
	#
	#  INPUT:  none
	#
	#  RETURNS:  none
	# ================================================================================================
	def __main_loop(self):
		print('initilisation finished successfully! \n Running program now...')

		if self.type == 'text':

			while text_globals.go:
				text_tick.tick()

		elif self.type == 'full':

			while full_globals.go:
				full_tick.tick()

		else:
			print(f'Error: program type is {self.type}, which is not valid')
		
	# ================================================================================================
	#  run_program -- controls selecting the program type, and then the whole Program
	#
	#		Waits untill a valid response for program type has been inputed, and then initlises and 
	#		runs the main loop of the program. This is called to run the program
	#
	#  INPUT:  none
	#
	#  RETURNS:  none
	# ================================================================================================
	def run_program(self):
		print("Welcome to Joseph Coppin's year 10 and 11 computer science non-examined assessment project!\nWould you like to run the full program, or just the text-based one?\n")

		while not self.type:

			print("Please enter 'full' for the full program, and 'text' for the text-based one\n")
			answer = input()
			if answer not in ('full', 'text'):
				print("\nSorry, that is not a valid response. Please enter either 'full' or 'text'.\n")
			else:
				
				self.type = answer

		self.__init_program()
		self.__main_loop()


Program().run_program()
py.quit()
