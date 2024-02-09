def call_data(source: str='') -> list[str]:
    '''Function that returns a list of objects from a csv file.
    
    :param source: A string that contains the path to a CSV file.
    :return: all_colleagues is a list of names to be assigned to seats.
    '''
    all_colleagues: list[str] = [] # List where each row should be stored

    with open(source, 'r') as file:
        rows = file.readlines()
        for row in rows:
            clean_row = row.strip()  # Remove \n after each name
            all_colleagues.append(clean_row)
    return all_colleagues

