width = int(input('Please give a width of rectangle'))
assert width > 0, 'The value must be positive'
height = int(input('Please give a height of rectangle'))
assert height > 0, 'The value must be positive'

area = width * height

print(f'Area {area}')