from threat_classifier import clf
import numpy as np

# Training data for classification
X_train = np.array([[3, 2, 1], [5, 8, 5], [2, 1, 1], [8, 10, 7], [6, 5, 3], [7, 15, 8], [6, 6, 4]])
y_train = np.array([0, 1, 2, 1, 3, 4, 1])

def train():
    clf.fit(X_train, y_train)
    print("Model trained successfully!")

if __name__ == "__main__":
    train()
