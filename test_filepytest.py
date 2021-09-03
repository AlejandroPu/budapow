# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:03:48 2021

This file test was created to test it with pytest

@author: retac
"""

from dograph import mat_to_dic
from shortest_path import dijkstra_stations
from testspath.data_for_tests import data01

# data to test
mat, normal_dic, red_dic, green_dic = data01()

def test_mat_to_dic():
    
    assert mat_to_dic(mat, "normal")==normal_dic
    assert mat_to_dic(mat, "any")==normal_dic
    assert mat_to_dic(mat, "")==normal_dic
    assert mat_to_dic(mat, "red")==red_dic
    assert mat_to_dic(mat, "green")==green_dic

def test_dijkstra():
    
    assert dijkstra_stations( normal_dic, "A", "F" )== \
            ['A', 'B', 'C', 'D', 'E', 'F']
    assert dijkstra_stations( normal_dic, "F", "A" )== \
                ['F', 'E', 'D', 'C', 'B', 'A']
    assert dijkstra_stations( red_dic, "A", "F" )== \
                ['A', 'B', 'C', 'H', 'F']
    assert dijkstra_stations( green_dic, "A", "F" )== \
                ['A', 'B', 'C', 'D', 'E', 'F']

