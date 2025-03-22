import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.under_sampling import RandomUnderSampler
import joblib

# Load preprocessed data
df = pd.read_csv("data/processed_data.csv")

# Separate features and target
X = df.drop(columns=["Is_Phishing"])
y = df["Is_Phishing"]

# Balance dataset using under-sampling (to avoid overfitting phishing features)
rus = RandomUnderSampler(random_state=42)
X_resampled, y_resampled = rus.fit_resample(X, y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=300, max_depth=20, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("✅ Model Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "models/phishing_model.pkl")
print("✅ Model saved as 'model/phishing_model.pkl'")
