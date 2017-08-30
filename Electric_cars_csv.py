#Coursera Python Course 4: Using a csv data file
print "PROGRAM reads a csv data file, 'Electric_cars.csv', and does a few queries on it."
print "Data obtained from 'https://en.wikipedia.org/wiki/List_of_electric_cars_currently_available'  "

import csv
import urllib2
import sqlite3
conn = sqlite3.connect('Electric_carsdb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS ElectricCars''')
cur.execute('''
CREATE TABLE ElectricCars (Manufacturer TEXT, Model TEXT, Top speed INTEGER, Acceleration INTEGER, Capacity INTEGER)''')

print " "
top_speedL = list()
file = 'Electric_cars.csv'
fh = open(file)
print "Retrieving Electric cars data from a csv data file: ", file
connection = open(file)
data = connection.read()

with open('Electric_Cars.csv') as csvfile:
    cars = list(csv.DictReader(csvfile))


print 'Retrieved', len(cars),'items in list'

print " "

print "Electric cars listed:"
print "Manufacturer  Model  Top_speed  Acceleration  Capacity"
for i in range(0, len(cars)):
    manufacturer = str(cars[i]["Manufacturer"])
    model = str(cars[i]["Model"])
    top_speed = cars[i]["Top_speed"]
    acceleration = cars[i]["Acceleration"]
    capacity = cars[i]["Capacity"]
    print manufacturer, model, top_speed, acceleration, capacity

    manufacturerL = str(manufacturer)
    modelL = str(model)
    top_speedI = int(top_speed)
    accelerationL =  float(acceleration)
    capacityL = int(capacity)

    itemTS = top_speedI, manufacturerL, modelL, accelerationL, capacityL
    top_speedL.append(itemTS)


top_speedL.sort(reverse=True)
print " "
print "The car with the highest speed: "
print 'Manufacturer', top_speedL[0][1]
print 'Model', top_speedL[0][2]
print 'Top speed', top_speedL[0][0]
print 'Acceleration', top_speedL[0][0]
print 'Capacity', top_speedL[0][4]   

#determine
