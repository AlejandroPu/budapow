# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:42:40 2021

Tarea para Buda.com

@author: Francisco Alejandro Retamal Reinoso
"""

import pandas as pnds

def stations_matrix( fname ):
    
    fpath = "archivos/"
    sepchar = [";", ",","\s+"]
    
    matrix = pnds.read_csv( fpath + fname, sep = sepchar[0])

    return matrix

