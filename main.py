# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:42:40 2021

Tarea para Buda.com

@author: Francisco Alejandro Retamal Reinoso
"""
from stations_paths import StationsPathsInput
from stations_file import stations_matrix
from dograph import mat_to_dic
from shortest_path import dijkstra_stations

## INPUT PARAMETERS

# creating an StationsPathsInput Object with inputs
# train_color is usefull only if it is "green" or "red"
this_net = StationsPathsInput( "estaciones02.csv")
this_net.start_end_stations( "A", "F" )
this_net.train_color( "normal" ) 

# getting matrix from CSV File with stations info
mat = stations_matrix(this_net.mat_stations)
# Start and final stations, and train color
start = this_net.start_station
final = this_net.final_station
tcolor = this_net.train_color


## FIND SHORTEST PATH

# dictionary representation to the stations net
dic_net = mat_to_dic(mat, tcolor)

# dijkstra algorithm applied to this problem
# works with dictionary representation of the net
result = dijkstra_stations( dic_net, start, final )

print( "La ruta más corta es: " + str(result))

