# START PROBLEM SET 07
print('Problem Set 07')

netflix = {
    "TV Show": [
        {'date_added': 'July 31, 2020', 'duration': '3 Seasons',
            'listed_in': 'Reality TV', 'rating': 'TV-PG', 'title': 'Sugar Rush'},
        {'date_added': 'November 18, 2020', 'duration': '1 Season', 'listed_in': 'Reality TV',
            'rating': 'TV-G', 'title': 'Holiday Home Makeover with Mr. Christmas'},
        {'date_added': 'February 21, 2020', 'duration': '1 Season',
            'listed_in': 'TV Comedies, TV Dramas', 'rating': 'TV-MA', 'title': 'Gentefied'},
        {'date_added': 'January 1, 2020', 'duration': '1 Season',
            'listed_in': 'TV Dramas', 'rating': 'TV-MA', 'title': 'Spinning Out'},
        {'date_added': 'April 1, 2020', 'duration': '4 Seasons',
            'listed_in': 'Reality TV', 'rating': 'TV-PG', 'title': 'Nailed It'},
        {'date_added': 'September 18, 2020', 'duration': '1 Season',
            'listed_in': 'TV Dramas, TV Horror, TV Mysteries', 'rating': 'TV-MA', 'title': 'Ratched'},
        {'date_added': 'September 30, 2020', 'duration': '4 Seasons',
            'listed_in': 'TV Comedies', 'rating': 'TV-PG', 'title': 'Man with a Plan'},
        {'date_added': 'May 15, 2020', 'duration': '5 Seasons', 'listed_in': "Kids' TV, TV Action & Adventure, TV Sci-Fi & Fantasy",
            'rating': 'TV-Y7', 'title': 'She-Ra and the Princesses of Power'},
        {'date_added': 'June 26, 2020', 'duration': '1 Season',
            'listed_in': 'Docuseries', 'rating': 'TV-MA', 'title': 'Home Game'},
        {'date_added': 'January 15, 2020', 'duration': '1 Season', 'listed_in': 'Crime TV Shows, Docuseries',
            'rating': 'TV-MA', 'title': 'Killer Inside: The Mind of Aaron Hernandez'},
        {'date_added': 'April 20, 2020', 'duration': '1 Season',
            'listed_in': 'Reality TV', 'rating': 'TV-MA', 'title': 'Cooked with Cannabis'},
        {'date_added': 'July 17, 2020', 'duration': '2 Seasons',
            'listed_in': 'Crime TV Shows, TV Dramas', 'rating': 'TV-14', 'title': 'In The Dark'},
        {'date_added': 'October 2, 2020', 'duration': '1 Season',
            'listed_in': 'Romantic TV Shows, TV Comedies, TV Dramas', 'rating': 'TV-MA', 'title': 'Emily in Paris'},
        {'date_added': 'September 28, 2020', 'duration': '1 Season', 'listed_in': 'Docuseries',
            'rating': 'TV-PG', 'title': 'Whose Vote Counts, Explained'},
        {'date_added': 'December 30, 2020', 'duration': '1 Season',
            'listed_in': 'Reality TV', 'rating': 'TV-G', 'title': 'Best Leftovers Ever!'},
        {'date_added': 'January 23, 2020', 'duration': '1 Season',
            'listed_in': 'TV Action & Adventure, TV Dramas, TV Horror', 'rating': 'TV-MA', 'title': 'October Faction'},
        {'date_added': 'December 15, 2020', 'duration': '2 Seasons',
            'listed_in': 'Docuseries', 'rating': 'TV-MA', 'title': 'Song Exploder'},
        {'date_added': 'October 16, 2020', 'duration': '3 Seasons',
            'listed_in': "Kids' TV, TV Comedies", 'rating': 'TV-Y7', 'title': 'The Last Kids on Earth'},
        {'date_added': 'March 20, 2020', 'duration': '4 Seasons',
            'listed_in': "Kids' TV, TV Dramas, Teen TV Shows", 'rating': 'TV-PG', 'title': 'Greenhouse Academy'},
        {'date_added': 'December 22, 2020', 'duration': '1 Season',
            'listed_in': "Kids' TV", 'rating': 'TV-Y', 'title': 'Rhyme Time Town Singalongs'}
    ],
    "Movie": [
        {'date_added': 'November 24, 2020', 'duration': '46 min', 'listed_in': 'Children & Family Movies, Comedies',
            'rating': 'TV-Y', 'title': 'Dragons: Rescue Riders: Huttsgalor Holiday'},
        {'date_added': 'December 11, 2020', 'duration': '91 min',
            'listed_in': 'Documentaries', 'rating': 'PG-13', 'title': 'Giving Voice'},
        {'date_added': 'April 24, 2020', 'duration': '117 min',
            'listed_in': 'Action & Adventure', 'rating': 'R', 'title': 'Extraction'},
        {'date_added': 'May 1, 2020', 'duration': '42 min', 'listed_in': 'Children & Family Movies',
            'rating': 'TV-Y', 'title': 'Go! Go! Cory Carson: The Chrissy'},
        {'date_added': 'September 10, 2020', 'duration': '102 min', 'listed_in': 'Comedies, Horror Movies',
            'rating': 'TV-MA', 'title': 'The Babysitter: Killer Queen'},
        {'date_added': 'March 13, 2020', 'duration': '95 min',
            'listed_in': 'Dramas', 'rating': 'R', 'title': 'Lost Girls'},
        {'date_added': 'June 24, 2020', 'duration': '104 min',
            'listed_in': 'Documentaries, Sports Movies', 'rating': 'PG-13', 'title': 'Athlete A'},
        {'date_added': 'December 4, 2020', 'duration': '46 min', 'listed_in': 'Children & Family Movies, Comedies',
            'rating': 'TV-Y7', 'title': 'Captain Underpants Mega Blissmas'},
        {'date_added': 'April 14, 2020', 'duration': '55 min', 'listed_in': 'Stand-Up Comedy',
            'rating': 'TV-MA', 'title': "Chris D'Elia: No Pain"},
        {'date_added': 'April 29, 2020', 'duration': '97 min', 'listed_in': 'Documentaries',
            'rating': 'TV-MA', 'title': 'Murder to Mercy: The Cyntoia Brown Story'},
        {'date_added': 'February 4, 2020', 'duration': '60 min', 'listed_in': 'Stand-Up Comedy',
            'rating': 'TV-14', 'title': "Tom Papa: You're Doing Great!"},
        {'date_added': 'January 31, 2020', 'duration': '85 min',
            'listed_in': 'Documentaries, Music & Musicals', 'rating': 'TV-MA', 'title': 'Miss Americana'},
        {'date_added': 'November 22, 2020', 'duration': '99 min', 'listed_in': 'Children & Family Movies, Music & Musicals',
            'rating': 'TV-PG', 'title': 'Dolly Parton’s Christmas on the Square'},
        {'date_added': 'August 20, 2020', 'duration': '17 min', 'listed_in': 'Documentaries, LGBTQ Movies',
            'rating': 'TV-PG', 'title': 'John Was Trying to Contact Aliens'},
        {'date_added': 'January 14, 2020', 'duration': '66 min', 'listed_in': 'Stand-Up Comedy',
            'rating': 'TV-MA', 'title': 'Leslie Jones: Time Machine'},
        {'date_added': 'December 1, 2020', 'duration': '48 min',
            'listed_in': 'Children & Family Movies', 'rating': 'TV-Y', 'title': "Angela's Christmas Wish"},
        {'date_added': 'December 22, 2020', 'duration': '105 min',
            'listed_in': 'Dramas, Romantic Movies', 'rating': 'R', 'title': 'After We Collided'},
        {'date_added': 'October 6, 2020', 'duration': '96 min', 'listed_in': 'Comedies',
            'rating': 'R', 'title': "American Pie 9: Girls' Rules"},
        {'date_added': 'April 30, 2020', 'duration': '97 min',
            'listed_in': 'Thrillers', 'rating': 'TV-14', 'title': 'Dangerous Lies'},
        {'date_added': 'December 27, 2020', 'duration': '71 min',
            'listed_in': 'Comedies', 'rating': 'TV-MA', 'title': 'Death to 2020'}
    ]
}


