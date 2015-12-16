import numpy as nu
import math


class NormDistVal(object):
    """
    A class for 2-d data generation with normally distributed values
    """

    def __init__(self, x_mean, y_mean, x_var, y_var):
        self.x_mean = x_mean
        self.y_mean = y_mean
        self.x_var = x_var
        self.y_var = y_var
        self.x_dev = math.sqrt(x_var)
        self.y_dev = math.sqrt(y_var)

    def __str__(self):
        return "x mean: " + str(self.x_m) + "\ny mean: " + str(self.y_m) + "\nx variance: " + str(
            self.x_v) + "\ny variance: " + str(self.y_v) + "\nx standard deviation: " + str(
            self.x_dev) + "\ny stadard deviation: " + str(self.y_dev)

    def calc_norm_dist_val(self, amount_points):
        x = nu.random.normal(self.x_mean, self.x_dev, amount_points)
        y = nu.random.normal(self.y_mean, self.y_dev, amount_points)
        points_list = []
        for i in range(0, amount_points):
            points_list.append([x[i],y[i]])
        return points_list



