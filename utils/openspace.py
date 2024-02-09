
from table import Table
from file_utils import call_data
import random as r
import openpyxl


class Openspace():
    def __init__(self, number_of_tables= 6, seats_per_table=4, data_source='./new_colleagues.csv'):
        '''Class openspace, creates an environment with x tables with y seats each where:
        x= number_of_tables (default= 6) & y= seats_per_table (default= 4).
        -organize(names): takes a list of names, randomly shuffles them and assigns them to seats at tables.
        If some people were unable to be seated, a list will be returned.
        -display(): goes over each table and returns the seat assignment.
        -store(filename): stores the repartition in an excel file. Change source as desired.'''

        self.tables = []
        self.number_of_tables = number_of_tables
        self.seats_per_table = seats_per_table
        self.data_source= data_source
        for x in range(self.number_of_tables):
            table = Table(self.seats_per_table)
            self.tables.append(table)
        self.waiting_line =[]

# The program distributes randomly the people on the existing tables and says how much seats are left.
    def organize(self, names = None):
        '''Calls the data, shuffles the list and then for each person, 
        goes over the tables and their seats and assigns the person to the first available seat.
        Gives feedback on assignment result.'''
        if names is None:
            names = call_data(self.data_source)
        colleagues = names
        remaining_seats = 0
        r.shuffle(colleagues)
        for i in range(len(colleagues)):
            if i >= (self.number_of_tables*self.seats_per_table): 
                    self.waiting_line.append(colleagues[i])
            else:
                for n in range(self.number_of_tables):
                    if not self.tables[n].has_free_spot():
                        continue
                    else:
                        self.tables[n].assign_seat(colleagues[i])
                        break
        for table in self.tables:
            remaining_seats += table.left_capacity()
        if len(self.waiting_line) > 0:
               print(f"The following people were unable to take a seat: {self.waiting_line}\nPlease add {len(self.waiting_line)} chairs.")
        elif remaining_seats > 0:
            print(f"Everybody is seated and there are {remaining_seats} empty seats left.")
        else:
             print('Everybody is seated and all seats are filled.')


    def display(self):
        '''Displays each tables and how the seats are assigned, as well as any unseated people.'''
        for i in range(len(self.tables)):
            seat_assignments = []
            for seat in self.tables[i].seats:
                seat_assignments.append(seat.occupant)
            print(f"At table {i+1} the seats are assigned as follows:\n{seat_assignments}")
        if len(self.waiting_line) > 0:
            print(f'The following people are unseated: {self.waiting_line}')

    def get_seat_assignments(self):
        '''Used for storage for the self.store() function'''
        all_seats=[]
        for i in range(len(self.tables)):
            seat_assignments = [seat.occupant for seat in self.tables[i].seats]
            all_seats.append(["Table " + str(i+1)] + seat_assignments)
        return all_seats

    def store(self, filename= 'Seat_assignments.xlsx'):
        '''Stores the seat assignments and waiting line in an excel file.
        Insert different storage path if desired.'''
        wb = openpyxl.Workbook()
        ws = wb.active
        all_seats = self.get_seat_assignments()

        for row_index, seats in enumerate(all_seats, start=1):
            for col_index, seat in enumerate(seats, start=1):
                ws.cell(row=row_index, column=col_index, value=seat)
        
        #Add waiting line
        if len(self.waiting_line) > 0:
            spacer_row = len(all_seats) + 2
            ws.cell(row=spacer_row, column=1, value="Waiting Line:")
            for index, person in enumerate(self.waiting_line, start=spacer_row + 1):
                ws.cell(row=index, column=1, value=person)

        wb.save(filename)
        print(f'Data stored in {filename}')