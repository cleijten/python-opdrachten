# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

#1 Greeting template
def greet(name, greeting_template='Hello, <name>!'):

    msg = greeting_template.replace("<name>", name)
    return msg

print(greet('Doc'))
print(greet("Bob", "What's up, <name>!"))

#2 Force
def force(mass, body='earth'):
    planets = {'sun': 274, 'jupiter': 24.9, 'neptune': 11.2, 'saturn': 10.4, 'uranus': 8.9, 'venus': 8.9, 'mars': 3.7, 'mercury': 3.7, 'moon': 1.6, 'pluto': 0.6, 'earth': 9.8 }
    gravity_planet = planets.get(body)
    force_calc = mass * gravity_planet
    return round(force_calc, 2)

force(1)
force(1.2, 'jupiter')
force(2, 'sun')

#3 Gravity
def pull(m1, m2, d):
    gravity = (6.674 * (10 ** -11))
    outcome = gravity * ((m1 * m2) / (d ** 2))
    return outcome

mass_earth = (5.972 * (10 ** 6))
pull(800, 1500, 3)
pull(0.1, mass_earth, 6371000)



