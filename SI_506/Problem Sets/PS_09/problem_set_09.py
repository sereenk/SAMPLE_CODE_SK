# START PROBLEM SET 09
import csv
print('Problem set 09 \n')

# SETUP
class Meat():
    """
    Representation of a meat

    Attributes:
        name (str): The name of the meat
        emission_per_kg (float): CO2 equivalent emission per kg meat consumption
    """
    def __init__(self, name, emission_per_kg):
        """
        The constructor of the < Meat > class. Here you will need to create
        the attributes ("instance variables") that were described in the < Meat >
        docstring.
        Parameters:
            name (str): The name of the meat
            emission_per_kg (float): CO2 equivalent emission per kg meat consumption

        Returns:
            None
        """

        self.name = name
        self.emission_per_kg = float(emission_per_kg)


    def emit(self, weight):
        """
        This method calculates the CO2 equivalent emission of a given weight for the meat

        Parameters:
            weight (float): The weight of the meat

        Returns:
            float: A float that describes the emission of the meat with givin weight < Meat >
        """
        self.weight = float(weight)
        return self.weight * self.emission_per_kg


class Country():
    """
    Representation of a country

    Attributes:
        code (str): the code of the country
        name (str): the name of the country
        population (int): the population of the country
        meat_co2_emission_per_capita (dict): the co2 emission per capita for different kinds of meat with given weights
        emission_per_capita (float): the co2 emission caused by consumption of meat per capita of the country
        total_emission (float): the total co2 emission caused by consumption of meat of the country
    """

    def __init__(self, code, name, population): 
        """
        The constructor of the < Country > class. Here you will need to create
        the attributes ("instance variables") that were described in the < Country >
        docstring. Note that some of the attributes are defined by parameters passed
        to this constructor method, but others are not.
l
        Parameters:
            code (str): The code of the country
            name (str): The name of the country
            population (int): The population of the country

        Returns:
            None
        """

        self.code = code
        self.name = name
        self.population = population
        self.meat_co2_emission_per_capita = {}
        self.emission_per_capita = float(0)
        self.total_emission = float(0)

    def __str__(self):
        """
        This is the string method for the < Country > class. Whenever an instance of
        < Country > is passed to the str() or print() functions, the return string
        from this method will be returned.

        Parameters:
            None

        Returns:
            str: A string that describes this instance of < Country >
        """

        return f'{self.name} ({self.code}) emitted {self.emission_per_capita} kg co2 caused by meat consumption per capita and {self.total_emission} kg in total'



    def consume(self, meat, weight): 
        """
        This method adds a key:value pair to <meat_co2_emission_per_capita>, where key is the name of the meat
        and the value is the emission of the given weight for that kind of meat

        Parameters:
            meat (Meat): An instance of the Meat class
            weight (float): The weight of the meat that one capita consumes
        Returns:
            None
        """
        self.meat_co2_emission_per_capita[meat.name] = meat.emission_per_kg * weight

    def calculate_total_emission(self):
        """
        This method assigns the sum of the values of <meat_co2_emission_per_capita> to <emission_per_capita>
        and calculates <total_emission> as the product of <population> and <emission_per_capita>

        Parameters:
            None
        Returns:
            None
        """
        for k,v in self.meat_co2_emission_per_capita.items():
            self.emission_per_capita += v
        # self.emission_per_capita = [sum(int(v) )]
        self.total_emission = self.population * self.emission_per_capita


    def get_most_emittable_meat(self):
        """
        This method loops over <meat_co2_emission> and return the name of the meat that has the most CO2 emission

        Parameters:
            None
        Returns:
            str: The name of the most emittable meat of the country
        """

        #return max(meat_co2_emission_per_capita, key=meat_co2_emission_per_capita.get)
        max_value = 0
        for key,value in self.meat_co2_emission_per_capita.items():
            max_value = max(value, max_value)
        
        for key,value in self.meat_co2_emission_per_capita.items():
            if value == max_value:
                return key
        # return key




def read_csv(filepath):
    """Returns a list of dictionaries where each dictionary is formed from the data.

    Parameters:
        filepath (str): a filepath that includes a filename with its extension

    Returns:
        list: a list of dictionaries where each dictionary is formed from the data
    """

    with open(filepath, mode='r', newline='', encoding='utf-8-sig') as file_obj:
        data = list(csv.DictReader(file_obj))
    return data


def write_txt(filepath, data):
    """
    This function takes a filepath and a list of strings as arguments and outputs a txt file.
    For each string in the list, write it with a new line character
    Parameters:
        filepath (str): the filepath that points to the file that will be written.
        data (list): a list of strings that will be written.

    Returns:
        None, but a file is produced.
    """

    with open(filepath, 'w') as file_obj:
        for info in data:
            file_obj.write(str(info) + '\n')

def main():
    """Program entry point.  Handles program workflow.

    Parameters:
        None

    Returns:
        None
    """

    meat_emission = {
        'BEEF': 27.0,
        'PIG': 12.1,
        'SHEEP': 39.2,
        'POULTRY': 6.9,
    }

    # Problem 7.1

    country_population = read_csv('country_population.csv')
    country_meat_consumption = read_csv('country_meat_consumption.csv')

    #print(country_population)

    # meats = {}
    # for k,v in meat_emission.items():
    #     #info = Meat(k,v) 
    #     info = Meat(k,v)
    #     meats[k] = info


    # Problem 7.2 

    countries = {}
    for i in country_population:
        countries[i['Code']] = Country(i['Code'],i['Name'],(float(i['Population(m)']))*1000000)
    return(countries)
    usa = str(countries[-1])

    #a = write_txt("usa.txt", [usa, None])


    # Problem 7.3

    # Problem 7.4

    for i in countries:
        info = Country.calculate_total_emission
        if i['Code'] == 'USA':
            usa2 = str(Country.calculate_total_emission)
            write_txt("usa.txt", [usa, usa2])


    # Problem 7.5


# Do not delete the lines below.
if __name__ == '__main__':
    main()
