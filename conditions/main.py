# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_day, milking_status, location, season, slurry_tank_full, grass_long):
    if (location == "pasture" and time_of_day == "night") or weather == "rainy":
        return 'Take cows to cowshed'
    elif location == "cowshed" and milking_status == True:
        return 'Milk cows'
    elif slurry_tank_full == True and location == "cowshed" and weather not in ("sunny", "windy"):
        return 'Fertilize pasture'
    elif grass_long == True and season == "Spring" and weather == "Sunny" and location != "pasture":
        return 'Mow grass'
    elif weather == "sunny" and time_of_day == "day" and milking_status == True and location == "pasture" and season == "spring" and slurry_tank_full == False and grass_long == True:
        return ("take cows to cowshed\nmilk cows\ntake cows back to pasture")
    return 'wait'

print("1", farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))    
print("2", farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
print("3", farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
print("4", farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))

"""
1. Weather
2. time of day
3. milking status
4. location
5. season
6. slurry tank
7. grass long
"""
    