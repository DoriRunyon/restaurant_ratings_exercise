import sys


def show_restaurant_ratings(filename): 

    """Shows ratings by restaurant"""

    with open(filename) as ratings_file:
        restaurant_and_ratings = {}
        for line in ratings_file:
            line = line.rstrip()
            restaurants = line.split(":")
            
            restaurant_and_ratings[restaurants[0]] = restaurants[1]


    alphabetical_restaurants = sorted(restaurant_and_ratings.items())

    for restaurant, rating in alphabetical_restaurants:
        print "%s is rated at %s." % (restaurant, rating)




show_restaurant_ratings(sys.argv[1])            