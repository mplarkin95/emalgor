import math as M
import numpy as nu

class gaus_std(object):
	"""Make a gausian std distro"""
	def __init__(self, x_mean,y_mean,var_x,var_y):	
		self.x_m = x_mean
		self.y_m = y_mean
		self.x_v = var_x
		self.y_v = var_y

	def calculate(self,point):
		x_m = self.x_m
		x_v = self.x_v
		y_m = self.y_m
		y_v = self.y_v
		x=point[0]
		y=point[1]
		final = 
			(1/(2*M.pi*x_v*y_v))*M.exp(-.5(()))









		