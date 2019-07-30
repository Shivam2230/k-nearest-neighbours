
import numpy as np
import math 

def pointClassifier(points,p,k=3):
    distance=[] 
    for group in points:
        for feature in points[group]:
            euclidean_distance = math.sqrt((feature[0]-p[0])**2 +(feature[1]-p[1])**2) 
            distance.append((euclidean_distance,group)) 

    # sort the distance list in ascending order and select first k distances 
    distance = np.array(sorted(distance)[:k+1]) 
    freq1 = 0  
    freq2 = 0 
    mat=distance[:,-1]
    freq1=np.count_nonzero(mat==0)
    freq2=np.count_nonzero(mat==1)
    return 0 if freq1>freq2 else 1



points = {0:[(1,12),(2,5),(3,6),(3,10),(3.5,8),(2,11),(2,9),(1,7)], 
                1:[(5,3),(3,2),(1.5,9),(7,2),(6,1),(3.8,1),(5.6,4),(4,2),(2,5)]} 

# testing point p(x,y) 
p = (2.5,7) 

# Number of neighbours 
k = 2

print("The value classified to unknown point is: {}".format(pointClassifier(points,p,k))) 

