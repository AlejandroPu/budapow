# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:42:40 2021

Tarea para Buda.com

@author: Francisco Alejandro Retamal Reinoso
"""

from stations_file import stations_matrix
from dograph import mat_to_dic
from shortest_path import dijkstra_stations

## INPUT PARAMETERS

# CSV File to import stations info
mat = stations_matrix("estaciones02.csv")

# Start and final stations
start = "A"
final = "F"

# optional train color variable, works if it is "green" or "red"
tcolor = "red"



## FIND SHORTEST PATH

# dic representation of the stations net
dic_net = mat_to_dic(mat, tcolor)

# dijkstra algorithm applied to this problem
result = dijkstra_stations( dic_net, start, final )

print(result)
