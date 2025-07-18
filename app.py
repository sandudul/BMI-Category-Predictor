from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the model and label encoder (make sure these files are in the same folder as app.py)
model = joblib.load('bmi_model.pkl')
le = joblib.load('label_encoder.pkl')

# BMI category mapping
bmi_categories = {
    0: "Extremely Weak",
    1: "Weak",
    2: "Normal",
    3: "Overweight",
    4: "Obese",
    5: "Extremely Obese"
}

@app.route('/')
def home():
    return render_template('index.html')  # Renders your frontend page

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    gender = request.form['gender']           # e.g., "Male" or "Female"
    height = float(request.form['height'])    # e.g., 170.5
    weight = float(request.form['weight'])    # e.g., 65.3

    # Encode gender to numeric using the saved LabelEncoder
    gender_encoded = le.transform([gender])[0]

    # Prepare input for prediction
    input_data = np.array([[gender_encoded, height, weight]])

    # Predict BMI category index
    prediction = model.predict(input_data)[0]

    # Map index to category name
    category = bmi_categories.get(prediction, "Unknown")

    # Render the same page with prediction result
    return render_template('index.html', prediction_text=f'Predicted BMI Category: {category}')

if __name__ == '__main__':
    app.run(debug=True)
