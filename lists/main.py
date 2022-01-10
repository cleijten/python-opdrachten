# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

#1 Write a function alphabetical_order that takes one argument: a list of strings that represent film names. It returns a list of the same films in alphabetical order. 
def alphabetical_order(list):
    alphabetical_list = sorted(list)
    return alphabetical_list

films = ['Fiddler on the roof', 'Jaws', 'Star Wars', 'Raiders of the lost Ark', 'Home Alone', 'Armistead']

print(alphabetical_order(films)) #['Armistead', 'Fiddler on the roof', 'Home Alone', 'Jaws', 'Raiders of the lost Ark', 'Star Wars']

#2 Write a function won_golden_globe that takes a film name and returns True or False based on whether or not this movie won a Golden Globe.
# use for loop for putting the list to lower case with .lower()

def won_golden_globe(film):
    won = ['Jaws', 'ET - the Extra-Terrestial', 'Memoirs of a Geisha', 'Star Wars IV', ]
    for i in range(len(won)):
        won[i] = won[i].lower()
    film_lower = film.lower()
   
    if film_lower in won: 
        return True
    else:
        return False

print(won_golden_globe('Jaws')) #True
print(won_golden_globe('JaWs')) #True
print(won_golden_globe('MEMOIRS OF A GEISHA')) #True
print(won_golden_globe('empire of the sun')) #False

#3 Write a function remove_toto_albums that takes a list of strings, removes Joseph's Toto albums from it and returns the tidy list.
# use .remove
movies_list = ['Fiddler on the roof', 'Jaws', 'Star Wars', 'Raiders of the lost Ark', 'Home Alone', 'Armistead']
toto_albums = ['Fahrenheit', 'Old Is New']
movies_list.extend(toto_albums)
print(movies_list)

def remove_toto_albums(movies):
    for element in toto_albums:
        if element in movies:
            movies.remove(element)
    return movies

remove_toto_albums(movies_list)
print(movies_list)



