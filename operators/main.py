# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
spain_total_area = 505307
switzerland_total_area = 41277

population_count_spain = 47300000
population_count_switzerland = 8500000
language_most_spoken_spain = 'Spanish'
language_most_spoken_switzerland = 'German'
prevalent_religion_spain = 'Roman Catholic'
prevalent_religion_switzerland = 'Roman Catholic'
capital_length_spain = len('Madrid')
capital_length_switzerland = len('Bern')
gdp_spain = 36200
gdp_switzerland = 68400
population_growth_percentage_spain = -0.03
population_growth_percentage_switzerland = 0.65


print(language_most_spoken_spain == language_most_spoken_switzerland) #1
print(prevalent_religion_spain == prevalent_religion_switzerland) #2
print(capital_length_spain != capital_length_switzerland) #3
print(gdp_switzerland > gdp_spain) #4
print(population_growth_percentage_switzerland < 0.01 and population_growth_percentage_spain < 0.01) #5
print(population_count_switzerland > 10000000 or population_count_spain > 10000000) #6

if ((population_count_spain > 10000000) and (population_count_switzerland < 10000000)) or ((population_count_spain < 10000000) and (population_count_switzerland > 10000000)): Exactly_one_of_the_two_has_population_count_of_over_10_milion = True
else: Exactly_one_of_the_two_has_population_count_of_over_10_milion =  False
print(Exactly_one_of_the_two_has_population_count_of_over_10_milion) #7

