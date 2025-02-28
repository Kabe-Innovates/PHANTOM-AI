from model_utils import generate_synthetic_text_data, generate_synthetic_time_series, generate_synthetic_attacker_profiles

X_train, X_test, y_train, y_test = generate_synthetic_text_data()
X_train.to_csv("synthetic_text_train.csv", index=False)
X_test.to_csv("synthetic_text_test.csv", index=False)

time_series_data = generate_synthetic_time_series()
time_series_data.to_csv("synthetic_time_series.csv", index=False)

attacker_profiles = generate_synthetic_attacker_profiles()
attacker_profiles.to_csv("synthetic_attacker_profiles.csv", index=False)

print("Synthetic data saved!")
