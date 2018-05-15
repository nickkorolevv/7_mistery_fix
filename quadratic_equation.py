from math import sqrt

def get_first_root(major_coef, mid_coef, Discriminant):
    first_root = (-mid_coef - sqrt(Discriminant))/(2 * major_coef)
    return first_root


def get_second_root(major_coef, mid_coef, Discriminant):
    second_root = (-mid_coef + sqrt(Discriminant))/(2 * major_coef)
    return second_root
    

def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        first_root = None
        second_root = None
    elif discriminant == 0:
        first_root = (-b / (2 * a))
        second_root = None

    else: 
        first_root = get_first_root(a, b, discriminant)
        second_root = get_second_root(a, b, discriminant)
    return first_root, second_root
