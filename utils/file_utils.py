def call_data():
    '''returns a list of objects from a csv file'''
    all_colleagues = []

    with open('./new_colleagues.csv', 'r') as file:
        rows = file.readlines()
        for row in rows:
            clean_row = row.strip()  # Remove \n after each name
            all_colleagues.append(clean_row)
    return all_colleagues

call_data()