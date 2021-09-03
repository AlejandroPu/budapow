# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 20:10:17 2021

@author: retac
"""

def verifications( matrix ):
    
    verification = True
    
    est_col = matrix.keys()[0]=='Estaciones'
    tip_col = matrix.keys()[-1]=='Tipo'
    square = ( len(matrix.keys())-2 )==len(matrix)
    stations = list(matrix.transpose().iloc[0])==list(matrix.keys()[1:-1])
    if square==True:
        simetry = True
        for array in range(len(matrix)):
            line = list(matrix.transpose().iloc[array+1])\
                ==list(matrix.iloc[array])[1:-1]
            simetry = simetry and line
    else:
        simetry = False
    
    values = {
            "est_col": [ est_col, "Falta la columna Estaciones" ],
            "tip_col": [ tip_col, "Falta la columna Tipo" ],
            "square": [ square, "La matriz no es cuadrada" ],
            "stations": [stations, "Asimetría en estaciones de la matriz" ],
            "simetry": [simetry, "Asimetría en datos de la matriz" ]
        }
    for value in values.keys():
        verification = ( verification and values[value][0] )
        if values[value][0]==False:
            print("Verificación "+value+" es incorrecta.")
            print("Existe un error en la matriz de entrada.")
            print(values[value][1])
            break

    
    return verification
