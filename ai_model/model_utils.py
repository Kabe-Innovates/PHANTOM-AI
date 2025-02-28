import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

# Function to generate synthetic text data
def generate_synthetic_text_data(num_samples=1000):
    threats = ["DDoS", "Ransomware", "Phishing", "APT", "Botnet"]
    attack_methods = ["Exploit CVE-2024-1234", "SQL Injection", "Malware Delivery"]
    attack_vectors = ["Email Phishing", "Brute Force", "Zero-Day Exploit"]
    
    data = []
    for _ in range(num_samples):
        text = f"A new {random.choice(threats)} attack detected, using {random.choice(attack_methods)} via {random.choice(attack_vectors)}."
        label = random.choice(threats)
        data.append([text, label])

    return pd.DataFrame(data, columns=["text", "label"])

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Generate synthetic data
synthetic_data = generate_synthetic_text_data(1000)

# Vectorize the text data
X = vectorizer.fit_transform(synthetic_data["text"]).toarray()
y = synthetic_data["label"]

# Encode labels as integers
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Create a simple Keras model (classifier)
classifier_model = Sequential([
    Dense(128, input_dim=X.shape[1], activation='relu'),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(len(set(y)), activation='softmax')  # Output layer with one neuron for each class
])

classifier_model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

# Train the classifier model
classifier_model.fit(X, y, epochs=10, batch_size=32)

# Save the trained model as .h5
classifier_model.save("ai_model/classifier_model.h5")
print("Classifier model trained & saved as classifier_model.h5 successfully.")

# Function to generate synthetic attack prediction data
def generate_synthetic_attack_data(num_samples=500):
    dates = pd.date_range(start="2024-01-01", periods=num_samples, freq="D")
    attack_counts = np.random.randint(1, 50, size=num_samples)
    
    return pd.DataFrame({"date": dates, "attack_count": attack_counts})

# Generate synthetic time-series attack data
attack_data = generate_synthetic_attack_data(500)

# Prepare the data for prediction model (simple regression)
X_pred = np.arange(len(attack_data)).reshape(-1, 1)  # Date indices as features
y_pred = attack_data["attack_count"].values

# Create a Keras model for attack prediction (regression)
predictor_model = Sequential([
    Dense(64, input_dim=1, activation='relu'),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(1)
])

predictor_model.compile(loss='mean_squared_error', optimizer=Adam(), metrics=['mean_squared_error'])

# Train the attack predictor model
predictor_model.fit(X_pred, y_pred, epochs=10, batch_size=32)

# Save the predictor model
predictor_model.save("ai_model/predictor_model.h5")
print("Predictor model trained & saved as predictor_model.h5 successfully.")

# Function to generate synthetic attacker profiling data
def generate_synthetic_attacker_profiles(num_samples=500):
    attackers = ["APT-28", "APT-29", "Lazarus Group", "Fancy Bear", "DarkSide"]
    techniques = ["Phishing", "Zero-Day Exploit", "DDoS", "Privilege Escalation"]
    targets = ["Government", "Financial Institutions", "Healthcare", "IoT Devices"]
    
    data = []
    for _ in range(num_samples):
        data.append([random.choice(attackers), random.choice(techniques), random.choice(targets)])
    
    return pd.DataFrame(data, columns=["attacker", "techniques", "target"])

# Generate synthetic attacker profiling data
attacker_profiles = generate_synthetic_attacker_profiles(500)

# Prepare the data for profiling model
X_profiler = pd.get_dummies(attacker_profiles[["techniques", "target"]]).values
y_profiler = LabelEncoder().fit_transform(attacker_profiles["attacker"])

# Create a Keras model for attacker profiling (classification)
profiler_model = Sequential([
    Dense(128, input_dim=X_profiler.shape[1], activation='relu'),
    Dropout(0.2),
    Dense(64, activation='relu'),
    Dense(len(set(y_profiler)), activation='softmax')  # Output layer with one neuron for each attacker class
])

profiler_model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

# Train the attacker profiling model
profiler_model.fit(X_profiler, y_profiler, epochs=10, batch_size=32)

# Save the profiler model
profiler_model.save("ai_model/profiler_model.h5")
print("Profiler model trained & saved as profiler_model.h5 successfully.")
