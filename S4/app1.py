import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import base64

# Set Page Config
st.set_page_config(page_title="Diabetic Retinopathy Detection", page_icon="👁️", layout="wide")

# Function to set background image
def set_bg_image(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set Background (Replace '123.png' with your background image)
set_bg_image("123.png")

# Custom CSS for Styling
st.markdown(
    """
    <style>
    .title-container {
        text-align: center;
        position: relative;
        width: 100%;
        padding: 15px;
        background: rgba(0, 0, 0, 0.5);
        border-radius: 10px;
        display: inline-block;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin: 0;
    }
    .subtext-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin-top: 10px;
    }
    .subtext-container {
        text-align: center;
        width: 40%;
        height: 50px;
        padding: 15px;
        background: rgba(0, 0, 0, 0.5);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .subtext {
        color: #eeeeee;
        font-size: 18px;
        margin: 0;
    }
    .uploaded-image-container {
        display: flex;
        justify-content: center;
        align-item: center;
        margin-top: 20px;
    }
    .uploaded-image {
        border-radius: 15px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.5);
    }
    .result {
        font-size: 25px;
        font-weight: bold;
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        background-color: #ffffff;
        color: #333333;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Header
st.markdown('<div class="title-container"><p class="title">👁️ Diabetic Retinopathy Detection</p></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="subtext-wrapper">
        <div class="subtext-container">
            <p class="subtext">Upload an eye image to check for diabetic retinopathy.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Load the trained model with error handling
try:
    model = tf.keras.models.load_model("diabetic_retinopathy_model.keras")
    st.success("✅ Model Loaded Successfully")
except Exception as e:
    st.error(f"❌ Model loading failed: {e}")
    st.stop()

# Define class labels
class_labels = {0: "Diabetic Retinopathy", 1: "No Diabetic Retinopathy"}

# File uploader
uploaded_file = st.file_uploader("📂 Choose an eye image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    try:
        # Load and preprocess the image
        img = Image.open(uploaded_file).convert("RGB")
        img = img.resize((100, 100))  # Resize to match model input shape

        # Display uploaded image in center
        st.markdown('<div class="uploaded-image-container">', unsafe_allow_html=True)
        st.image(img, caption="🖼️ Uploaded Image", use_column_width=False, width=250, output_format="PNG")
        st.markdown('</div>', unsafe_allow_html=True)

        # Convert image to array
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = img_array / 255.0  # Normalize

        # Model prediction
        prediction = model.predict(img_array)

        # Handling binary classification
        result = class_labels[int(prediction[0][0] > 0.5)]

        # Display result
        st.markdown(f'<p class="result">🔍 Prediction: {result}</p>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error processing image: {e}")

# Debugging
st.write("ℹ️ Debug: Script is running fine.")
