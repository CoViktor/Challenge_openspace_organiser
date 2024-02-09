
class Seat:
    def __init__(self, occupant='Unoccupied'):
        '''Seat class, called when creating a table. Seats are unoccupied by default.
        -set_occupant(name): allows the assignation of a person if the seat is free.
        -remove_occupant(): allows removing someone from a seat.'''
        self.free = True
        self.occupant = occupant
    def set_occupant(self, name):
        self.occupant = name
        self.free = False
    def remove_occupant(self):
        self.occupant = 'Unoccupied'
        self.free = True

# 1.2 Table
class Table:
    def __init__(self, capacity=4):
        '''Table class, called when creating an open space. 
        Capacity is the amount of seats added to this table (default = 4).
        -left_capacity(): returns the amount of unoccupied seats.
        -has_free_spot(): returns True if left_capacity > 0
        -assign_seat(name): assigns a name to a seat.'''
        self.capacity = capacity 
        self.seats = []
        for x in range(capacity):
            seat= Seat()
            self.seats.append(seat)
    def left_capacity(self): #fix this
        empty_seats = 0
        for x in self.seats:
            if x.occupant == 'Unoccupied':
                empty_seats +=1
        return empty_seats

    def has_free_spot(self):
        return self.left_capacity() > 0

    def assign_seat(self, name):
        '''assign_seat(name) that places someone at the table'''
        for seat in self.seats:
            if seat.occupant != 'Unoccupied':
                continue
            else:
                seat.set_occupant(name)
                break
    def who_sits_here(self): #EXTRA: Just for testing whether seat assignment works, make cleaner
        print('At this table is seated:')
        for x in self.seats:
            print(x.occupant)

