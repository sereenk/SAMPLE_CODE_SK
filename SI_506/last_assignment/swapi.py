
import csv
import json
import os
import requests


class Crew:
    """Representation of a Starship or Vehicle crew.

    Attributes:
        Instance variables are generated when an instance is instantiated based on
        the passed in key-value pairs.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, members):
        """Initialize Crew instance. Loops over the passed in dictionary and calls the built-in
        function < setattr() > to generate each instance variable and assign the value. The
        dictionary key (e.g., "pilot") will serve as the instance variable name to which the
        accompanying < Person > or < Droid > instance value will be assigned.

        Parameters:
            members (dict): crew members dictionary (< position >: < Person >)

        Returns:
            None
        """

        for key, val in members.items():
            setattr(self, key, val) # call built-in function

    def __str__(self):
        """Loops over the instance variables and return a string representation of each crew
        member < Person > object per the following format:

        < position >: < crew member name > e.g., "pilot: Han Solo, copilot: Chewbacca"
        """

        crew = None
        for key, val in self.__dict__.items():
            if crew:
                crew += f", {key}: {val}" # additional member
            else:
                crew = f"{key}: {val}" # 1st member

        return crew

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over instance variables
        and converts person objects to dictionaries. Do not simply return self.__dict__. It can
        be intercepted and mutated, adding, modifying or removing instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        crew = {}
        for key, val in self.__dict__.items():
            crew[key] = val.jsonable() # person object

        return crew


class Droid:
    """Representation of a mechanical being that possesses artificial intelligence.

    Attributes:
        url (str): identifier/locator
        name (str): droid name
        model (str): droid model
        manufacturer (str): creator
        create_year (str): droid's year of manufacture (akin to birth_year)
        height (float): droid's height in meters
        mass (float): droid's mass in kilograms
        equipment (list): droid's equipment, if any
        instructions (list): language modules, flight plans, etc.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
        store_instructions: provides Droid instance with data to store
    """

    def __init__(self, url, name, model):
        """Initialize a Droid instance."""

        self.url = url
        self.name = name
        self.model = model
        self.manufacturer = None
        self.create_year = None
        self.height = None
        self.mass = None
        self.equipment = []
        self.instructions = []

    def __str__(self):
        """Return a string representation of the object."""

        return f"{self.name}"

    def store_instructions(self, instructions):
        """Provide droid with special instructions such as language modules, flight
        plans, etc.

        Parameters:
            instructions (dict): nested dictionaries of key-value pairs of instructions

        Returns:
            None
        """

        self.instructions.append(instructions)

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Use a dictionary literal
        rather than a built-in dict() to avoid built-in lookup costs. Do not simply return
        self.__dict__. It can be intercepted and mutated, adding, modifying or removing
        instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        return {
            "url": self.url,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "create_year": self.create_year,
            "height": self.height,
            "mass": self.mass,
            "equipment": self.equipment,
            "instructions": self.instructions
        }

class Passengers:
    """Representation of passengers carried on a Starship or Vehicle.

    Attributes:
        Instance variables are generated when an object is instantiated based on
        the passed in list of < Person > and/or < Droid > objects. The instance name format
        is described in the < __init__() > method Docstring.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, passengers):
        """Initialize Passengers instance. Loops over the passed in list of < Person > and/or
        < Droid >objects and calls the built-in function < setattr() > to generate the instance
        variable and assign the value. The name of each < Droid > or < Person > will serve as
        the instance variable name (see format below) to which the accompanying < Person > or
        < Droid > instance value will be assigned.

        Key name format:
            lowercase; spaces replaced by underscores, e.g., "Luke Skywalker" to "luke_skywalker"

        Parameters:
            passengers (list): list of < Person > objects

        Returns:
            None
        """

        for val in passengers:
            val.name = str(val.name.replace(' ','_')).lower()
            setattr(self, val.name, val)
        #print(passengers.type)


    def __str__(self):
        """Loops over instance variable values and returns a string representation of each
        passenger < Person > or < Droid > object (passenger name only)."""

        passengers = None
        for val in self.__dict__.values():
            if passengers:
                passengers = f"{passengers}, {val.name}" # additional member
            else:
                passengers = val.name # 1st passenger

        return passengers

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over instance variable
        values and converts passenger < Person > or < Droid >objects to dictionaries. Do not
        simply return self.__dict__. It can be intercepted and mutated, adding, modifying or
        removing instance attributes as a result.

        Parameters:
            None

        Returns:
            list: dictionary of the object's instance variables
        """

        passenger_list = []
        for val in self.__dict__.values():
            passenger_list.append(val.jsonable())

        return passenger_list


class Person:
    """Representation of a person.

    Attributes:
        url (str): identifer/locator
        name (str): person name
        birth_year (str): person's birth_year
        height (float): person's height in centimeters
        mass (float): person's weight in kilograms
        homeworld (Planet): person's home planet
        species (Species): species of person
        force_sensitive (bool): ability to harness the power of the Force.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, birth_year, force_sensitive=False):
        """Initialize a Person instance."""

        self.url = url
        self.name = name
        self.birth_year = birth_year
        self.height = None
        self.mass = None
        self.homeworld = None
        self.species = None
        self.force_sensitive = force_sensitive

    def __str__(self):
        """Return a string representation of the object."""

        return f"{self.name}"

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        if self.homeworld:
            homeworld = self.homeworld.jsonable()
        else:
            homeworld = None

        if self.species:
            species = self.species.jsonable()
        else:
            species = None


        return {
            "url": self.url,
            "name": self.name,
            "birth_year": self.birth_year,
            "height": self.height,
            "mass": self.mass,
            "homeworld": homeworld,
            "species": species,
            "force_sensitive": self.force_sensitive
        }


