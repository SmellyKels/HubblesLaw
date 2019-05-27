# Hubbles Law

My reference material comes from zoninations analysis of the age of the universe following the same approach.  
Here is their github repository: https://github.com/zonination/galaxies

I am merely following a slightly different approach to the same project. Instead of using R, I used python.  
Instead of calculating the age of the universe, I simply look at the slope data to determine Hubble's Constant.

However I used the same data set that zonination provided, which is here:http://leda.univ-lyon1.fr/leda/fullsql.html.  
Of course I used the same SQL query: SELECT objname, mod0, vgsr WHERE mod0 IS NOT NULL

I was concerned about the exclusion of outliers, and also the removal of the y-intercepts in the regression lines.    
As my first project in python, I have difficulty grasping the concept of outliers. 
It seemed like when to exclude outliers and how to exclude it depended on the analyst and the data set they were looking at.  
Being a newbie to the field of data science, I asked a friend what criteria to use to determine outliers.  
He suggested that I use standard deviations and averages. If a data point was above or below standard deviation, omit it.  
The practice of excluding intercepts also confused me. 
It seems like the practice is common, but determing when to do it or why I should do it is difficult.  

The resulting data set turns out to have 3915 data points, close to the 3908 data points in zoninations repository.  

The comparison shows that without removing outliers, the Hubble constant is 63.0.  
This is not in agreement with the latest measurement of 68.0 +4.2, −4.1.  
However when removing the outliers, the Hubble constant is 65.4.  
This agrees with the latest measurement.  



![alt text](https://github.com/SmellyKels/HubblesLaw/blob/master/Figure_1.png)
![alt text](https://github.com/SmellyKels/HubblesLaw/blob/master/Figure_2.png)
