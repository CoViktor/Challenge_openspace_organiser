#In openspace.py create a class Openspace that contains these attributes:

# tables which is a list of Table. (you will need to import Table from table.py).

from table import Table, Seat
from file_utils import call_data
import random as r


class Openspace():
    def __init__(self, number_of_tables= 6, seats_per_table=4):
        '''tablecount = amount of tables (default= 4)
        this amount will be assigned on initialisation of the object
        tables = list of all tables in the space'''
        self.tables = []
        self.number_of_tables = number_of_tables
        self.seats_per_table = seats_per_table
        for x in range(self.number_of_tables):
            table = Table(self.seats_per_table)
            self.tables.append(table)
        self.waiting_line =[]

    def organize(self, names = call_data()):
        '''Randomly assign people to Seat objects in the different Table objects'''
        #maak nog random via r.shuffle(colleagues)
        colleagues = names
        full_tables = 0
        for i in range(len(colleagues)):
            #goes over each table
            if i > (self.number_of_tables*self.seats_per_table): 
                    '''Checks if number of student selected in is equal to tables*seats/table, 
                    to see if there's enough places. Should I look for a way to easily swap this parameter from outside?'''
                    self.waiting_line.append(colleagues[i])
                    print(f'{colleagues[i]} has no seat')
            else:
                for n in range(self.number_of_tables):
                    if not self.tables[n].has_free_spot():
                        continue
                    else:
                        for seat in self.tables[n].seats:
                            if seat.occupant == 'Unoccupied':
                                seat.occupant = colleagues[i]
                                print(f'{colleagues[i]} has a seat now')
                                break
                            else:
                                continue
                        break
                #ga over seats
                    #als vol, move table
                    #assign seat
                #als elke table vol, append to waiting_line        
        #check of er nog plaatsen over zijn en print hoeveel
            
        #hou rekening met manier om te zorgen dat niemand op zelfde seat zit als dag ervoor? -> extra

            
    #def display():
        #'''display the different tables and there occupants in a nice and readable way'''
        # for table in room1.tables:
    #     table.who_sits_here()
    # def store(filename):
    #     '''store the repartition in an excel file'''


#----------testing----------------
room1 = Openspace(7)
room1.organize()
for table in room1.tables:
    table.who_sits_here()
print(f"Still unseated are: {room1.waiting_line}")