import sys

restaurant_and_ratings = {}
restaurant_filename = sys.argv[1]

def read_restaurant_ratings(filename = restaurant_filename): 

    """Shows ratings by restaurant"""

    with open(filename) as ratings_file:

        for line in ratings_file:
            line = line.rstrip()
            restaurants = line.split(":")
            
            restaurant_and_ratings[restaurants[0]] = restaurants[1]


    return restaurant_and_ratings


def alphabetical_restaurant_ratings(restaurant_ratings_dict): 
    """Print alphabetically sorted restaurant ratings"""
    

    alphabetical_restaurants = sorted(read_restaurant_ratings(restaurant_ratings_dict).items())

    for restaurant, rating in alphabetical_restaurants:
        print "%s is rated at %s." % (restaurant, rating)



def get_new_restaurant_entry(restaurant_ratings = restaurant_and_ratings): 
    """Get raw input for new restaurant and rating"""

    restaurant_and_ratings = read_restaurant_ratings(restaurant_filename)
    print restaurant_and_ratings

    restaurant_name = ""
    # restaurant_name = raw_input("What is the name of the restaurant you are rating? Or type 'Quit' if done. ")
    # if restaurant_name == "Quit":
    #     return None
    while restaurant_name != "Quit": 
        restaurant_name = raw_input("What is the name of the restaurant you are rating? Or type 'Quit' if done. ")
        if restaurant_name == "Quit":
            break
            #return None
        rating = int(raw_input("What rating do you give this restaurant? "))
        print restaurant_name
        #get_new_restaurant_entry()
        restaurant_and_ratings[restaurant_name] = rating
        print restaurant_and_ratings


    alphabetical_restaurant_ratings(restaurant_and_ratings)


#alphabetical_restaurant_ratings(restaurant_filename) 
get_new_restaurant_entry()