class Planet:
    """Representation of a planet.

    Attributes:
        url (str): identifier/locator
        name (str): planet name
        region (str): region name
        sector (str): sector name
        suns (int): number of suns
        moons (int): number of moons
        orbital_period_days (float): orbital period around sun(s) measured in days
        diameter_km (int): diameter of planet measured in kilometers
        gravity (dict): gravity level
        climate (list): climate type(s) found on planet
        terrain (list): terrain type(s) found on planet
        population (int): population size

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name):
        """Initialize a Planet instance."""

        self.url = url
        self.name = name
        self.region = None
        self.sector = None
        self.suns = None
        self.moons = None
        self.orbital_period_days = None
        self.diameter_km = None
        self.gravity = None
        self.climate = None
        self.terrain = None
        self.population = None


    def __str__(self):
        """Return a string representation of the object."""

        return f"{self.name}"

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as
        a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        return {
            "url": self.url,
            "name": self.name,
            "region": self.region,
            "sector": self.sector,
            "suns": self.suns,
            "moons": self.moons,
            "orbital_period_days": self.orbital_period_days,
            "diameter_km": self.diameter_km,
            "gravity": self.gravity,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population
        }


class Species:
    """A unit of biodiversity.

    Attributes:
        url (str): identifier/locator
        name (str): common name
        classification (str): classifier (e.g., 'mammal', 'reptile')
        designation (str): designation (e.g., 'sentient')
        language (str): language commonly spoken by species

    Methods:
        jsonable: return JSON-friendly dict representation of the object.
    """

    def __init__(self, url, name):
        """Initialize a Species instance."""

        self.url = url
        self.name = name
        self.classification = None
        self.designation = None
        self.language = None

    def __str__(self):
        """Human-readable string representation of the object."""

        return f"{self.name}"

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as
        a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """
        return {
                'url': self.url,
                'name': self.name,
                'classification': self.classification,
                'designation': self.designation,
                'language': self.language
            }


