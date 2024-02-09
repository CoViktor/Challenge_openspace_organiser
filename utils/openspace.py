
from table import Table, Seat
from file_utils import call_data
import random as r


class Openspace():
    def __init__(self, number_of_tables= 6, seats_per_table=4):
        '''Class openspace, creates an environment with x tables with y seats each where:
        x= number_of_tables (default= 6) & y= seats_per_table (default= 4).
        -organize(names): takes a list of names, randomly shuffles them and assigns them to seats at tables.
        If some people were unable to be seated, a list will be returned.
        -display(): goes over each table and returns the seat assignment.
        -store(filename): stores the repartition in an excel file.'''

        self.tables = []
        self.number_of_tables = number_of_tables
        self.seats_per_table = seats_per_table
        for x in range(self.number_of_tables):
            table = Table(self.seats_per_table)
            self.tables.append(table)
        self.waiting_line =[]

    def organize(self, names = call_data()):
        '''default list of names= call_data(), adjust data-source in file_utils.py if needed'''
        colleagues = names
        r.shuffle(colleagues)
        for i in range(len(colleagues)):
            #goes over each table
            if i > (self.number_of_tables*self.seats_per_table): 
                    self.waiting_line.append(colleagues[i])
            else:
                for n in range(self.number_of_tables):
                    if not self.tables[n].has_free_spot():
                        continue
                    else:
                        self.tables[n].assign_seat(colleagues[i])
                        break
        if len(self.waiting_line) > 0:
               print(f"The following people were unable to take a seat: {self.waiting_line}\nPlease add {len(self.waiting_line)} chairs.")
        else:
             print('Everybody is seated.')
    def display(self):
         for i in range(len(self.tables)):
            seat_assignments = []
            for seat in self.tables[i].seats:
                seat_assignments.append(seat.occupant)
            print(f"At table {i+1} the seats are assigned as follows:\n{seat_assignments}")
            
    # def store(filename):
    #     '''store the repartition in an excel file'''


#----------testing----------------
room1 = Openspace(5)
room1.organize()
room1.display()
#issue: 1 person missing? -> unrandomize & play with 6/5 tables
#hou rekening met manier om te zorgen dat niemand op zelfde seat zit als dag ervoor? -> extra
