
class Seat:
    def __init__(self, occupant='Unoccupied'):
        '''This is class info'''
        self.free = True
        self.occupant = occupant
    def set_occupant(self, name):
        '''which allows the program to assign someone a seat if it's free'''
        if self.free:
            # -> not needed since assignment checks for free? might remove later
            self.occupant = name
            self.free = False
        else:
            print('This seat is occupied') # -> not needed ? might remove later
    def remove_occupant(self):     #see if in need to check for occumants or any failsafe
        ''' which remove someone from a seat and return the name of the person occupying the seat before'''
        self.occupant = 'Unoccupied'
        self.free = True

# 1.2 Table
class Table:
    def __init__(self, capacity=4):
        '''# In the same file, create a class Table with ? attributes:

# capacity which is an integer
# seats which is a list of Seat objects (size = capacity)
# and 3 functions :

'''
        self.capacity = capacity #total number seats at the table, inputted when setting it up
        self.seats = [] # list of Seat objects, len= capacity -> find way to cleanly store 6 obj.Seat() in here
        for x in range(capacity):
            seat= Seat()
            self.seats.append(seat)
    def left_capacity(self): #find way to make this shorter and cleaner, can i do this in 2 lines?
        '''left_capacity() that returns an integer'''
        empty_seats = 0
        for x in self.seats:
            if x.occupant == 'Unoccupied':
                empty_seats +=1
        return empty_seats

    def has_free_spot(self):
        '''# has_free_spot() that returns a boolean (True if a spot is available)'''
        if self.left_capacity() > 0:
            return True

    def assign_seat(self, name):
        '''assign_seat(name) that places someone at the table'''
        for seat in self.seats:
            if seat.occupant != 'Unoccupied':
                continue
            else:
                seat.occupant = name
                break
    def who_sits_here(self): #Just for testing whether seat assignment works
        print('At this table is seated:')
        for x in self.seats:
            print(x.occupant)

