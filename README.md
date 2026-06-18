# 🌱 Crop Recommendation System using Machine Learning

## 📌 Overview

The Crop Recommendation System is a machine learning-based application that recommends the most suitable crop to cultivate based on soil nutrients and environmental conditions.

The model analyzes agricultural parameters such as Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH level, and rainfall to predict the optimal crop for farming. This project helps support data-driven agricultural decision-making and can assist farmers in improving productivity and crop selection.

---

## 🚀 Features

* Predicts suitable crops based on soil and weather conditions
* Performs data preprocessing and feature analysis
* Uses Machine Learning for accurate crop prediction
* Interactive web application built with Streamlit
* Visualization of agricultural data using charts and heatmaps
* Easy-to-use user interface

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit

---

## 📊 Dataset

The dataset contains agricultural and environmental parameters:

| Feature     | Description                |
| ----------- | -------------------------- |
| N           | Nitrogen content in soil   |
| P           | Phosphorus content in soil |
| K           | Potassium content in soil  |
| Temperature | Temperature in Celsius     |
| Humidity    | Relative humidity (%)      |
| pH          | Soil pH value              |
| Rainfall    | Rainfall in mm             |
| Label       | Recommended crop           |

---

## ⚙️ Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Train-Test Split
6. Model Training using Random Forest Classifier
7. Model Evaluation
8. Model Deployment using Streamlit

---

## 📈 Model Performance

The Random Forest Classifier achieved high prediction accuracy on the crop recommendation dataset.

Evaluation Metrics:

* Accuracy Score
* Classification Report
* Confusion Matrix

---

## 📂 Project Structure

```text
Crop-Recommendation-System/
│
├── Crop_recommendation.csv
├── train_model.py
├── visualize.py
├── app.py
├── crop_model.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/srinivassannegandla-commits/crop-prediction-.git
cd Crop-Recommendation-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

```bash
python train_model.py
```

This generates:

```text
crop_model.pkl
```

---

## ▶️ Run the Streamlit Application

```bash
py -m streamlit run app.py
```

Open the local URL displayed in the terminal to access the application.

---


## 🌍 Real-World Applications

* Smart Farming
* Precision Agriculture
* Crop Planning
* Agricultural Advisory Systems
* Data-Driven Decision Making

---

## 🔮 Future Enhancements

* Integration with live weather APIs
* Fertilizer recommendation system
* Crop yield prediction
* Disease detection module
* Cloud deployment using AWS or Azure

---

## 👨‍💻 Author

Developed as a Machine Learning project for agricultural analytics and crop recommendation using predictive modeling.

If you found this project useful, consider giving it a ⭐ on GitHub.
