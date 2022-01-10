# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
#1
def greet(name):
    return f'Hello, {name}!'

greet("Celia")

#2
def add(a, b, c):
    return a + b + c

add(5, 6, 1)   

#3
def positive(number):
    if number > 0: return True
    else: return False

positive(-10)
positive(15)
positive(0)  

def negative(number):
    if number < 0: return True
    else: return False

negative(-2)
negative(2)



