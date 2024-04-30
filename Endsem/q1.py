
import numpy as np
from matplotlib import pyplot as plt


def linear_regression(x_values, y_values, errors):
    slope = 0.0
    intercept = 0.0
    chi_square = 0.0
    num_points = len(y_values)
    num_features = len(x_values)
    total_weight = 0.0
    sum_x_weighted = 0.0
    sum_y_weighted = 0.0
    sum_x_squared_weighted = 0.0
    sum_xy_weighted = 0.0
    predicted_y = [0 for _ in range(num_points)]
    
    for i in range(num_features):
        predicted_y[i] = slope * intercept * x_values[i]
        chi_square += ((y_values[i] - predicted_y[i]) / errors[i])**2
        total_weight += 1 / errors[i]**2
        sum_x_weighted += x_values[i] / errors[i]**2
        sum_y_weighted += y_values[i] / errors[i]**2
        sum_x_squared_weighted += (x_values[i] / errors[i])**2
        sum_xy_weighted += x_values[i] * y_values[i] / errors[i]**2
    
    delta = total_weight * sum_x_squared_weighted - (sum_x_weighted)**2
    slope = (sum_x_squared_weighted * sum_y_weighted - sum_x_weighted * sum_xy_weighted) / delta
    intercept = (total_weight * sum_xy_weighted - sum_x_weighted * sum_y_weighted) / delta
    cov_slope_intercept = -sum_x_weighted / delta
    error_slope = np.sqrt(sum_x_squared_weighted / delta)
    error_intercept = np.sqrt(total_weight / delta)
    
    return slope, intercept, cov_slope_intercept, error_slope, error_intercept

def read_matrix(name): #combined matrix reading 
    with open(name,'r') as f:
        l = [[float(num) for num in line.split('	')] for line in f]
    ques=[]
    for i in range(len(l)):
        ques.append(l[i])
    return ques
A=read_matrix("endsemfit.txt")
A=np.array(A)
x,y,sigma= A[:, 0],A[:, 1],A[:, 2]
slope, intercept, cov_slope_intercept, error_slope, error_intercept = linear_regression(x, y, sigma)
slope, intercept, cov_slope_intercept, error_slope, error_intercept = linear_regression(x, y, sigma)
print("Slope:", slope)
print("Intercept:", intercept)
print("Covariance of Slope and Intercept:", cov_slope_intercept)
print("Error in Slope:", error_slope)
print("Error in Intercept:", error_intercept)


#plotting
x = [1,15,30,45,60,75,90,105,120,135]
y=[106,80,98,75,74,73,49,38,37,32]
c = [10,9,10,9,8,8,7,6,6,5]

plt.plot(x,y)



#Output
'''
Slope: 104.93548814956169
Intercept: -0.5961406559094794
Covariance of Slope and Intercept: -0.2570612823004929
Error in Slope: 5.244973800007545
Error in Intercept: 0.0544371685494538
'''