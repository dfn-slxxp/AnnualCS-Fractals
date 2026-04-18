import turtle_functions
# Welcome to our project!
#
# In this file, you can find all the options you *can* customize
#
#
# With the Julia Set, it can look completely different depending on the c value you add
# So feel free to play with that!
#
# Here are the options!
#
#
# This is the c value
# The first term in the list represents the real part of c
# While the second represents the imaginary part. (second value * i)
# You can think about it like the array being [a, b]
# And c = a + bi
# For some ideas of c values to try, visit https://en.wikipedia.org/wiki/Julia_set#Quadratic_polynomials
# The following preset is the example in the bottom of the "pseudocode" section
c = [-0.835, -0.321]
#
# This is the "escape radius"
# It is the boundary that determines whether a point is within the Julia Set
# Leaving it at 2 is generally the best idea
R = 2
#
# The max iteration count affects the detail of the set.
# Increasing this number can make the map more detailed, but as a result will make it slower to run for the first time
# Since we cache previous calculations, running it once will save the results of the recursion
# But the turtle drawing each dot still takes minutes
max_iteration = 500
#
# This is the width and height of the map
# This will affect how big the map will be, also make it more or less detailed
# But increasing these will more greatly affect the time it takes to draw
# Since python's turtle is not instant and can get slow
width = 300
height = 300
#
# These are the 2 colors the map interpolates between. 
# The first color, [r, g, b], is the dark color
# That can be found on the edge of the screen
# While the second color is the lighter color
# That is found in the middle of the screen where the point "escapes" near-instantly
color1 = [32, 0, 46]
color2 = [255, 105, 180]
#
# And there you go! This line simply runs the code with these settings, generating your Julia Set!
turtle_functions.create_julia_set_map(c, R, max_iteration, width, height, color1, color2)
#
# Have fun playing around with this!
# - Sebastian Waldman, Emily Kagan, Warren Andrews