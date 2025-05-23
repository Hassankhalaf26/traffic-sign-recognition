from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

def train_svm_model(data, labels):
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42,stratify=labels)
    model = SVC(kernel='rbf')  
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("SVM training complete.")
    return model, X_test, y_test, y_pred
