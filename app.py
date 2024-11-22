from flask import Flask, request, render_template
import pickle
import pandas as pd

# Load the trained model
model_path = 'lightgbm_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Feature names used during training
feature_names = [
    'CustomerID', 'Age', 'CityTier', 'DurationOfPitch', 'Gender', 'NumberOfPersonVisiting',
    'NumberOfFollowups', 'PreferredPropertyStar', 'NumberOfTrips', 'Passport',
    'PitchSatisfactionScore', 'OwnCar', 'NumberOfChildrenVisiting', 'MonthlyIncome',
    'TypeofContact_Self Enquiry', 'Occupation_Large Business', 'Occupation_Salaried',
    'Occupation_Small Business', 'ProductPitched_Deluxe', 'ProductPitched_King',
    'ProductPitched_Standard', 'ProductPitched_Super Deluxe', 'MaritalStatus_Married',
    'MaritalStatus_Unmarried', 'Designation_Executive', 'Designation_Manager',
    'Designation_Senior Manager', 'Designation_VP'
]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data
        form_data = request.form.to_dict()

        # Map dropdown values to binary/one-hot encoded features
        categorical_mappings = {
            'Occupation': {
                'Large Business': [1, 0, 0],
                'Salaried': [0, 1, 0],
                'Small Business': [0, 0, 1]
            },
            'ProductPitched': {
                'Deluxe': [1, 0, 0, 0],
                'King': [0, 1, 0, 0],
                'Standard': [0, 0, 1, 0],
                'Super Deluxe': [0, 0, 0, 1]
            },
            'MaritalStatus': {
                'Married': [1, 0],
                'Unmarried': [0, 1]
            },
            'Designation': {
                'Executive': [1, 0, 0, 0],
                'Manager': [0, 1, 0, 0],
                'Senior Manager': [0, 0, 1, 0],
                'VP': [0, 0, 0, 1]
            }
        }

        # Initialize input data
        input_data = []

        # Numeric features
        numeric_features = [
            'CustomerID', 'Age', 'CityTier', 'DurationOfPitch', 'Gender',
            'NumberOfPersonVisiting', 'NumberOfFollowups', 'PreferredPropertyStar',
            'NumberOfTrips', 'Passport', 'PitchSatisfactionScore', 'OwnCar',
            'NumberOfChildrenVisiting', 'MonthlyIncome','TypeofContact_Self Enquiry'
        ]
        for feature in numeric_features:
            input_data.append(float(form_data.get(feature, 0)))

        # Categorical features
        for category, mapping in categorical_mappings.items():
            input_data.extend(mapping[form_data[category]])

        # Convert input to DataFrame
        input_df = pd.DataFrame([input_data], columns=feature_names)

        # Make prediction
        prediction = model.predict(input_df)[0]
        output = 'Will Purchase' if prediction == 1 else 'Not Purchase'

        return render_template('index.html', prediction_text=f'Prediction: {output}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
