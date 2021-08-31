# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 19:01:43 2021

Tarea para Buda.com

Dijkstra Algorithm to find shortest path between
starting and ending stations

@author: Francisco Alejandro Retamal Reinoso
based in a video from https://youtu.be/Ub4-nG09PFw
about the dijkstra algorithm, with a few changes like
the infinity definition, variables and function names
and use of "copy" module
"""
from copy import deepcopy as dpc

def dijkstra_stations( graph, s, e ):
    
    infinity = float('inf')
    unseen = dpc( graph )
    track_path = []
    shortest_d = {}
    track_prev = {}
    
    for station in unseen:
        shortest_d[station] = infinity
    shortest_d[s] = 0
    
    while unseen:
        
        min_distance_node = None
        
        for station in unseen:
            if min_distance_node is None:
                min_distance_node = station
            elif shortest_d[station] < shortest_d[min_distance_node]:
                min_distance_node = station
            
        path_options = graph[min_distance_node].items()
        
        for child_node, weight in path_options:
            
            if weight + shortest_d[min_distance_node] < shortest_d[child_node]:
                shortest_d[child_node] = weight + shortest_d[min_distance_node]
                track_prev[child_node] = min_distance_node
                
        unseen.pop(min_distance_node)
        
    currentNode = e
    
    while currentNode != s:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_prev[currentNode]
        
        except KeyError:
            print("Path is not reachable")
            break
        
    track_path.insert( 0, s )
    
    return track_path