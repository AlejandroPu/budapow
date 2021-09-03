# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:12:12 2021

Test with unittest module

@author: retac
"""

import unittest
from dograph import mat_to_dic
from shortest_path import dijkstra_stations
from testspath.data_for_tests import data01

#data to test
mat, normal_dic, red_dic, green_dic = data01()

class TestShortestNet(unittest.TestCase):

    def test_mat_to_dic(self):

        self.assertEqual( mat_to_dic(mat, "normal"), normal_dic )
        self.assertEqual( mat_to_dic(mat, "any"), normal_dic )
        self.assertEqual( mat_to_dic(mat, ""), normal_dic )
        self.assertEqual( mat_to_dic(mat, "red"), red_dic)
        self.assertEqual( mat_to_dic(mat, "green"), green_dic )
        
    def test_dijkstra(self):
        
        self.assertEqual( dijkstra_stations( normal_dic, "A", "F" ), \
                ['A', 'B', 'C', 'D', 'E', 'F'] )
        self.assertEqual( dijkstra_stations( normal_dic, "F", "A" ), \
                ['F', 'E', 'D', 'C', 'B', 'A'] )
        self.assertEqual( dijkstra_stations( red_dic, "A", "F" ), \
                ['A', 'B', 'C', 'H', 'F'] )
        self.assertEqual( dijkstra_stations( green_dic, "A", "F" ), \
                ['A', 'B', 'C', 'D', 'E', 'F'] )
        
if __name__ == '__main__':
    unittest.main()