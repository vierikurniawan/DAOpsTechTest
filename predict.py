import pickle
import pandas as pd

with open("wine_quality_rfc_model.pkl", "rb") as f:
    model = pickle.load(f)

feature_columns = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide',
    'density', 'pH', 'sulphates', 'alcohol'
]

feature_input = pd.DataFrame([[6.5, 0.3, 0.4, 2.0, 0.05,
                       35.0, 130.0, 0.994, 3.3, 0.9, 14.0]],
                            columns=feature_columns)

prediction = model.predict(feature_input)
print(f"Predicted wine quality: {prediction[0]}")
