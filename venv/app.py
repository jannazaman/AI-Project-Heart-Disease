from flask import Flask, render_template, send_from_directory, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the model
app_dir = os.path.abspath(os.path.dirname(__file__))
mlp_model_path = os.path.join(app_dir, 'templates', 'mlp_predict.pkl')
mlp_ = joblib.load(mlp_model_path)

# List of input features and a dictionary of constant features for rendering the form
input_features = ['Age', 'Sex', 'CP', 'fbs', 'trestbps', 'Chol', 'exang']
constant_features = {'restecg': 0, 'thalach': 150, 'oldpeak': 0, 'slope': 1, 'ca': 0, 'thal': 3}


# Define routes
@app.route('/')
def home():
    return render_template('index.html', input_features=input_features, constant_features=constant_features)


@app.route('/mlp_model')
def mlp_model():
    return render_template('mlp_model.html')


@app.route('/svm_model')
def svm_model():
    return render_template('svm_model.html')


# Send files from 'templates' directory
@app.route('/templates/<path:filename>')
def serve_static(filename):
    return send_from_directory('templates', filename)


# Handles form submission, extracts data, makes predictions, and displays the result.
@app.route('/Predict_disease', methods=['POST'])
def Predict_disease():
    try:
        # Extract data from the form
        user_input = [float(request.form[feature]) if feature in input_features else constant_features[feature] for
                      feature in input_features + list(constant_features.keys())]

        # Make predictions using the loaded model
        prediction = mlp_.predict([user_input])

        # Display the prediction
        result = "Likelihood of Heart Disease: {}".format("Positive" if prediction[0] == 1 else "Negative")

        # Pass the result back to the form for display
        return render_template('Predict_disease.html', result=result, input_features=input_features,
                               constant_features=constant_features)

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        # Pass the error message back to the form for display
        return render_template('Predict_disease.html', result=error_message, input_features=input_features,
                               constant_features=constant_features)


# Renders the form page for initial display
@app.route('/Predict_disease', methods=['GET'])
def show_prediction_form():
    return render_template('Predict_disease.html', input_features=input_features, constant_features=constant_features)


if __name__ == '__main__':
    app.run(debug=True)
