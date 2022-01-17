from helpers import get_countries

__winc_id__ = "25a8041d2d5e4e3ab61ab1be43bfb863"
__human_name__ = "dictionaries"


#1 create passport dictionary
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    country_list = get_countries()
    if nationality in country_list:
        passport = {'name': name, 'date_of_birth': date_of_birth, 'place_of_birth': place_of_birth, 'height': height, 'nationality': nationality}
        return passport
    else:
        return 'Country not found'


#2 add stamp
def add_stamp(passport, country):
    if 'stamps' not in passport:
        passport['stamps'] = [country]
    elif country not in passport['stamps'] and passport['nationality'] != country:
        passport['stamps'].append(country)
    else:
        passport
    return passport

#3 check passport

if __name__ == "__main__":
    countries = get_countries()
    passport_dict = create_passport('Celia Leijten', '1968-02-22', 'Breda', float(1.68), 'Netherlands')
    add_stamp(passport_dict, 'Norway')
    add_stamp(passport_dict, 'Sweden')
    add_stamp(passport_dict, 'Netherlands')    
    print(passport_dict)
