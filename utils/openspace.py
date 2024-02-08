#In openspace.py create a class Openspace that contains these attributes:

# tables which is a list of Table. (you will need to import Table from table.py).
# number_of_tables which is an integer.
# And some methods:

# organize(names) that will:
# randomly assign people to Seat objects in the different Table objects.
# display() display the different tables and there occupants in a nice and readable way
# store(filename) store the repartition in an excel file

from table import Table, Seat

class Openspace():
    def __init__(self, table_count= 4):
        '''tables = amount of tables'''
        self.tables = []
        for x in range(table_count):
            table = Table()
            self.tables.append(table)

room1 = Openspace(3)
for x in room1.tables:
    x.who_sits_here()