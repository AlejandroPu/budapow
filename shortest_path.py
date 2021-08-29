# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 19:01:43 2021

@author: retac
"""

def dijkstra_stations( graph, s, e ):
    
    shortest_d = {}
    track_prev = {}
    unseenNodes = graph
    infinity = 999999 #representation of infinity
    track_path = []
    
    for station in unseenNodes:
        shortest_d[station] = infinity
    shortest_d[s] = 0
    
    while unseenNodes:
        
        min_distance_node = None
        
        for station in unseenNodes:
            if min_distance_node is None:
                min_distance_node = station
            elif shortest_d[station] < shortest_d[min_distance_node]:
                min_distance_node = station
            
        path_options = graph[min_distance_node].items()
        
        for child_node, weight in path_options:
            
            if weight + shortest_d[min_distance_node] < shortest_d[child_node]:
                shortest_d[child_node] = weight + shortest_d[min_distance_node]
                track_prev[child_node] = min_distance_node
                
        unseenNodes.pop(min_distance_node)
        
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