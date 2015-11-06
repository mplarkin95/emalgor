import matplotlib.pyplot as plt
import gausian0
from mpl_toolkits.mplot3d import Axes3D
import math as M


def plot(x,y,z):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.plot_trisurf(x, y, z)
	plt.show()

def g_plot(x,y,x_var,y_var):
	g= gausian0.gaus_std(x,y,x_var,y_var)
	X = []
	Y = []
	Z = []
	for i in range(int(x-2*x_var),int(x+2*x_var)):
		for j in range(int(y-2*y_var),int(y+2*y_var)):
			X.append(i)
			Y.append(j)
			Z.append(g.calculate([i,j]))
			
	plot(X,Y,Z)




if __name__ == '__main__':
	while(1):
		print("What do you want to do?")
		print("Enter g for single gausian, gm for gausian mixture, e to exit")
		answer = raw_input()
		if answer == 'g':
			x_mean = float(raw_input("enter x_mean: "))
			y_mean = float(raw_input("enter y_mean: "))
			x_var = float(raw_input("enter x_var: "))
			y_var = float(raw_input("enter y_var: "))

			g_plot(x_mean,y_mean,x_var,y_var)
		elif answer == 'gm':
			print("Please enter information for 3 fixed components")
			x_mean1 = float(raw_input("enter x_mean for the first component: "))
			y_mean1 = float(raw_input("enter y_mean for the first component: "))
			x_var1  = float(raw_input("enter x_var for the first component: "))
			y_var1  = float(raw_input("enter y_var for the first component: "))
			a = gausian0.gaus_std(x_mean1, y_mean1, x_var1, y_var1)

			x_mean2 = float(raw_input("enter x_mean for the second component: "))
			y_mean2 = float(raw_input("enter y_mean for the second component: "))
			x_var2  = float(raw_input("enter x_var for the second component: "))
			y_var2  = float(raw_input("enter y_var for the second component: "))
			b = gausian0.gaus_std(x_mean2, y_mean2, x_var2, y_var2)

			x_mean3 = float(raw_input("enter x_mean for the third component: "))
			y_mean3 = float(raw_input("enter y_mean for the third component: "))
			x_var3  = float(raw_input("enter x_var for the third component: "))
			y_var3  = float(raw_input("enter y_var for the third component: "))
			c = gausian0.gaus_std(x_mean3, y_mean3, x_var3, y_var3)

			g = gausian0.gaus_mix(3,a,b,c)
			print
			print g
		elif answer == 'e':
			break
		else:
			print "please enter valid input!"