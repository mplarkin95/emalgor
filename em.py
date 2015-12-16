import matplotlib.pyplot as plt
from gausian0 import gaus_std, gaus_mix
from mpl_toolkits.mplot3d import Axes3D
import math as M
from normalDistroValues import NormDistVal as nDV


def plot(g):
	fig = plt.figure()
	i = 111
	for a in g:
		x,y,z = g_plot(a)
		ax = fig.add_subplot(i, projection='3d')
		ax.plot_trisurf(x,y,z)
		i=i-1
	
	plt.show()	
#TEST FUCNTION TO FALSIFY STANDARD DEVIATIon
def g_plot(gausian):
	x = gausian.x_mean()
	y = gausian.y_mean()
	x_var = gausian.x_var()
	y_var = gausian.y_var()
	X = []
	Y = []
	Z = []
	for i in range(int(x-2*x_var),int(x+2*x_var)):
		for j in range(int(y-2*y_var),int(y+2*y_var)):
			X.append(i)
			Y.append(j)
			Z.append(gausian.calculate([i,j]))
			
	return (X,Y,Z)

def EM_algorithim(mixture_model,data_set,threshold):
	k = mixture_model.components()
	N = data_set
	count = 0
	while True:
		
		#E-Step
		num_probability_matrix= []
		#find the numerators of points in the probability matrix
		for point in N:
			row = []
			for model in k:
				row.append(model.calculate(point)*mixture_model.weight(model))
			num_probability_matrix.append(row)
		#find the denominators and thus final values for probability matrix
		probability_matrix = []
		high_count = 0
		for row in num_probability_matrix:
			row_sum = sum(row)
			new_row = []
			for point in row:
				n_v = (point/row_sum)
				new_row.append(n_v)
				if n_v >=threshold: high_count+=1
			probability_matrix.append(new_row)
		if high_count > len(N)/3:break
		print str(high_count) +'/'+ str(len(N))
		##########################
		#M-Step
		value_sum_x = [0]*len(k)
		value_sum_y = [0]*len(k)
		value_var_x = [0]*len(k)
		value_var_y = [0]*len(k)
		N_k = [sum(x) for x in zip(*probability_matrix)]

		#calculate numerators for the new mean values of x and y
		for point in xrange(len(probability_matrix)):
			for component in xrange(len(probability_matrix[point])):
				value_sum_x[component] += (probability_matrix[point][component]* N[point][0])
				value_sum_y[component] += (probability_matrix[point][component]* N[point][1])
		#divide numerators by total soft assignments and change the mean
		for i in xrange(len(N_k)):
			k[i].x_mean_change(value_sum_x[i]/N_k[i])
			k[i].y_mean_change(value_sum_y[i]/N_k[i])

		#calculate numerators for the new variance values of x and y
		for point in xrange(len(probability_matrix)):
			for component in xrange(len(probability_matrix[point])):
				value_var_x[component] += (probability_matrix[point][component]* (N[point][0]-k[component].x_mean())*(N[point][0]-k[component].x_mean()))
				value_var_y[component] += (probability_matrix[point][component]* (N[point][1]-k[component].y_mean())*(N[point][1]-k[component].y_mean()))
		#divide numerators by total soft assignment and update variance
		for i in xrange(len(N_k)):
			k[i].x_var_change(value_var_x[i]/N_k[i])
			k[i].y_var_change(value_var_y[i]/N_k[i])

		#update the weights of all models
		
		for component in xrange(len(k)):
			mixture_model.change_weight(component,N_k[component]/len(N))

		count +=1

		
	print str(mixture_model)


			




if __name__ == '__main__':
	# while(1):
	a = gaus_std(1,1,1,1)
	b = gaus_std(2,2,1,1)
	c = gaus_std(3,3,1,1)
	g = gaus_mix(3,a,b,c)
	A = nDV(1,2,1.0,1.5)
	B = nDV(3,3,1.0,1.5)
	C = nDV(5,2,.5,.5)
	print "running training algorithim for 100 samples"
	n = A.calc_norm_dist_val(100)+B.calc_norm_dist_val(100)+C.calc_norm_dist_val(100)
	i = float(raw_input("enter threshold"))
	EM_algorithim(g,n,i)
	print' *****************'
	print "running training algorithim for 200 samples"
	n = A.calc_norm_dist_val(200)+B.calc_norm_dist_val(200)+C.calc_norm_dist_val(200)
	i = float(raw_input("enter threshold"))
	EM_algorithim(g,n,i)
	print '******************'
	print "running training algorithim for 300 samples"
	n = A.calc_norm_dist_val(300)+B.calc_norm_dist_val(300)+C.calc_norm_dist_val(300)
	i = float(raw_input("enter threshold"))
	EM_algorithim(g,n,i)
	print 'Done'
		# print("What do you want to do?")
		# print("Enter g for single gausian, gm for gausian mixture, e to exit")
		# answer = raw_input()
		# if answer == 'g':
		# 	x_mean = float(raw_input("enter x_mean: "))
		# 	y_mean = float(raw_input("enter y_mean: "))
		# 	x_var = float(raw_input("enter x_var: "))
		# 	y_var = float(raw_input("enter y_var: "))
		# 	g= gaus_std(x_mean,y_mean,x_var,y_var)
		# 	print g
		# 	plot([g])
		# elif answer == 'gm':
		# 	print("Please enter information for 3 fixed components")
		# 	x_mean1 = float(raw_input("enter x_mean for the first component: "))
		# 	y_mean1 = float(raw_input("enter y_mean for the first component: "))
		# 	x_var1  = float(raw_input("enter x_var for the first component: "))
		# 	y_var1  = float(raw_input("enter y_var for the first component: "))
		# 	a = gaus_std(x_mean1, y_mean1, x_var1, y_var1)

		# 	x_mean2 = float(raw_input("enter x_mean for the second component: "))
		# 	y_mean2 = float(raw_input("enter y_mean for the second component: "))
		# 	x_var2  = float(raw_input("enter x_var for the second component: "))
		# 	y_var2  = float(raw_input("enter y_var for the second component: "))
		# 	b = gaus_std(x_mean2, y_mean2, x_var2, y_var2)

		# 	x_mean3 = float(raw_input("enter x_mean for the third component: "))
		# 	y_mean3 = float(raw_input("enter y_mean for the third component: "))
		# 	x_var3  = float(raw_input("enter x_var for the third component: "))
		# 	y_var3  = float(raw_input("enter y_var for the third component: "))
		# 	c = gaus_std(x_mean3, y_mean3, x_var3, y_var3)

		# 	g = gaus_mix(3,a,b,c)
		# 	print
		# 	print g
		# 	plot(g.components())			

		# elif answer == 'e':
		# 	break
		# else:
		# 	print "please enter valid input!"