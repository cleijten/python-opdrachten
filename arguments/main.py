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
    gravity = 9.8

    if body == 'sun':
        gravity = 274
    elif body == 'jupiter':
        gravity = 24.9
    elif body == 'neptune':
        gravity = 11.2
    elif body == 'saturn':
        gravity = 10.4
    elif body == 'uranus':
        gravity = 8.9
    elif body == 'venus':
        gravity = 8.9
    elif body == 'mars':
        gravity = 3.7
    elif body == 'mercury':
        gravity = 3.7
    elif body == 'moon':
        gravity = 1.6
    elif body == 'pluto':
        gravity = 0.6
    force_calc = mass * gravity
    return print(round(force_calc, 2))

force(1)
force(1.2, 'jupiter')
force(2, 'sun')

#3 Gravity
def pull(m1, m2, d):
    gravity = (6.674 * (10 ** -11))
    outcome = gravity * ((m1 * m2) / (d ** 2))
    return print(outcome)

mass_earth = (5.972 * (10 ** 6))
pull(800, 1500, 3)
pull(0.1, mass_earth, 6371000)



