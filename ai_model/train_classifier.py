import joblib
import pandas as pd
from model_utils import classifier_model, generate_synthetic_attack_data
import numpy as np

# Generate synthetic attack data
attack_data = generate_synthetic_attack_data(500)

# Prepare the data for the classifier model (shape should be (500, 23))
X = np.random.rand(500, 23)  # 500 samples, 23 features (adjust as needed)
y = attack_data["classification"].values  # Assuming classification is part of the data

# Ensure input data shape is correct
print("Shape of X:", X.shape)  # Should print (500, 23)

# Train the attack classifier model
classifier_model.fit(X, y, epochs=10, batch_size=32)

# Save the trained model as .h5
classifier_model.save("ai_model/classifier_model.h5")
print("Classifier model trained & saved successfully.")
