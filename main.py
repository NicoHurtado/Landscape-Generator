from funciones import *

file = 'entrada.txt'

landscape = []

a = 0
b = 0

with open (file) as fileLandscape:
    
    lineOne = []
    first = fileLandscape.readline().rstrip()
    for numero in first.split():
        lineOne.append(numero)
    

    number_of_points = int(lineOne[0])
    for i in range (number_of_points):
        landscape.append(0)
        
    
    for line in fileLandscape:

        line = line.rstrip().split()
        a = int(line[1])
        b = int(line[2])


        if line[0] == "H":
            Hill(landscape, a, b)
            print("Es H")

        elif line[0] == "D":
            Depress(landscape, a, b)
            print("Es D")

        elif line[0] == "R":
            Raise(landscape, a, b)
            print("Es R")

        else:
            Valley(landscape, a, b)
            print("Es V")

for i in landscape:
    print(i)


