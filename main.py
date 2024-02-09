from utils.openspace import Openspace


# ====Welcome to the Openspace Organiser====
#The readme contains a full explanation of this project.
#Enjoy

#An openspace called room is created. By default it has 6 tables with 4 chairs each.
#Hover over the class to see which parameters need to be adjusted to change this.
room = Openspace()
#A list of names is taken and shuffled. By default the list is aquired from './new_colleagues.csv'.
#Insert another list between the brackets or by adjusting the data_source parameter in the class creation above.
room.organize()
#The result can be stored in an excel file. The default is 'Seat_assignments.xlsx'.
#Insert a source path as a string between the brackets if a different output destination is desired.
room.store()
