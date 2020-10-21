import program_listing.full.global_data as global_data
import pickle

# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : preset_controller.py
#
#                                       Created : September 28, 2020
#
#                                   Last Update : October 10, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                             Controls presets, and the file management.
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================


class Preset:
    def __init__(self):
        self.name = ''
        self.uk_airport = ''
        self.overseas_airport = ''
        self.airplane_type = 0
        self.first_seats = 0
        self.first_price = 0
        self.standard_price = 0


presets = {}
for i in range(global_data.max_presets):
    presets[i] = None

with open('presets_data.txt', 'rb') as pickle_file:
    presets = pickle.load(pickle_file)


# ================================================================================================
#  save_current_as_preset -- gets the current entered data, and saves it to a new preset.
#
#  INPUT:  name: str - the name of the new preset
#
#  RETURNS:  none
#
#  CREATED: 28/07/2020
# ================================================================================================
def save_current_as_preset(name: str):
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
        if type(presets[j]) is not Preset:
            found_empty = True
            presets[j] = new_preset
            break

    # check if there is an empty slot for the preset
    if not found_empty:
        print('no more preset slots')
    else:
        print('saving')
        with open('presets_data.txt', 'wb') as pickle_file:
            print('opened')
            pickle.dump(presets, pickle_file)
            print('dumped')


# ================================================================================================
#   load_in_preset -- loads a preset from the id of the preset.
#
#   INPUT:  id_: int - the id of the preset to be loaded in
#
#   RETURNS:  none
#
#   CREATED: 28/07/2020
# ================================================================================================
def load_in_preset(id_: int):
    preset = presets[id_]

    global_data.uk_airport = preset.uk_airport
    global_data.overseas_airport = preset.overseas_airport
    global_data.airplane_type = preset.airplane_type
    global_data.first_seats = preset.first_seats
    global_data.first_price = preset.first_price
    global_data.standard_price = preset.standard_price
