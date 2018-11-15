import numpy as np
import networkx as nx
import ns.applications
import ns.core
import ns.mobility
import ns.network
import ns.csma
import sys
from mobilityTrace import main

main(sys.argv)

def distance(x1,x2,y1,y2):
    dis = np.sqrt(np.power((x1-x2),2)+np.power((y1-y2),2))
    return dis


tXrange = 25 # in meters

file = open("mobility-trace.mob", "r")
lines = file.readlines()
file.close()
numberoflines = len(lines)
varstorage = []

for counterx in range(0,numberoflines):
    words = lines[counterx].split()
    varstorage.append([])
    varstorage[counterx]= words

location = []
nodes = []
velocities = []
locations = []
times = []
for countery in range(0, numberoflines):
    times.append(float((varstorage[countery][0].split("+"))[1].split("n")[0]))
    locations.append(map(float,((varstorage[countery][2].split("="))[1].split(":"))))
    velocities.append(map(float,((varstorage[countery][3].split("="))[1].split(":"))))
    nodes.append(int(varstorage[countery][1].split("=")[1]))



finalcounter = -1
pastnode = 0

for node in nodes:
    finalcounter += 1
topnode = -1
counter = 0
temptimeback = times[counter]
temptimefront = times[counter+1]
final = []
for node in nodes:
    if node > topnode:
        final.append([])
        topnode = node
    if counter != 0:
        temptimeback = times[counter-1]
        if counter == (finalcounter):
            counter += -1
            temptimefront = times[counter+1]
            counter += 1
        else:
            temptimefront = times[counter+1]
    if times[counter] == temptimeback or times[counter] == temptimefront:
        if counter == finalcounter:
            if times[counter] == temptimeback:
                final[node].append([times[counter],locations[counter]])
        else:
            final[node].append([times[counter],locations[counter]])
    counter += 1
connection = 0

adjMatrix = []
disMatrix = []
time = 0
dis = 0
totalruns = len(final[0])
for time in range(totalruns):
    adjMatrix.append([])
    disMatrix.append([])
    for x in range(topnode+1):
        adjMatrix[time].append([])
        disMatrix[time].append([])
        for y in range(topnode+1):
            if x == y:
                connection = 0
            else:
                dis = distance(final[x][time][1][0],final[y][time][1][0],final[x][time][1][1],final[y][time][1][1])
                if dis > tXrange:
                    connection = 0
                else:
                    connection = 1
            adjMatrix[time][x].append(connection)
            disMatrix[time][x].append(connection*dis)
time = 0
G_disweight = []
G_adj = []
for time in range(totalruns):
    G_disweight.append(nx.from_numpy_matrix(np.matrix(disMatrix[time])))
    G_adj.append(nx.from_numpy_matrix(np.matrix(adjMatrix[time])))
    print nx.algebraic_connectivity(G_adj[time], weight='weight', normalized=False, tol=1e-08, method='tracemin_pcg')
