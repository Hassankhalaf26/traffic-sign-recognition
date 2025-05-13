import numpy as np
from PIL import Image
import os
from sklearn.preprocessing import StandardScaler

def load_data(project_dir, classes=43, image_size=(20, 20), max_images_per_class=5000):
    data = []
    labels = []

    train_dir = os.path.join(project_dir, 'Train')

    for i in range(classes):
        path = os.path.join(train_dir, str(i))
        if os.path.exists(path):
            images = os.listdir(path)[:max_images_per_class]  # Limit the number of images
            for a in images:
                try:
                    image_path = os.path.join(path, a)
                    image = Image.open(image_path)
                    image = image.resize(image_size)
                    image = np.array(image)
                    image = image.flatten()
                    data.append(image)
                    labels.append(i)
                except Exception as e:
                    print(f"Error loading image {a}: {e}")
        else:
            print(f"Directory '{path}' not found.")
    
    data = np.array(data)
    labels = np.array(labels)

    # Normalize
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    
    return data, labels, scaler
