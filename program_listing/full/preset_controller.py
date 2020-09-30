import program_listing.full.global_data as global_data
import pickle

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : file_name.py
#
#                                       Created : month 00, 2020
#
#                                   Last Update : month 00, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
# global_function_1 - what this function does
#
# class 'preset' functions:
#	__init__
#	function_1 - whatever this function does
#
# ================================================================================================
presets = {}


def save_current_as_preset(name):
    new_preset = Preset()

    new_preset.name = name
    new_preset.uk_airport = global_data.uk_airport
    new_preset.overseas_airport = global_data.overseas_airport
    new_preset.airplane_type = global_data.airplane_type
    new_preset.first_seats = global_data.first_seats
    new_preset.first_price = global_data.first_price
    new_preset.standard_price = global_data.standard_price

    found_empty = False
    for j in range(len(presets)):
        if presets[j] is None:
            found_empty = True
            presets[j] = new_preset
            break

    with open('presets_data.txt', 'wb') as pickle_file:
        pickle.dump(presets, pickle_file)

    if not found_empty:
        print('no more preset slots')


def load_presets():
    with open('presets_data.txt', 'rb') as pickle_file:
        return pickle.load(pickle_file)


def load_in_preset(id_):
    preset = presets[id_]

    global_data.uk_airport = preset.uk_airport
    global_data.overseas_airport = preset.overseas_airport
    global_data.airplane_type = preset.airplane_type
    global_data.first_seats = preset.first_seats
    global_data.first_price = preset.first_price
    global_data.standard_price = preset.standard_price


try:
    presets = load_presets()
except Exception:
    print('Welcome new user!')
    presets = {}
    for i in range(
            global_data.max_presets):  # sets a empty dict of presets ready to be made
        presets[i] = 0


class Preset:
    def __init__(self):
        self.name = ''
        self.uk_airport = ''
        self.overseas_airport = ''
        self.airplane_type = 0
        self.first_seats = 0
        self.first_price = 0
        self.standard_price = 0
