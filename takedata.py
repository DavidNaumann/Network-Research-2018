import numpy as np
import networkx as nx
import ns.applications
import ns.core
import ns.mobility
import ns.network
import ns.csma
import sys
from mobilityTrace import siumulate
from functions import *



tXrange = 8 # Transmission range in meters
tRuns = 5  # Total runs
nNodes = 3 # number of nodes
for runs in range(1,tRuns):
    simulate(sys.argv,nNodes)
    # File variable
    file = open("mobility-trace.mob", "r")
    # Lines in file
    lines = file.readlines()
    file.close() # Closes file for first run
    # Number of lines in file
    numberoflines = len(lines)
    # Data dump for all word chunks in lines split by spaces
    varstorage = []

    # Read the file and seperate data by spaces

    for counterx in range(0,numberoflines):
        # Splits words by spaces
        words = lines[counterx].split()
        # appends an array for placing the split word arays
        varstorage.append([])
        """
        Add word chunks into array in organization of:

        """
        varstorage[counterx]= words

    # for all locations in the file
    location = []
    # for all node numbers in the file
    nodes = []
    # for all locations in the file
    locations = []
    # for all times in the file
    times = []

    """
    Further in depth split based on appereances of:
        + and n characters in time words
        = and : characters in location words
        = characters in node words
    """
    for countery in range(0, numberoflines):
        times.append(float((varstorage[countery][0].split("+"))[1].split("n")[0]))
        locations.append(map(float,((varstorage[countery][2].split("="))[1].split(":"))))
        nodes.append(int(varstorage[countery][1].split("=")[1]))

    """
    Organization of times, locations and nodes arrays is as follows:
        times is an array of all of the times (time0 for node 0 ,time0 for node 1,time1 for node 0,time1 for node 1,...,etc.)
        locations is an array of all of the locations(location0 for node 0,locatio 0 for node 1,...,etc)
        nodes is an array of all of the nodes (number of node0, number of node1,number of node0,number of node1)
    *** For two nodes, more nodes would expand these arrays ***
    """

    finalcounter = -1 # final number of nodes

    for node in nodes:
        finalcounter += 1
    final = []
    """
    Final is the array of the parsed data formated thusly:
        [[]]
    """
    topnode = seperatedata(final,finalcounter,times,locations,nodes)

    adjMatrix = [] # stores adjency matrices in array
    disMatrix = [] # stores distance weighted matrices in array
    totalruns = len(final[0])

    matriceMaker(adjMatrix,disMatrix,final,tXrange,topnode,totalruns)

    time = 0
    G_disweight = []
    G_adj = []

    """
    Data organization:
    data[time][selection]
    selection:
        0: current time
        1: array of algebraic_connectivity
        2: array of average_clustering
        3: array of closeness
        4: array of degree_centrality
        5: edge_betweenness
        6: node_betweenness
    [[time,[algebraic_connectivity],[average_clustering],[closeness],[degree_centrality],[edge_betweenness],[node_betweenness]]

    """
    selection_name = ["Time","Algebraic Connectivity","Average Clustering","Closeness","Degree Centrality","Edge Betweenness","Node Betweeness"]
    for time in range(totalruns):
        G_disweight.append(nx.from_numpy_matrix(np.matrix(disMatrix[time])))
        G_adj.append(nx.from_numpy_matrix(np.matrix(adjMatrix[time])))
        print nx.algebraic_connectivity(G_adj[time], weight='weight', normalized=False, tol=1e-08, method='tracemin_pcg')

print adjMatrix[1]