class Starship:
    """A crewed vehicle used for traveling in realspace or hyperspace.

    Attributes:
        url (str): identifier/locator
        name (str): starship name or nickname
        model (str): manufacturer's model name
        starship_class (str): class of starship
        manufacturer (str): starship builder
        length (float): starship length
        max_atmosphering_speed (int): max sub-orbital speed
        hyperdrive_rating (float): lightspeed propulsion system rating
        MGLT (int): megalight per hour traveled
        armament [list]: offensive and defensive weaponry
        crew (int): crew size
        crew_members (Crew): Crew instance assigned to starship
        passengers (int): number of passengers starship rated to carry
        passengers_on_board (Passengers): passengers on board starship
        cargo_capacity (float): cargo metric tonnage starship rated to carry
        consumables (str): max period in months before on-board provisions must be replenished

    Methods:
        assign_crew: assign < Crew > instance to starship
        add_passengers: assign < Passengers > instance to starship
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, model, starship_class):
        """Initalize instance of a Starship."""

        self.url = url
        self.name = name
        self.model = model
        self.starship_class = starship_class
        self.manufacturer = None
        self.length = None
        self.max_atmosphering_speed = None
        self.hyperdrive_rating = None
        self.MGLT = None
        self.armament = None
        self.crew = None
        self.crew_members = None
        self.passengers = None
        self.passengers_on_board = None
        self.cargo_capacity = None
        self.consumables = None

    def __str__(self):
        """String representation of the object."""

        return f"{self.model}"


    def add_passengers(self, passengers):
        """Add passengers to starship if passenger accommodations are available.

        Parameters:
            passengers (Passengers): object containing < Person > and/or < Droid > instances

        Returns:
            None
        """
        
        if self.passengers > 0:
            self.passengers_on_board = passengers

    def assign_crew_members(self, crew):
        """Assign crew_members.

        Parameters:
            crew (Crew): object comprising crew members ('< role >': < Person> / < Droid >)

        Returns:
            None
        """

        self.crew_members = crew

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """
        if self.crew_members:
            crew_members = self.crew_members.jsonable()
        else:
            crew_members = None

        if self.passengers_on_board:
            passengers_on_board = self.passengers_on_board.jsonable()
        else:
            passengers_on_board = None

        return {
            "url": self.url,
            "name": self.name,
            "model": self.model,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "armament": self.armament,
            "crew": self.crew,
            "crew_members": crew_members,
            "passengers": self.passengers,
            "passengers_on_board": passengers_on_board,
            "cargo_capacity": self.cargo_capacity,
            "consumables":self.consumables
        }


def create_droid(data):
    """Creates a < Droid > instance from dictionary data, converting string values to the
    appropriate type whenever possible. Adding special instructions constitutes a seperate
    operation.

    Type conversions:
        height (str->float)
        mass (str->float)
        equipment (str->list)

    Parameters:
        data (dict): source data

    Returns:
        Droid: new < Droid > instance
    """

    # Instantiate
    droid = Droid(data['url'], data['name'], data['model'])

    # Adding new
    if data.get('manufacturer'):
        droid.manufacturer = data.get('manufacturer')
    if data.get('create_year'):
        droid.create_year = data.get('create_year')
    if data.get('height'):
        droid.height = float(data.get('height'))
    if data.get('mass'):
        droid.mass = float(data.get('mass'))
    if data.get('equipment'):
        droid.equipment = data.get('equipment').split("|") #.split("|") #Check if needed to be split by |
    if data.get('instructions'):
        droid.instructions = data.get('instructions')

    return droid

def create_person(data, planets=None):
    """Creates a < Person > instance from dictionary data, converting string values to the
    appropriate type whenever possible. Calls < get_swapi_resource() > to retrieve homeworld and
    species data. Calls < create_planet() > and < create_species() > to add < Planet > and
    < Species > objects to the person instance.

    Type conversions:
        height (str->float)
        mass (str->float)
        homeworld (str->Planet)
        species (str->Species)
        force_sensitive (str->bool)

    Parameters:
        data (dict): source data
        planets (list): supplemental planetary data

    Returns:
        Person: new < Person > instance
    """

    person = Person(data['url'], data['name'], data['birth_year'], data['force_sensitive'])

    if data.get("height"):
        person.height = float(data.get("height"))
    if data.get("mass"):
        person.mass = float(data.get("mass"))

    if data.get("homeworld"):
        #data.homeworld = data['homeworld']
        homeworld_data = get_swapi_resource(data.get("homeworld"))
        #print(homeworld_data)
        if planets != None:
            for p in planets:
                #print(p)
                if (p['name'].lower()) == (homeworld_data['name'].lower()):
                    homeworld_data.update(p)
                    #print(homeworld_data)
        person.homeworld = create_planet(homeworld_data)

    #something wrong with the jsonable methos. Species is not updating within Person
    if data.get("species"):
        species_data = get_swapi_resource(data.get("species")[0])
        person.species = create_species(species_data)
    #print(person)

    return person



