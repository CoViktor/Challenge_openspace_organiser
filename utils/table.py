
class Seat:
    def __init__(self, occupant: str='Unoccupied') -> None:
        '''Class called when creating a table. Can store one person.
        
        :param occupant: An str that depicts the person sitting here. Unoccupied by default.
        '''
        self.free = True
        self.occupant = occupant

    def __str__(self) -> str:
        '''Method called during a conversion of the object into a chain.'''
        if self.occupant != 'Unoccupied':
            return f'{self.occupant} is sitting here.'
        else:
            return f'This seat is unoccupied.'

    def set_occupant(self, name: str) -> None:
        '''Function that assigns a person to the seat. Changes occupant to the new occupant and changes the 'free' variable to False.
        
        :param name: A string containing the name to be assigned to be the new occupant of this seat.
        '''
        self.occupant = name
        self.free = False

    def remove_occupant(self) -> None:
        '''Function that allows removing someone from a seat. Changes occupant to Unoccupied and 'free' to True.'''
        self.occupant = 'Unoccupied'
        self.free = True


class Table:
    def __init__(self, capacity: int=4) -> None:
        '''Class called when creating an open space. 
        Will take capacity as the amount of times a Seat class should be created and added to a list: self.seats.

        :param capacity: An int that represents of seats added to this table (default = 4).
        '''
        self.capacity = capacity 
        self.seats = []
        for x in range(capacity):
            seat= Seat()
            self.seats.append(seat)

    def __str__(self) -> str:
        '''Method called during a conversion of the object into a chain.'''
        return f'This is a table with {self.capacity} seats.'  

    def left_capacity(self) -> int:
        '''Function that returns the amount of unoccupied seats at this table as an int.'''
        empty_seats = 0
        for x in self.seats:
            if x.occupant == 'Unoccupied':
                empty_seats +=1
        return empty_seats

    def has_free_spot(self) -> bool:
        '''Function that checks wheter any seats at this table are unnocupied and returns a bool.'''
        return self.left_capacity() > 0

    def assign_seat(self, name: str) -> None:
        '''Function that goes takes a str and goes over the list of seats at this table.
        The str is assigned as occupant to the first available seat that is unoccupied.

        :param name: An str that contains the name of the person who is to be given a seat.
        '''
        for seat in self.seats:
            if seat.occupant != 'Unoccupied':
                continue
            else:
                seat.set_occupant(name)
                break

