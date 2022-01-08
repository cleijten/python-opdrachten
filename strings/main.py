# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_name_1 = 'Ruud Gullit'
scorer_name_2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorer_name_1 + ' ' + str(goal_0) + ', ' + scorer_name_2  + ' ' +  str(goal_1)

report = f'{scorer_name_1} scored in the {goal_0}nd minute\n{scorer_name_2} scored in the {goal_1}th minute'

player = 'Frank Rijkaard'
space = player.find(' ')
first_name = player[:space]
length = len(player)

last_name_len = len(player[space+1:length])

name_short = first_name[0] + '.' + ' ' + player[space+1:14]


chant = (first_name + '! ') * len(first_name)
chant = chant[:-1]

good_chant = chant[:-1] != ' '
print(good_chant)



