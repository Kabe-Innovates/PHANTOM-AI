import joblib
import pandas as pd
from model_utils import predictor_model, generate_synthetic_attack_data
import numpy as np

# Generate synthetic attack data
attack_data = generate_synthetic_attack_data(500)

# Prepare the data for the prediction model
X_pred = np.random.rand(500, 23)  # 500 samples, 23 features (adjust as needed)
y_pred = attack_data["attack_count"].values

# Ensure input data shape is correct
print("Shape of X_pred:", X_pred.shape)  # Should print (500, 23)

# Train the attack prediction model
predictor_model.fit(X_pred, y_pred, epochs=10, batch_size=32)

# Save the trained model as .h5
predictor_model.save("ai_model/predictor_model.h5")
print("Attack predictor model trained & saved successfully.")
