import numpy as np
import sys

#global vars
max_green_window=2


#part 1: Read input into proper DSs

def main():
    input_filename= "a.txt"
    f = open(input_filename, "r")
    inp=f.read().splitlines()

    logistics = inp[0].split(" ")
    time = logistics[0]
    n_intersections = logistics[1]
    n_streets = logistics[2]
    n_cars = logistics[3]

    #populate streets dictionary
    streets={}
    for i in range(1,n_streets):
        deets =  inp[i].strip().split(" ")
        streets[deets[2]]=(deets[0], deets[1], deets[3])
        print(streets)


    


if __name__ == "__main__":
    main()