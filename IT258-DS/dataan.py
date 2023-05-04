import os
import cv2
from skimage.feature import hog

# Define HOG parameters
orientations = 9
pixels_per_cell = (8, 8)
cells_per_block = (3, 3)
visualize = False
transform_sqrt = False
feature_vector = True

# Define directory containing images
directory = 'PlantVillage\Potato___healthy'

# Loop over all images in directory
for filename in os.listdir(directory):
    if filename.endswith('.JPG'):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            print(f"Processing {filename}...")
            # Load image
            img = cv2.imread(file_path)

            # Convert image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Extract HOG features
            features = hog(gray, orientations=orientations,
                           pixels_per_cell=pixels_per_cell,
                           cells_per_block=cells_per_block,
                           visualize=visualize,
                           transform_sqrt=transform_sqrt,
                           feature_vector=feature_vector)

            # Do something with the feature vector (e.g., save it to a file or use it for classification)
            print(features)
        else:
            print(f"{filename} is not a file.")
