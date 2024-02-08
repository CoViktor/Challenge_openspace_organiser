#In openspace.py create a class Openspace that contains these attributes:

# tables which is a list of Table. (you will need to import Table from table.py).

from table import Table, Seat
from file_utils import call_data
import random as r


class Openspace():
    def __init__(self, number_of_tables= 6):
        '''tablecount = amount of tables (default= 4)
        this amount will be assigned on initialisation of the object
        tables = list of all tables in the space'''
        self.tables = []
        self.number_of_tables = number_of_tables #-> is this needed?? make sure to refactor all if i don't do this
        for x in range(self.number_of_tables):
            table = Table()
            self.tables.append(table)

# And some methods:
# organize(names) that will:
    #def organize(names=[]):
        #'''Randomly assign people to Seat objects in the different Table objects'''
        #fill names with names from csv file
        #for name in names: pick a random table and then fill seats
        #OF: randomly pick names from the list that weren't added yet and fill seats in order
        #-> might be preferrable so that people are not on their own
        #check of er nog plaatsen over zijn
            #vs what to do when too little places
        #mss alle mensen in de lijst steken en assignment gelijk zetten met removal vd list
        #kan dan ook nog de namen in de list geven die niet konden geassignd worden wegens plaatsgebrek
            
    #def display():
        #'''display the different tables and there occupants in a nice and readable way'''
        # for table in room1.tables:
    #     table.who_sits_here()
    # def store(filename):
    #     '''store the repartition in an excel file'''


#----------testing----------------
# room1 = Openspace(3)
