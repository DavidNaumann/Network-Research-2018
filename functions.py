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

"""
    Data pack organization:
    data[time][selection]
    selection:
        0: current time
        1: array of algebraic_connectivity
        2: array of average_clustering
        3: array of closeness
        4: array of degree_centrality
        5: edge_betweenness
        6: node_betweenness
    [[time,[algebraic_connectivity],[average_clustering],[closeness],[degree_centrality],[node_betweenness],[edge_betweenness]]

"""

def data_pack_define(adj_data_pack,disweight_data_pack,disMatrix,adjMatrix,time,runs):
    G_disweight = nx.from_numpy_matrix(np.matrix(disMatrix))
    G_adj = nx.from_numpy_matrix(np.matrix(adjMatrix))
    no_nodes = len(G_adj)
    no_edges = G_adj.size()
    norm_alg_con = nx.algebraic_connectivity(G_adj, weight='weight', normalized=False, tol=1e-08, method='tracemin_pcg')
    norm_avg_clu = nx.average_clustering(G_adj,weight='weight')
    norm_closeness = np.mean(list(nx.closeness_centrality(G_adj,u=None,distance='weight')))
    norm_deg = np.mean(list(nx.degree_centrality(G_adj).values()))
    if no_nodes >= 1:
        norm_n_betweenness = np.mean(list(nx.betweenness_centrality(G_adj,normalized=True,weight='weight').values()))
    else:
        norm_n_betweenness = 0
    if no_edges >= 1:
        norm_e_betweenness = np.mean(list(nx.edge_betweenness_centrality(G_adj, normalized=True, weight='weight').values()))
    else:
        norm_e_betweenness = 0
    norm_arr = [norm_alg_con,norm_avg_clu,norm_closeness,norm_deg,norm_n_betweenness,norm_e_betweenness]
    counter = 0
    if runs == 0:
        for items in norm_arr:
            adj_data_pack[time][1].append([])
            adj_data_pack[time][1][counter].append(norm_arr[counter])
            counter = counter + 1
    else:
        for items in norm_arr:
            adj_data_pack[time][1][counter].append(norm_arr[counter])
            counter = counter + 1
    return
