# 🚦 AI-Based Traffic Sign Recognition System

This project provides a machine learning pipeline and web interface for detecting German traffic signs using an SVM model and Flask framework.

---

## 📚 Description

This system classifies traffic signs into 43 categories using a Support Vector Machine (SVM). A web interface allows users to upload an image and view the prediction in real-time.

---

## 📝 Features

* Data preprocessing and normalization
* Training using Scikit-learn's SVM
* Evaluation and confusion matrix visualization
* Flask web application for image uploads and predictions

---

## 📂 Project Structure

```
traffic-sign-recognition/
│
├── app.py                       # Flask app
├── templates/
│   └── index.html               # HTML frontend
├── static/
│   └── style.css                # CSS styling
|    
|    # Contains the dataset and saved models              
|── svm_model.joblib 
|── scaler.joblib
|
|── data_preprocessing.py
|── train_svm.py
├── evaluate_model.py
|── save_model.py
├── main.py                      # Main training and evaluation script
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

## 📂 Dataset
You can download the GTSRB (German Traffic Sign Benchmark) dataset from:
[Kaggle GTSRB Dataset](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)


### 1. Prepare Dataset

Download and extract the GTSRB dataset into:

```
data/Train/0, data/Train/1, ..., data/Train/42
```

### 4. Train the Model

```bash
python main.py
```

### 5. Run the Flask App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 🧬 Model Info

* Algorithm: SVM (linear kernel)
* Input: 15x15 RGB images (flattened)
* Classes: 43 traffic sign types
* Normalization: StandardScaler

---

## 📊 Evaluation

# Confusion Matrix

This is the confusion matrix for the traffic sign classification model:

![confusion matrix](data/confusion%20matrix.png)



---

## 🔧 Example Output

```json
{
  "prediction": "Speed limit (70km/h)"
}
```

---

## 🌐 Web Interface

Upload a traffic sign image (JPG/PNG). The app returns the predicted class in JSON.

---
![Speed limit (70km/h)](data/Speed%20limit%2070kmh.png)

##

---

## ✅ Future Improvements

* Add image augmentation
* Integrate confidence scores
* Deploy online using Render or HuggingFace Spaces
##
------

## team members 
* Hassan khalaf hassan   
* Siraj Al-Din Asim
* Girgis Imad Rizk
* Ahmed Saleh Mohammed
* Basil Amin Mohammed Ahmed
* Ahmed Nasser Arman

##


