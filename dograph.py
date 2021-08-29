# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:40:46 2021

Tarea para Buda.com
This module write a stations net matrix into
a dictionary, modifing the net based on the train color
to use the whole net, or discard red stations or green stations

@author: Francisco Alejandro Retamal Reinoso
"""
import copy

def mat_to_dic( matrix, train_color ):
    
    graph = {}
    stations = list(matrix.iloc[:,0])
    qstations = len(stations)
    typestations = list( matrix.iloc[:, len(stations)+1] )
    
    ## making a dictionary from the net
    for word in range( qstations ):
        graph[stations[word]] = {}
        conections = list(matrix.iloc[0:,(word+1)])
        for conection in range( qstations ):
            if conections[conection] == 1:
                graph[stations[word]][stations[conection]] = conections[conection]
    
    ## net remaking for green or red trains
    if (train_color == 'green') or (train_color == 'red'):
        
        # recognize colored stations in lists to red and green
        red_stations = []
        green_stations = []
        for nstation in range( qstations ):
            colorsta = typestations[nstation]
            thisstat = stations[nstation]
            if colorsta == 'green': green_stations.append(thisstat)
            if colorsta == 'red': red_stations.append(thisstat)

        # Depend on train color, recognize stations not allowed
        if (train_color == 'green'):
            not_stations = copy.deepcopy( red_stations )
        if (train_color == 'red'):
            not_stations = copy.deepcopy( green_stations )
        
        # getting out not allowed stations in not_stations list
        for nstation in range( qstations ):
            thisstat = stations[nstation]
            # conections from thisstat
            conect = list(graph[thisstat].keys())
            # not_stations in conect
            matches = list( set(not_stations) & set(conect))
            # stations to delete from conect if there are in
            to_erase = [ thisstat ]
            # process of remake
            while( matches ):
                to_erase.append( matches[0] )
                # add new conections from the station not allowed
                for new_conect in graph[matches[0]]:
                    graph[thisstat][new_conect] = graph[matches[0]][new_conect]
                # delete stations written into to_erase list
                for del_station in to_erase:
                    if del_station in graph[thisstat]:
                        del( graph[thisstat][del_station] )
                conect = list(graph[thisstat].keys())
                matches = list( set(not_stations) & set(conect))

    return graph