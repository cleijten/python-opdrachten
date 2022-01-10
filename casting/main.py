# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1
leek_price = 2
print('Leek is ' + str(leek_price) + ' euro per kilo.')

# Part 2
leek_order = 'leek 4'
leek_pos = leek_order.find('leek ')

length_leek = len('leek')

leek_order_amount = int(leek_order[leek_pos+length_leek+1:len(leek_order)])
sum_total = leek_price * leek_order_amount
print(sum_total)

# Part 3
broccoli_price = 2.34
broccoli_order = 'broccoli 1.6'

broccoli_pos = broccoli_order.find('broccoli')
length_broccoli = len('broccoli')
broccoli_order_amount = float(broccoli_order[broccoli_pos+length_broccoli+1:len(broccoli_order)])

sum_total_broccoli = round((broccoli_price * broccoli_order_amount), 2)

print(str(broccoli_order_amount) + 'kg broccoli costs ' + str(sum_total_broccoli) + 'e')


