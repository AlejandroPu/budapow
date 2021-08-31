# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:33:01 2021

@author: retac
"""

class StationsPathsInput:

    def __init__( self, nfile ):
        self.mat_stations = nfile

    def start_end_stations( self, start, final ):
        self.start_station = start
        self.final_station = final

    def train_color( self, tcolor="normal" ):
        self.train_color = tcolor
    