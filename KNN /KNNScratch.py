
import numpy as np 
from collections import Counter

def euclidean_distance(x1,x2):
    distance = np.sqrt(np.sum(x1-x2))
    return distance

class KNN:
    def __init__(self, k =3):
        self.k = k

    def fit(self,X,y):
        self.X_train = X
        self.y_train = y

    def predict(self,X):
        predictions = [self._predict(x) for x in X]
        return predictions

    def _predict(self,x):
        # helper function that will predict a single data point value
        

        #compute the disctances
        distances = [euclidean_distance(x,x_train) for x_train in self.X_train]

      #get the closest k 
        k_indeces = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indeces]

        #majority vote
        most_common = Counter(k_nearest_labels).most_common()
        return most_common[0][0]
        