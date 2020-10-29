# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : unit_tests.py
#
#                                       Created : October 15, 2020
#
#                                   Last Update : October 21, 2020
#
# ------------------------------------------------------------------------------------------------
#
#	  Holds all the unit tests. I am using the built in python unit tester, which sorts out many
#	  nice things.
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
import unittest
import program_listing.full.global_data as global_data
from program_listing.full.clear_data import clear
#
# -------------------------------------------------------------------------------------------------
#
# ================================================================================================
"""
                                         Joseph Coppin
                                  Computer Science GSCE Coursework

Description of file

Global Functions:

Imports:                                                                                         """


class ClearData(unittest.TestCase):
    def test(self):
        global_data.uk_airport = 'test'
        global_data.overseas_airport = 'test'
        global_data.airplane_type = 100
        global_data.first_seats = 200
        global_data.first_price = -50
        global_data.standard_price = 9876

        clear()

        self.assertEqual([
            global_data.uk_airport,
            global_data.overseas_airport,
            global_data.airplane_type,
            global_data.first_seats,
            global_data.first_price,
            global_data.standard_price
        ], [
            '',
            '',
            -1,
            0,
            0,
            0
        ])


if __name__ == '__main__':
    unittest.main()
