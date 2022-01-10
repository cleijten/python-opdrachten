from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

#1 get shortest countries with for loop and len

length_list = []
shortest_names_list = []

def shortest_names(country_list):
    for country in country_list:
        length_list.append(len(country))
    sorted_list = sorted(length_list)
    shortest_length = sorted_list[0]
    for country in country_list:
        if len(country) == shortest_length:
            shortest_names_list.append(country)
    return shortest_names_list

#2 get top 3 countries that have most vowels in name (aeiou)

country_vowels = []

def most_vowels(country_list):
    for country in country_list:
        chars_country = list(country.lower())
 #       print(chars_country)
        nbr_of_vowels = 0
        for char in chars_country:
            if char in ['a', 'e', 'o', 'u', 'i']:
                
                nbr_of_vowels += 1
        country_vowels.append([country, nbr_of_vowels])
    sorted_country_vowels = sorted(country_vowels, key = lambda x: x[1])[-3:]
    return(sorted_country_vowels)

        

#3 list of country names that can form the alphabet

def alphabet_set(country_list):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    checked_countries = []
    found_letters = []

    for country in country_list:
        contains_newletter = False
        for c in country:
            char = c.lower()
            if char in alphabet:
                if char not in found_letters:
                    contains_newletter = True
                    found_letters.append(char)
        if contains_newletter:
            checked_countries.append(country)
        
        if len(checked_countries) <= 14 and len(found_letters) == 26:
            return(f'we were able to to find all the chars within {len(checked_countries)} countries. The countries: {checked_countries}')

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
shortest_names(countries)

most_vowels(countries)

alphabet_set(countries)