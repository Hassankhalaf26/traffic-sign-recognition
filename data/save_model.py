import joblib
import os 
def save_model(svm_model, scaler, project_dir):
    # Save the trained model using joblib
    model_path = os.path.join(project_dir, 'svm_model.joblib')
    joblib.dump(svm_model, model_path)
    print(f"Model saved at {model_path}")

    # Save the scaler
    scaler_path = os.path.join(project_dir, 'scaler.joblib')
    joblib.dump(scaler, scaler_path)
    print(f"Scaler saved at {scaler_path}")
