#This script analyses Hyperleda galaxy data in order to determine the Hubble Constant.
#It compares two sets of data, one with outliers, one without outliers.

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression as lgr

x,y = list(np.loadtxt('hyperleda base data.txt', 
           unpack=True,delimiter=','))
x = 10*(10**(x/5))/(10**6)
x_filtered = []
y_filtered = []

x_avg = np.average(x)
x_std = np.std(x)
y_avg = np.average(y)
y_std = np.std(y)

i = 0
while i < len(x) - 1:
    if (x[i] <= x_avg + x_std 
        and x[i] >= x_avg - x_std 
        and y[i] <= y_avg + y_std 
        and y[i] >= y_avg - y_std):
            x_filtered.append(x[i])
            y_filtered.append(y[i])
    i+=1

model = lgr().fit(np.array(x).reshape(-1, 1), y)
y_pred = model.coef_ * x + model.intercept_
model_filtered = lgr().fit(np.array(x_filtered).reshape(-1, 1), y_filtered)
y_predfiltered = model_filtered.coef_ * x_filtered + model_filtered.intercept_

plt.style.use("dark_background")
plt.figure(figsize = (20,20))
plt.scatter(x, y, c = x, cmap = 'rainbow_r', s=1)
plt.plot(x, y_pred)
plt.suptitle("Recession Data of Galaxies", 
              fontsize = 25, y = .95)
plt.xlabel('Distance from Earth in Megaparsecs',fontsize = 20)
plt.ylabel('Radial velocity with respect to galactic center in km/s',
            fontsize = 20)
plt.text(500, 500, 
         'y={:.2f}x+{:.2f}'.format(float(model.coef_), model.intercept_), 
         fontsize = 20)

plt.style.use("dark_background")
plt.figure(figsize = (20,20))
plt.scatter(x_filtered,y_filtered, c = x_filtered, cmap = 'rainbow', s=1)
plt.plot(x_filtered, y_predfiltered)
plt.suptitle("Recession Data of Galaxies: Outliers removed", 
              fontsize = 25, y = .95)
plt.xlabel('Distance from Earth in Megaparsecs',fontsize = 20)
plt.ylabel('Radial velocity with respect to galactic center in km/s',
            fontsize = 20)
plt.text(50, 500, 
         'y={:.2f}x+{:.2f}'.format(float(model_filtered.coef_), model_filtered.intercept_), 
         fontsize = 20)

plt.show()