def int_div(integer, div):
    count = 0
    while integer - div >= 0:
        integer -= div
        count += 1

    return count, integer

def convert_base10_to_x(integer, base):
    a, integer = int_div(integer, base**2)
    b, integer = int_div(integer, base)
    c = integer

    if a >= base:
        return 999
    else:
        return a*100 + b*10 + c

def convert_x_to_base10(integer, base):
    a, integer = int_div(integer, 100)
    b, integer = int_div(integer, 10)
    c = integer
    return a*base**2 + b*base + c

def convert_x_to_y(integer, x, y):
    temp = convert_x_to_base10(integer, x)
    return convert_base10_to_x(temp, y)

print(convert_x_to_y(110, 4, 10))
