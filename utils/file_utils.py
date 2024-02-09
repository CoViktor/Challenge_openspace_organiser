def call_data(source=''):
    '''returns a list of objects from a csv file'''
    all_colleagues = []

    with open(source, 'r') as file:
        rows = file.readlines()
        for row in rows:
            clean_row = row.strip()  # Remove \n after each name
            all_colleagues.append(clean_row)
    return all_colleagues

