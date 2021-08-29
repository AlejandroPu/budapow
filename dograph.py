# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:40:46 2021

@author: retac
"""
import copy

# from a matrix, return a graph form
def mat_to_dic( matrix, train_color ):
    
    graph = {}
    stations = list(matrix.iloc[:,0])
    qstations = len(stations)
    tipos = list( matrix.iloc[:, len(stations)+1] )
    
    # making dic of the net
    for word in range( qstations ):
        graph[stations[word]] = {}
        conections = list(matrix.iloc[0:,(word+1)])
        for conection in range( qstations ):
            if conections[conection] == 1:
                graph[stations[word]][stations[conection]] = conections[conection]
    
    # net remaking for green or red trains
    if (train_color == 'green') or (train_color == 'red'):
        
        red_stations = []
        green_stations = []
        for nstation in range( qstations ):
            if tipos[nstation] == 'green': green_stations.append(stations[nstation])
            if tipos[nstation] == 'red': red_stations.append(stations[nstation])

        # if train is green, delete red stations from the net
        if (train_color == 'green'):
            not_stations = copy.deepcopy( red_stations )
        # if train is red, delete green stations from the net
        if (train_color == 'red'):
            not_stations = copy.deepcopy( green_stations )
            
        for nstation in range( qstations ):
            # conecciones de la estacion nstation
            conect = list(graph[stations[nstation]].keys())
            # estaciones verdes en conect
            matches = list( set(not_stations) & set(conect))
            to_erase = [ stations[nstation] ]
            while( matches != [] ):
                to_erase.append( matches[0] )
                # incluír conecciones de estación verde, directamente
                # en estación nstation
                for new_conect in graph[matches[0]]:
                    graph[stations[nstation]][new_conect] = graph[matches[0]][new_conect]
                for del_station in to_erase:
                    if del_station in graph[stations[nstation]]:
                        del( graph[stations[nstation]][del_station] )
                conect = list(graph[stations[nstation]].keys())
                matches = list( set(not_stations) & set(conect))

    return graph