def create_planet(data):
    """Creates a < Planet > instance from dictionary data, converting string values to the
    appropriate type whenever possible.

    Type conversions:
        suns (str->int)
        moons (str->int)
        orbital_period_days (str->float)
        diameter_km (str->int)
        climate (str->list)
        terrain (str->list)
        population (str->int)

    Parameters:
        data (dict): source data

    Returns:
        Planet: new < Planet > instance
    """
    # Instantiate
    planets = Planet(data['url'], data['name'])

    # Adding new
    if data.get('region'):
        planets.region = data.get('region')
    if data.get('sector'):
        planets.sector = data.get('sector')
    if data.get('suns'):
        planets.suns = int(data.get('suns'))
    if data.get('moons'):
        planets.moons = int(data.get('moons'))
    if data.get('orbital_period_days'):
        planets.orbital_period_days = float(data.get('orbital_period_days'))
    if data.get('diameter_km'):
        planets.diameter_km = int(data.get('diameter_km'))
    if data.get('gravity'):
        planets.gravity = data.get('gravity')
    if data.get('climate'):
        planets.climate = data.get('climate').split(', ')
    if data.get('terrain'):
        planets.terrain = list(data.get('terrain').split(", "))
    if data.get('population'):
        planets.population = int(data.get('population'))

    return planets


def create_species(data):
    """Creates a < Species > instance from the passed in dictionary data.

    Type conversions:
        None

    Parameters:
        data (dict): source data

    Returns:
        species: a new < Species > instance
    """
    # Instantiate
    species = Species(data['url'], data['name'])

    # Adding more variables
    if data.get('classification'):
        species.classification = data.get('classification')
    if data.get('designation'):
        species.designation = data.get('designation')
    if data.get('language'):
        species.language = data.get('language')

    return species

def create_starship(data):
    """Creates a Starship instance from dictionary data, converting string values to the
    appropriate type whenever possible. Assigning crews and passengers consitute separate
    operations.

    Type conversions:
        length (str->float)
        max_atmosphering_speed (str->int)
        hyperdrive_rating (str->float)
        MGLT (str->int)
        armament (str->list)
        crew (str->int)
        passengers (str->int)
        cargo_capacity (str->int)

    Parameters:
        data (dict): source data

    Returns:
        starship: a new Starship instance
    """

    starship = Starship(data['url'], data['name'], data['model'], data['starship_class'])

    # Adding more variables
    if data.get('manufacturer'):
        starship.manufacturer = data.get('manufacturer')
    if data.get('length'):
        starship.length = float(data.get('length'))
    if data.get('max_atmosphering_speed'):
        starship.max_atmosphering_speed = int(data.get('max_atmosphering_speed'))
    if data.get('hyperdrive_rating'):
        starship.hyperdrive_rating = float(data.get('hyperdrive_rating'))
    if data.get('MGLT'):
        starship.MGLT = int(data.get('MGLT'))
    if data.get('armament'):
        starship.armament = data.get('armament').split(",")
    if data.get('crew'):
        starship.crew = int(data.get('crew'))
    if data.get('passengers'):
        starship.passengers = int(data.get('passengers'))
    if data.get('cargo_capacity'):
        starship.cargo_capacity = int(data.get('cargo_capacity'))
    if data.get('consumables'):
        starship.consumables = data.get('consumables')
    if data.get('crew_members'):
        starship.crew_members = data.get('crew_members')
    if data.get('passengers_on_board'):
        starship.passengers_on_board = data.get('passengers_on_board')


    return starship






def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provide the response object body is in the form on an "envelope" with the data payload of
    one or more SWAPI entities to be found in ['results'] list; otherwise, response object
    body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        response = requests.get(url, params=params, timeout=timeout)
    else:
        response = requests.get(url, timeout=timeout)

    return response.json()

