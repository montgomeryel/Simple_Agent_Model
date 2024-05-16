# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:56:30 2024

@author: Ella
"""

#We want an overarching world class that has an init function that 
##builds a grid, builds agents, and detects vacant positions
##the agent class should determine if happy and move if not
#world needs to have a run method
#visualization: https://github.com/prasenjit52282/GridWorld
    #http://modelingcommons.org/account/login

#setting up the world
parameters = {'world_size':(10,10),
          'num_agents':40,
          'same_pref' :0.4, #desires 40% of neighbors to be same color
          'max_iter'  :100,
          'out_path'  :r'C:\Users\Ella\Documents\GitHub\Simple_Agent_Model\abm_results.csv' }

class Agent():
    def __init__(self, color, pref):
        #needs to know prefrence and location
        self.color = color
        self.pref = pref
        self.location = None
        pass
    def move(self):
        #decide if it wants to move
        #move to new position if it does
        #need to check if happy first 
      happy = self.am_i_happy
      
      if not happy:
          vacancies = self.world.find_vacant(return_all=True) # returns all empty grid spots
          for patch in vacancies:
              i_moved = False
              likeit = self.am_i_happy
              if likeit is True:
                  self.world.grid[self.location] = None
                  self.location = patch
                  self.world.grid[patch] = self
                  i_moved = True