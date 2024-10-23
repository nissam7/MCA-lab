import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image

# Global size for resizing images
size = 100

# Try loading the model
try:
    model = load_model('./model/truesample.h5')  # Ensure this file contains the complete model (architecture + weights)
    st.success("Model loaded successfully.")
except Exception as e:
    st.error(f"Error loading model: {e}")

# Helper function to preprocess the uploaded image
def preprocess_image(image):
    # Convert PIL image to grayscale OpenCV format
    image = np.array(image.convert('L'))  # Convert to grayscale
    image = cv2.resize(image, (size, size))  # Resize to the model input size
    return image

# Streamlit interface
st.title("Pothole Detection System")

# Option for user to upload images
uploaded_files = st.file_uploader("Upload images for pothole detection", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

if uploaded_files:
    # Initialize lists for storing images and filenames
    images = []
    filenames = []

    # Process each uploaded file
    for uploaded_file in uploaded_files:
        # Open the uploaded file as a PIL image
        img = Image.open(uploaded_file)
        # Preprocess the image for model prediction (no need to show this)
        preprocessed_img = preprocess_image(img)
        images.append(preprocessed_img)
        filenames.append(uploaded_file.name)
    
    # Convert list of images to numpy array and reshape for the model
    X_test = np.array(images).reshape(len(images), size, size, 1)
    
    # Predict using the model
    try:
        predictions = model.predict(X_test)
        predicted_classes = np.argmax(predictions, axis=1)  # Get class with highest probability
        
        # Display results
        for i, pred in enumerate(predicted_classes):
            label = "Pothole Detected" if pred == 1 else "No Pothole Detected"
            st.write(f"Filename: {filenames[i]} - {label}")
            
            # Display only the original uploaded image with the detection label
            st.image(Image.open(uploaded_files[i]), caption=label, use_column_width=True)

    except Exception as e:
        st.error(f"Error during prediction: {e}")

else:
    st.write("Please upload images to run the detection.")