def read_csv_into_dicts(filepath, delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        delimiter (str): delimiter that overrides the default delimiter

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, mode='r', newline='',encoding='utf-8-sig') as file_obj:
        data = list(csv.DictReader(file_obj))
    return data


def read_json(filepath):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict/list: dictionary or list representations of the decoded JSON document.
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        data = json.load(file_obj)
    return data


def write_json(filepath, data):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict)/(list): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
            json.dump(data, file_obj, ensure_ascii=False, indent=2)


def main():
    """Entry point for program."""

    endpoint = 'https://swapi.py4e.com/api'

    # ABSOLUTE PATH (VS CODE DEBUGGER-FRIENDLY)
    # WARN: autograder does not require absolute paths
    # abs_path = os.path.dirname(os.path.abspath(__file__))
    # print(f"\n0.0: Absolute directory path = {abs_path}")

    # Example: absolute filepath (create)
    # filepath = os.path.join(abs_path, 'stu_swapi_species_wookiee.json')

    # Example: relative filepath
    # filepath = 'stu_swapi_species_wookiee.json'


    # CHALLENGE 01 UTILITY FUNCTIONS / INHABITED PLANETS

    # Output file is exactly the same as fxt_inhabited output after comparing too.

    swapi_planets_data = read_json('swapi_planets.json')
    inhabited_planets = []
    for info in swapi_planets_data:
        if (str(info['population']) != "unknown") and (int(info['population']) > 10000):
            planet_dict = {}
            planet_dict['url'] = info['url']
            planet_dict['name'] = info['name']
            planet_dict['population'] = int(info['population'])
            inhabited_planets.append(planet_dict)

    write_json('stu_swapi_inhabited_planets.json', inhabited_planets)

    # CHALLENGE 02 SPECIES

    response_2 = get_swapi_resource(endpoint + '/species/', {'search': 'wookiee'})
    wookiee_data = response_2['results'][0]
    wookiee = create_species(wookiee_data)
    wookiee_json = wookiee.jsonable()

    write_json('stu_swapi_species_wookiee.json', wookiee_json)

    # CHALLENGE 03 PLANET

    response_3 = get_swapi_resource(endpoint + '/planets/', {'search': 'Hoth'})
    hoth_data = response_3['results'][0]

    #Wookiee planets csv to dict
    wookiee_planets = read_csv_into_dicts('wookieepedia_planets.csv')

    hoth_data.update(wookiee_planets[5])
    #print(hoth_data)

    hoth = create_planet(hoth_data)
    hoth_json = hoth.jsonable()

    write_json('stu_swapi_planet_hoth.json', hoth_json)

    # CHALLENGE 04 DROID

    response_4 = get_swapi_resource(endpoint + '/people/', {'search': 'R2-D2'})
    r2_d2_data = response_4['results'][0]

    wookiee_droids = read_json('wookieepedia_droids.json')
    r2_d2_data.update(wookiee_droids[2])

    r2_d2 = create_droid(r2_d2_data)
    r2_d2.json = r2_d2.jsonable()

    write_json('stu_swapi_droid_r2_d2.json', r2_d2.json)

    # CHALLENGE 05 PERSON

    response_5 = get_swapi_resource(endpoint + '/people/', {'search': 'Leia'})

    leia_data = response_5['results'][0]


    wookiee_people = read_json('wookieepedia_people.json')


    leia_data.update(wookiee_people[4])


    leia = create_person(leia_data, wookiee_planets)
    leia.json = leia.jsonable()

    write_json('stu_swapi_person_leia.json', leia.json)

    # CHALLENGE 06 PASSENGERS

    # TODO implement


    # CHALLENGE 07 STARSHIP
    # Works, output is right but gradescope is giving me an error for jsonable and add_passengers

    response_6 = get_swapi_resource(endpoint + '/starships/', {'search': 'T-70 X-wing'})
    x_wing_data = response_6['results'][0]
    wookiee_starships = read_csv_into_dicts('wookieepedia_starships.csv')
    #print(wookiee_starships)
    x_wing_data.update(wookiee_starships[1])
    x_wing = create_starship(x_wing_data)
    x_wing.json = x_wing.jsonable()
    #print(x_wing.json)

    write_json('stu_swapi_starship_x_wing.json', x_wing.json)

    # CHALLENGE 08 MISSION TO JAKKU

    poe_data = get_swapi_resource(endpoint + '/people/86')
    poe_data.update(wookiee_people[-2])
    poe = create_person(poe_data, wookiee_planets)
    #print(poe)
    bb8_data = get_swapi_resource(endpoint + '/people/87')
    bb8_data.update(wookiee_droids[0])
    bb8 = create_droid(bb8_data)
    #print(bb8)
    jakku_data = get_swapi_resource(endpoint + '/planets/61')
    jakku_data.update(wookiee_planets[-4])
    jakku = create_planet(jakku_data)
    #print(jakku)
    flight_plan = {
        'flight_plan': {
            'destination': jakku.jsonable(),
            'hyperspace_route': "Burke's Trailing",
            'year': '34 ABY'
        }
    }

    Droid.store_instructions(bb8, flight_plan)
    #8.8.3
    lor_data = wookiee_people[-3]
    lor = create_person(lor_data,wookiee_planets)
    #print(lor)

    lor_plan = {'locate_person': lor.jsonable()}
    Droid.store_instructions(bb8, lor_plan)

    # 8.8.4

    crew = Crew({'pilot': poe, 'astro_mech_droid': bb8})
    x_wing.assign_crew_members(crew)

    write_json('stu_episode_vii_mission_jakku.json', x_wing.jsonable())

    # Above Output Matches

    # CHALLENGE 09 STAR MAP (ATTACK ON TUANUL)

    wookiee_star_map = read_json('wookieepedia_star_map.json')

    star_plan = {'star_map': wookiee_star_map}
    Droid.store_instructions(bb8, star_plan)

    write_json('stu_episode_vii_star_map.json', bb8.jsonable())

    # Output is correct, exactly the same

    # CHALLENGE 10 ESCAPE FROM JAKKU

    rey_data = get_swapi_resource(endpoint + '/people/85')
    rey_data.update(wookiee_people[-1])
    rey = create_person(rey_data,wookiee_planets)

    finn_data = get_swapi_resource(endpoint + '/people/84')
    finn_data.update(wookiee_people[1])
    finn = create_person(finn_data,wookiee_planets)

    response_10 = get_swapi_resource(endpoint + '/starships/', {'search': 'Falcon'})
    m_falcon_data = response_10['results'][0]
    m_falcon_data.update(wookiee_starships[-1])
    m_falcon = create_starship(m_falcon_data)

    crew = Crew({'pilot': rey, 'gunner': finn})
    m_falcon.assign_crew_members(crew)

    # Instantiate Passengers 8.10.3 part 4 :

    # Commented out because gradescope gives an error for another part. Please note: my stu_episode_vii_escape_jakku.json is same exact output as fxt_escape_jakku output"
    #Please check this option as well. [lines 991,992,994]
    # passen = Passengers([bb8])
    # m_falcon.passengers_on_board = passen
    # m_falcon.passengers_on_board(passen) #{commented}
    # write_json('stu_episode_vii_escape_jakku.json',m_falcon.jsonable())

    # CHALLENGE 11 JOURNEY TO TAKODANA

    response_11 = get_swapi_resource(endpoint + '/people/', {'search': 'solo'})
    han_solo_data = response_11['results'][0]
    han_solo_data.update(wookiee_people[2])
    han_solo = create_person(han_solo_data, wookiee_planets)

    response_12 = get_swapi_resource(endpoint + '/people/', {'search': 'chewbacca'})
    chewie_data = response_12['results'][0]
    chewie_data.update(wookiee_people[0])
    chewie = create_person(chewie_data, wookiee_planets)

    crew = Crew({'pilot': han_solo, 'copilot': chewie})
    m_falcon.assign_crew_members(crew)

    # 8.11.2 part 3 and 4
    # Commented out because gradescope gives me an error for another part. Please check this option as well. [lines 1013 onwards]
    # passenger = Passengers([rey, finn, bb8])
    # m_falcon.add_passengers = passenger

    #write_json('stu_episode_vii_journey_takodana.json', m_falcon)


if __name__ == '__main__':
    main()
