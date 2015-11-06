import math as M
import numpy as nu

#single gausian curve
class gaus_std(object):
	"""Make a gausian std distro"""
	def __init__(self, x_mean,y_mean,var_x,var_y):	
		self.x_m = x_mean
		self.y_m = y_mean
		self.x_v = var_x
		self.y_v = var_y

	def __str__(self):
		return "x mean: "+ str(self.x_m)+"\ny mean: " + str(self.y_m)+"\nx variance: "+ str(self.x_v)+"\ny variance: "+ str(self.y_v) 
	def calculate(self,point):
		x_m = self.x_m
		x_v = self.x_v
		y_m = self.y_m
		y_v = self.y_v
		x=point[0]
		y=point[1]
		return(1/(2*M.pi*M.sqrt(x_v)*M.sqrt(y_v)))*M.exp(-.5*((M.pow((x-x_m),2)/x_v)+(M.pow((y-y_m),2)/y_v)))

	def x_mean_change(self,n):
		self.x_m = n

	def y_mean_change(self,n):
		self.y_m = n

	def x_var_change(self,n):
		self.x_v = n

	def y_var_change(self,n):
		self.y_v = n


#gausian Mixture model
class gaus_mix(object):
	"""Create a mixture model with set number of components"""
	def __init__(self,num_comp,*components):
		if(num_comp != len(components)): raise ValueError('enter correct # of components')
		self.n_c = num_comp
		self.weights = {}
		self.num = []
		for c in components:
			self.weights[c]=1
			self.num.append(c)

	def __str__(self):
		string = ''
		i = 0
		for k in self.num:
			string += "Component "+ str(i)+ '\n'+str(k)+ "\nWeight: "+ str(self.weights[k])+ "\n\n"
			i+=1
		return string
	
	def component(self,n):
		return self.num[n]

	def change_weight(self,component,nWeight):
		self.weights[self.num[component]]=nWeight

# 


#########################
#		TESTING
#########################
a = gaus_std(6,5,1,.8)
b = gaus_std(7,12,.6,1.2)
c = gaus_std(9,11,.9,2.1) 
print "gaus_mix"
print "--------------------"
g= gaus_mix(3,a,b,c)
print g
g.change_weight(1,2)
print g
print "--------------------"


