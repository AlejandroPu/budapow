# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:42:40 2021

Tarea para Buda.com

@author: Francisco Alejandro Retamal Reinoso
"""

import pandas as pnds

# This function open the fname archive in the path
# defined in fpath.
def stations_matrix( fname ):
    
    fpath = "archivos/"
    sepchar = [";", ",","\s+"]
    
    # for comma separation character choose sepchar[1]
    # and sepchar[2] to tab or space
    matrix = pnds.read_csv( fpath + fname, sep = sepchar[0])

    return matrix