# PROBLEM 1 (10 points)
print('\nProblem 1')
def extract_duration(duration):
    """
    This function accepts a string as an argument and extracts the integer part from it
    The input string looks like '4 Seasons', '71 min'
    Parameters:
        duration (str): a string representing the duration of a TV show / movie
    Returns:
        int: extracted duration.
    """
    for n in duration:
        n = int(duration.split(" ")[0])
    return n




# PROBLEM 2 (20 points)
print('\nProblem 2')
def extract_month(date):
    """
    This function accepts a string as an argument and extracts the month part from it
    The input string looks like 'August 20, 2020'
    Parameters:
        duration (str): a string representing the added date of a TV show / movie
    Returns:
        str: extracted month.
    """
    for month in date:
        month = date.split(" ")[0]
    return month


def is_month(show, month = None):
    """
    This function accepts two arguments <show> and <month>. <month> has a default value None.
    If <month> is None, this function should return True
    If the value of <month> equals the added month of <show>, this function should return True.
    Otherwise this function should return False

    Parameters:
        show (dict): a dictionary representing the information of a TV show / movie
        month (str): a string representing the month, e.g. 'August'
    Returns:
        boolean: whether <month> matches the added month of the <show>.
    """
    if not month:
       return True
    elif extract_month(show['date_added']) == month:
        return True
    else:
        return False

