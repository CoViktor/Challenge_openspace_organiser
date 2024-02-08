#Must-have features: MVP (Minimum Viable Product)
# You want to build a program that allows you to get a list of colleagues from an excel file and place them randomly on the different tables of the open space.

# Note: The default setup of the open space is 6 tables of 4 seats → 24 seats.
# The program can take a filepath as an argument to load the list of colleagues.
# The program distributes randomly the people on the existing tables and says how much seats are left.
# The program can deal with the possibility of having to much people in the room.

#Define a table with how many seats it encompasses and we define the object in the table.py file


# # --- This file should contain:
# Import everything you need to launch the organizer
# Load the colleagues from the excel file defined in the config file
# Launch the organizer. Display the results.

from utils.table import Table, Seat

test = Table()
test.who_sits_here()
test.assign_seat('Me')
test.who_sits_here()
print('done')
