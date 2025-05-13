import os
from data_preprocessing import load_data
from train_svm import train_svm_model
from evaluate_model import evaluate_model
from save_model import save_model

import time
start = time.time()
# Define the path to your project directory
project_dir = r'D:\collage\level 3 term 2\image processing\practical image\trafic sign\data'

# Load sample (e.g., only 5 classes and 20 images per class)
data, labels, scaler = load_data(project_dir, classes=43, image_size=(15, 15), max_images_per_class=1000)

# Train the SVM model
svm_model, X_test, y_test, y_pred = train_svm_model(data, labels)

# Evaluate the model
evaluate_model(y_test, y_pred)

# Save the trained model and scaler
save_model(svm_model, scaler, project_dir)


end = time.time()
print(f"Execution time: {end - start:.2f} seconds")

