import joblib
import pandas as pd
from model_utils import profiler_model, generate_synthetic_attacker_profiles
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Generate synthetic attacker profiling data
attacker_profiles = generate_synthetic_attacker_profiles(500)

# Prepare the data for the profiling model
X_profiler = np.random.rand(500, 23)  # 500 samples, 23 features (adjust as needed)
y_profiler = LabelEncoder().fit_transform(attacker_profiles["attacker"])

# Ensure input data shape is correct
print("Shape of X_profiler:", X_profiler.shape)  # Should print (500, 23)

# Train the attacker profiling model
profiler_model.fit(X_profiler, y_profiler, epochs=10, batch_size=32)

# Save the trained model as .h5
profiler_model.save("ai_model/profiler_model.h5")
print("Attacker profiling model trained & saved successfully.")