# PROBLEM 3 (10 points)
print('\nProblem 3')
def is_listed(show, listed = None):
    """
    This function accepts two arguments <show> and <listed>. <listed> has a default value None.
    If <listed> is None, this function should return True
    If the element of <listed> exists in the listed_in of <show>, this function should return True.
    Otherwise this function should return False

    Parameters:
        show (dict): a dictionary representing the information of a TV show / movie
        listed (list): a list of strings representing the categories, e.g. ['Dramas', 'Romantic Movies']
    Returns:
        boolean: whether <month> matches the added month of the <show>.
    """
    if listed == None:
        return True
    else:
        see_list = show['listed_in'].split(', ')
        for i in listed:
            for x in see_list:
                if i == x:
                    return True
            #print("not listed")
    return False


# PROBLEM 4 (30 points)
print('\nProblem 4')
def query(shows, listed = None, month = None, rating = None):
    """
    This function accepts four arguments <shows>, <listed>, <month>, <rating>. <listed>, <month>, <rating> have default values None.
    If any of <listed>, <month>, <rating> is None, it means that condition is ignored.
    This function filters out a list of shows where the element of <listed> exists in the listed_in of the show,
    the values of <month> and <rating> match the corresponding values in the show.

    Create an empty list <filtered_shows>
    Loop over <shows>, for each show, check whether <rating> is None.
    If <rating> is None, we can simply call <is_listed> and <is_month> to check the conditions
    Otherwise, we need to check the condition for <rating> as well
    If all the conditions match, we will append the show to the list <filtered_shows>

    Parameters:
        shows (list): a list of dictionaries representing the information of TV shows / movies to be filtered
        listed (list): a list of strings representing the categories, e.g. ['Dramas', 'Romantic Movies']
        month (str): a string representing the month, e.g. 'August'
        rating (str): a string representing the rating, e.g. 'TV-MA'

    Returns:
        list: a list of shows that match all the conditions thus are filtered out.
    """


    filtered_shows = []
    for show in shows:
        if rating == None:
            if is_listed(show,listed) and is_month(show,month):
                filtered_shows.append(show)
        else:
            if is_listed(show,listed) and is_month(show,month) and show['rating'] == rating :
                filtered_shows.append(show)
    return filtered_shows


# PROBLEM  5 (30 points)
print('\nProblem 5')
def main(netflix):
    """Program entry point. Handles the program workflow.
    Parameters:
        netflix(dict): a dictionary representing the TV shows and movies of netflix
    Returns:
        str: a string representing the information of the longest R rating movie
    """

    r_movie = query(netflix["Movie"], rating = 'R')
    time = 0
    longest_movie = ''
    for info in r_movie:
        a = int(info['duration'].split(" ")[0])
        if a > time:
            time = a
            longest_movie = info


    a = is_listed(longest_movie,['Dramas', 'Romantic Movies'])

    if a == False:
        return f"{longest_movie['title']} is NOT listed!"
    else:
        return f"{longest_movie['title']} is listed!"



if __name__ == '__main__':

    print(main(netflix))

