# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:42:40 2021

Tarea para Buda.com

@author: Francisco Alejandro Retamal Reinoso
"""

import pandas as pnds
from sys import exit
from testspath.matrix_verification import verifications

# This function open the fname archive in the path defined in fpath.
def stations_matrix( fname ):
    
    fpath = "archivos/"
    
    ## Import CVS file to matrix dataframe
    
    sepchar = [";", ",","\s+"]
    
    # sepchar[0] for semicolon separation
    # [1] for comma and [2] for tab or space
    matrix = pnds.read_csv( fpath + fname, sep = sepchar[0])
    
    if verifications(matrix)==False: exit()

    return matrix

