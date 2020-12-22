"""
Library to get beautiful colors from nord palette
more about nord theme: https://www.nordtheme.com/
"""


from random import choice


red = '#BF616A'
orange = '#D08770'
yellow = '#EBCB8B'
green = '#A3BE8C'
purple = '#B48EAD'

aurora = (red, orange, yellow, green, purple)
frost = ('#8FBCBB', '#88C0D0', '#81A1C1', '#5E81AC')
polar_night = ('#2E3440', '#3B4252', '#434C5E', '#4C566A')
snow_storm = ('#D8DEE9', '#E5E9F0', '#ECEFF4')

blackest = polar_night[0]
whitest = snow_storm[-1]

def rand_aurora():
    return choice(aurora)

def rand_frost():
    return choice(frost)

def rand_polar_night():
    return choice(polar_night)

def rand_snow_storm():
    return choice(snow_storm)

def rand_colorful(inlcude_dark=False, include_white=False):
    colors = [*aurora, rand_frost()]
    if inlcude_dark:
        colors.append(rand_polar_night())
    if include_white:
        colors.append(rand_snow_storm())
    return choice(colors)
    

