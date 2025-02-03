from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd  # Import pandas

# Initialize Flask App
app = Flask(__name__)

# Load the trained model and preprocessing pipeline
with open('flight_price_pipeline.pkl', 'rb') as f:
    model_pipeline = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')  # Render the main page with the form

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collecting input data from form with correct column names
        input_data = {
            'Airline': [request.form['airline']],
            'Source_City': [request.form['source']],
            'Departure_Time': [request.form['departure']],
            'Stops': [request.form['stops']],
            'Arrival_Time': [request.form['arrival']],
            'Destination_City': [request.form['destination']],
            'Class': [request.form['class']],
            'Duration': [float(request.form['duration'])],
            'Days_Left': [int(request.form['days_left'])]
        }

        # Convert to DataFrame
        input_df = pd.DataFrame(input_data)

        print(f"Input DataFrame:\n{input_df}")  # Debugging line

        # Predict using the saved pipeline
        predicted_price = model_pipeline.predict(input_df)[0]

        return render_template('index.html', 
                               prediction_text=f'Estimated Flight Price: ₹{predicted_price:,.2f}',
                               duration=request.form['duration'],
                               days_left=request.form['days_left'])

    except Exception as e:
        return render_template('index.html', 
                              prediction_text=f"Error: {str(e)}",
                              duration=request.form.get('duration', ''),
                              days_left=request.form.get('days_left', ''))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
