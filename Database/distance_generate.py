import numpy
from math import *
upper_limit = int(input("Enter the upper limit:\n"))
distance_data = open('distance.txt','a')
j = 0
string_line = ''
for i in range(1,upper_limit):
    j = 0
    string_line = ''
    while j <= i :
        distance_data.write(' ' + str(numpy.round(sqrt(int(i)**2 + j**2),3)))
        j += 1
    distance_data.write('\n')

distance_data.close()