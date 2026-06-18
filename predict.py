import joblib

model = joblib.load("crop_model.pkl")

sample = [[90, 42, 43, 20.8, 82.0, 6.5, 202.9]]

prediction = model.predict(sample)

print("Recommended Crop:", prediction[0])