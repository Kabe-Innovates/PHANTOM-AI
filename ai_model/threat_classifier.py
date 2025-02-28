from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Sample dataset for training
X_train = np.array([[3, 2, 1], [5, 8, 5], [2, 1, 1], [8, 10, 7], [6, 5, 3], [7, 15, 8], [6, 6, 4]])
y_train = np.array([0, 1, 2, 1, 3, 4, 1])  # 0: Script Kiddie, 1: APT, 2: Scammer, 3: Cybercriminal, 4: Hacktivist

clf = RandomForestClassifier(n_estimators=30, random_state=42)
clf.fit(X_train, y_train)

def classify_attacker(severity, frequency, tools_used):
    """Classifies attacker based on severity, frequency, and tools used."""
    pred = clf.predict(np.array([[severity, frequency, tools_used]]))[0]
    return pred
