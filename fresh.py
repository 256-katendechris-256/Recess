import streamlit as st
import numpy as np
import pickle
import librosa
import tensorflow as tf

# Load the trained model
model_path = "bird_species_model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

st.title("Bird Species Classification")

# Upload audio file
uploaded_file = st.file_uploader("Choose an audio file", type=["wav"])

if uploaded_file is not None:
    # Load and preprocess the uploaded audio
    audio, _ = librosa.load(uploaded_file, sr=22050)
    mfcc = librosa.feature.mfcc(y=audio, sr=22050, n_mfcc=13, n_fft=2048, hop_length=512)
    mfcc = mfcc.T[np.newaxis, ..., np.newaxis]  # Expand dimensions to match model input shape

    # Make a prediction
    prediction = model.predict(mfcc)
    predicted_label = np.argmax(prediction)

    # Display the prediction
    st.write("Predicted Bird Species:")
    st.write(predicted_label)  # You can replace this with your actual class labels

