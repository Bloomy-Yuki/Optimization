from numpy import round
from math import *
def write_data_set(upper_limit):
    #Setting up the upper limit of the data
    #Opening up the file once again to fill it up with potentially new information
    distance_data = open('distance.txt','a')
    row = 0
    #Filling out information anout the computation
    for col in range(0,upper_limit):
        distance_data.write(str(int(col)))
        row = 1
        while row <= upper_limit - 1:
            #What to fill in every line is expressed here in the expression
            distance_data.write(', '  + str(round(sqrt(int(col)**2 + row**2),3)))
            row += 1
        distance_data.write('\n')
    distance_data.close()
    return print("Done \n")
