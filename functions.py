import numpy as np
import networkx as nx

def distance(x1,x2,y1,y2):
    dis = np.sqrt(np.power((x1-x2),2)+np.power((y1-y2),2))
    return dis

def seperatedata(final,finalcounter,times,locations,nodes):
    topnode = -1 # keeps track of current top node
    counter = 0 # temporary counter variable
    temptimeback = times[counter]
    temptimefront = times[counter+1]
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
    return topnode

def matriceMaker(adjMatrix,disMatrix,final,tXrange,topnode,totalruns):
    time = 0
    dis = 0
    connection = 0
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
                if dis != 0:
                    disMatrix[time][x].append(connection*(1/dis))
                else:
                    disMatrix[time][x].append(connection*dis)
    return
