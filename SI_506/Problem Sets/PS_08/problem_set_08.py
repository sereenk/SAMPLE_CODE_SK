import csv
from collections import OrderedDict
from pprint import pprint

# Problem 01
def read_txt(filepath, strip = True):
    """
    This function takes a filepath as an argument and returns a list of strings, each being a line from the txt file.
    Before adding a line to the list, this function should first remove any newline (\n) characters from that string

    Parameters:
        filepath (str): A filepath for a txt file

    Returns
        (list): A list of strings, each being a line in from the txt file (with the newlines removed)
    """
    with open(filepath, 'r', encoding='utf-8') as file_obj:
        if strip:
            data = []
            for line in file_obj:
                data.append(line.strip())
            return data
        else:
            return file_obj.readlines()

# Problem 02
def write_txt(filepath, data):
    """
    This function takes a filepath and a list of lists as arguments and outputs each actress along with the movie they
    starred in to a txt file. When outputting to the txt file specified in the filepath, the each line should have the following
    format:

    < actress > - < film >

    Parameters:
        filepath (str): A filepath for a txt file to be written to
        data (list): A list of lists, each representing an actress and the movie she starred in

    Returns:
        None
    """

    with open(filepath, 'w') as file_obj:
        for info in data:
            name = info[0]
            movie = info[1]
            file_obj.write(str(name) + ' - ' + str(movie) + '\n')

# Problem 03
def read_csv(filepath):
    """
    This function takes a filepath for a csv as an argument and returns a list of dictionaries, each
    representing a film.

    The newly created dictionaries will have the following format:
    {
        'Category': < category >,
        'Title': < film title >,
        'Director(s)': < film director(s)
    }

    Parameters:
        filepath (str): A filepath of a csv file to be read from

    Returns:
        (list): A list of dictionaries, each representing a film
    """
    list_info = []
    with open(filepath, 'r', encoding = 'utf-8') as file_obj:
        reader = csv.DictReader(file_obj)
        for info in reader:
            list_info.append(dict(info))
    return list_info



# Problem 04
def sort_films(film_list):
    """
    This function takes a list of film dictionaries as an argument and sorts each film by category.
    Create a dictionary where the keys are the names of the film categories and the values are initially empty lists,
    then loop through the list of films and add each film to the list with the approriate category.
    The final dictionary should have the following format:
    {
        'Animated Feature Film': < list of Animated Feature Film  nominees >,
        'Best Picture': < list of Best Picture nominees >,
        'Documentary (Feature)': < list of Documentary (Feature) nominees >,
        'International Feature Film': < list of International Feature Film nominees >,
        'Short Film (Live Action)': < list of Short Film (Live Action) nominees >
    }

    Parameters:
        film_list (list): A list of dictionaries, each representing a film

    Returns:
        (dict): A dictionary with five key:value pairs
    """
    all_films = {
        'Animated Feature Film': [],
        'Best Picture': [],
        'Documentary (Feature)': [],
        'International Feature Film': [],
        'Short Film (Live Action)': []
    }
    for film in film_list:
        #print(film)
        if film['Category'] == 'Animated Feature Film':
            all_films['Animated Feature Film'].append(film)
        elif film['Category'] == 'Best Picture':
            all_films['Best Picture'].append(film)
        elif film['Category'] == 'Documentary (Feature)':
            all_films['Documentary (Feature)'].append(film)
        elif film['Category'] == 'International Feature Film':
            all_films['International Feature Film'].append(film)
        elif film['Category'] == 'Short Film (Live Action)':
            all_films['Short Film (Live Action)'].append(film)

    return all_films

# Problem 05
def write_csv(filepath, data):
    """
    This function takes a csv filepath and a list of dictionaries as arguments and outputs them
    to the specified csv file. 

    Parameters:
        filepath (str): A filepath of a csv file to be written to
        data (list): A list of dictionaries, each representing a film

    Returns:
        None
    """
    with open(filepath, 'w', encoding = 'utf-8') as file_obj:
        #data = list(data)
        writer = csv.DictWriter(file_obj,['Category','Title','Director(s)'])
        writer.writeheader()
        writer.writerows(data)


def main():
    """
    This function serves as the point of entry and controls the flow of this Python script

    Parameters:
        None

    Returns:
        None
    """
    # Problem 01
    print("Problem 01:\n")
    best_actors = read_txt('best_actor.txt')

    # Problem 02
    print("Problem 02:\n")
    best_actresses = [
        ['Viola Davis', 'Ma Rainey\'s Black Bottom'],
        ['Andra Day', 'The United States vs. Billie Holiday'],
        ['Vanessa Kirby', 'Pieces of a Woman'],
        ['Frances McDormand', 'Nomadland'],
        ['Cary Mulligan', 'Promising Young Woman']
    ]

    write_txt('best_actress.txt', best_actresses)


    # Problem 03
    print("Problem 03:\n")
    films = read_csv('nominees.csv')


    # Problem 04
    print("Problem 04:\n")
    sorted_films = sort_films(films)
    #print(sorted_films)

    animated_films = sorted_films['Animated Feature Film']
    best_films = sorted_films['Best Picture']
    documentaries = sorted_films['Documentary (Feature)']
    international_films = sorted_films['International Feature Film']
    short_films = sorted_films['Short Film (Live Action)']

    print(best_films)
    # Problem 05    
    print("Problem 05:\n")

    write_csv('best_picture.csv', best_films)


if __name__ == '__main__':
    main()

