# 💺💺💺 Openspace Organiser 💺💺💺
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

A small program to ameliorate organisational culture.

## 🔔 Description 

This program was designed as a way for organisations to increase the atmosphere in their teams. 
In order to better get to know everybody, employees are encouraged to daily switch seats and work side by side
with new people.

Enjoy meeting everybody! 😁

![workspace_img](https://cbx-prod.b-cdn.net/COLOURBOX34905697.jpg?width=1600&height=1600&quality=90)

## 📦 Repo structure

```
.
├── utils/
│   ├── file_utils.py
│   ├── openspace.py
│   └── table.py
├── .gitignore
├── main.py
├── new_colleagues.csv
└── README.md
```

## 🚧 Installation 

1. Clone the repository to your local machine.

2. To run the script, you can execute the `main.py` file from your command line:

    ```
    python main.py
    ```

3. The program is run in python and a few dependencies are used.
Simply press 'windows + R' and copy paste and enter the following lines.

`pip install CSV`

`pip install openpyxl`

## ✔️ Usage 

The script reads your input file, and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "output.csv" file in your root directory. 

```python

#An openspace called room is created. By default it has 6 tables with 4 chairs each.
#Hover over the class to see which parameters need to be adjusted to change this.
room = Openspace()

#A list of names is taken and shuffled. By default the list is aquired from 
#'./new_colleagues.csv'.
#Insert another list between the brackets or by adjusting the data_source parameter in the class creation above.
room.organize()

#The result can be stored in an excel file. The default is 'Seat_assignments.xlsx'.
#Insert a source path as a string between the brackets if a different output destination is desired.
room.store()

```

This program takes as input a number of tables in a room, as well as the amount of chairs at each table.
A list of names can then be provided (manually or via a CSV file).

Each time the program is run, the names will be shuffled and new seats will be assigned and saved in an excel file.
Only 'main.py' should be used to run this code.
An openspace creation, the organizing of the seats, and the storage of the output are already prepared in the template.
Instructions for personalisation are provided in the script.

## ⌚ Timeline 

This project was created over the timespan of 2 days.

## 🙋 Personal Situation 
This is my first personal project created during the [BeCode](https://becode.org/) AI and Datascience training.
The goal of this project was to implement a usecase for what was learned during the first two weeks of our training.
Learning by trial and error excites me, and this was a great way to learn new things and problemsolve myself into some new knowledge.

Connect with me on [LinkedIn](https://www.linkedin.com/in/viktor-cosaert/).