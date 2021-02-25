import numpy as np
import sys
import os

#global vars
max_green_window=2
print(os.chdir("/Users/ketkiambekar/Documents/GitHub-ketkiambekar/GoogleHashCode/Traffic"))
#part 1: Read input into proper DSs

def main():
    input_filename= "a.txt"
    f = open(input_filename, "r")
    inp=f.read().splitlines()

    logistics = inp[0].split(" ")
    time = int(logistics[0])
    n_intersections = int(logistics[1])
    n_streets = int(logistics[2])
    n_cars = int(logistics[3])

    #populate streets dictionary
    streets={}
    for i in range(1,n_streets+1):
        deets =  inp[i].strip().split(" ")
        streets[deets[2]]=(deets[0], deets[1], deets[3])
    
    #car paths
    cars={}
    for i in range(n_streets+1,n_streets+n_cars+1 ):
        cars[i]=


    #create Numpy Array of snapshots in time where axis 0 = Seconds, axis 1= Intersections, and cells will contain car_number
    snapshot = np.zeroes


    


if __name__ == "__main__":
    main()