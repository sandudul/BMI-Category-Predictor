import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv('dataset/500_Person_Gender_Height_Weight_Index.csv')

# Step 1: Encode Gender column
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])  # Male=1, Female=0 (or vice versa)

# Step 2: Define features (X) and target (y)
X = df[['Gender', 'Height', 'Weight']]
y = df['Index']

# Step 3: Handle missing values if any
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# Step 4: Split dataset (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Initialize and train Random Forest model
model = RandomForestClassifier(max_depth=5, n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Predict on test set and calculate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Step 7: Save the model and label encoder for later use
joblib.dump(model, 'bmi_model.pkl')
joblib.dump(le, 'label_encoder.pkl')
print("Model and Label Encoder saved!")
