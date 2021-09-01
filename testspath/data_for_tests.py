# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 16:14:18 2021

@author: retac
"""

import pandas as pds

def data01():
    
    cols = [
        [ 'A', -1, 1, 0, 0, 0, 0, 0, 0, 0, 'normal' ],
        [ 'B', 1, -1, 1, 0, 0, 0, 0, 0, 0, 'normal' ],
        [ 'C', 0, 1, -1, 1, 0, 0, 1, 0, 0, 'normal' ],
        [ 'D', 0, 0, 1, -1, 1, 0, 0, 0, 0, 'normal' ],
        [ 'E', 0, 0, 0, 1, -1, 1, 0, 0, 0, 'normal' ],
        [ 'F', 0, 0, 0, 0, 1, -1, 0, 0, 1, 'normal' ],
        [ 'G', 0, 0, 1, 0, 0, 0, -1, 1, 0, 'green' ],
        [ 'H', 0, 0, 0, 0, 0, 0, 1, -1, 1, 'red' ],
        [ 'I', 0, 0, 0, 0, 0, 1, 0, 1, -1, 'green' ],
    ]
            
    mat = pds.DataFrame( cols, columns = [ 'Estaciones', 'A', 'B', 'C', 'D',
                                           'E', 'F', 'G', 'H', 'I', 'Tipo' ]
                         )
    
    diccionario_normal = {
        'A': {'B': 1},
        'B': {'A': 1, 'C': 1},
        'C': {'B': 1, 'D': 1, 'G': 1},
        'D': {'C': 1, 'E': 1},
        'E': {'D': 1, 'F': 1},
        'F': {'E': 1, 'I': 1},
        'G': {'C': 1, 'H': 1},
        'H': {'G': 1, 'I': 1},
        'I': {'F': 1, 'H': 1}
    }
    diccionario_red = {
        'A': {'B': 1},
        'B': {'A': 1, 'C': 1},
        'C': {'B': 1, 'D': 1, 'H': 1},
        'D': {'C': 1, 'E': 1},
        'E': {'D': 1, 'F': 1},
        'F': {'E': 1, 'H': 1},
        'G': {'C': 1, 'H': 1},
        'H': {'F': 1, 'C': 1},
        'I': {'F': 1, 'H': 1}
    }
    diccionario_green = {
        'A': {'B': 1},
        'B': {'A': 1, 'C': 1},
        'C': {'B': 1, 'D': 1, 'G': 1},
        'D': {'C': 1, 'E': 1},
        'E': {'D': 1, 'F': 1},
        'F': {'E': 1, 'I': 1},
        'G': {'C': 1, 'I': 1},
        'H': {'G': 1, 'I': 1},
        'I': {'F': 1, 'G': 1}
    }
    
    response = [mat, diccionario_normal, diccionario_red, diccionario_green]
    
    return response