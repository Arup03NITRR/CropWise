import os
import numpy as np
import streamlit as st
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

##### Page Configuration #####
st.set_page_config(
    page_title="CropWise - Smart Soil Analyzer",
    page_icon="🌱",  # Emoji or path to .ico/.png file
    layout="centered",  # 'centered' or 'wide'
    initial_sidebar_state="auto",  # 'auto', 'expanded', 'collapsed'
)

##### Constants #####
IMG_WIDTH = 150
IMG_HEIGHT = 150
soil_crops = {
    'Black Soil': ['Cotton', 'Soybean', 'Sunflower', 'Millets', 'Sorghum'],
    'Cinder Soil': ['Tobacco', 'Groundnut', 'Cotton'],  
    'Laterite Soil': ['Tea', 'Coffee', 'Cashew', 'Coconut', 'Rubber'],
    'Peat Soil': ['Paddy (Rice)', 'Jute', 'Sugarcane'],  
    'Yellow Soil': ['Pulses', 'Oilseeds', 'Potato', 'Maize']
}
class_names = list(os.listdir("./Soil types"))

##### Loading Model #####
cnn = load_model("cnn.keras")

##### Functions #####
def predict(soil):
    soil_array = np.array(soil)
    # Normalization
    soil_array = soil_array/255.0
    soil_array = np.expand_dims(soil_array, axis=0)
    prediction = cnn.predict(soil_array)
    predicted_class_index = np.argmax(prediction)
    return predicted_class_index

def get_class(class_index):
    raw_label = class_names[class_index]
    formatted_label = raw_label.replace('_', ' ').strip().title()
    #Check if the image is from soil mapping
    is_soil_mapping = False
    for soil_type in soil_crops.keys():
        if soil_type.lower() in formatted_label.lower():
            is_soil_mapping = True
            return formatted_label
    if not is_soil_mapping:
        # print("Warning: This image does not appear to be from soil mapping. Please upload an image of soil.")
        return None



st.title("🌾 CropWise 🚜")
st.subheader("🌱 Know Your Soil, Grow the Right Crop.🌱")

st.markdown("<br>", unsafe_allow_html=True)
soil = st.file_uploader("📷 Upload the image of the soil", type=["jpg", "jpeg", "png", "webp"])

if soil:
    soil = Image.open(soil).convert("RGB")
    soil = soil.resize((IMG_WIDTH, IMG_HEIGHT))
    st.image(soil, caption="Uploaded Image")
    predict_btn = st.button("Predict 🔍")
    st.write("<br>", unsafe_allow_html=True)
    if predict_btn:
        predicted_class_index = predict(soil)
        result = get_class(predicted_class_index)
        if result:
            st.write("<h5>Predicted Soil Type:</h5>", unsafe_allow_html=True)
            st.write(f"<h3><span style='color: green;'> {result}</span></h3>", unsafe_allow_html=True)
            with st.expander("🌿 Crops can grow"):
                st.write("<ul>", unsafe_allow_html=True)
                for crop in soil_crops[result]:
                    st.write(f"<li> {crop} </li>", unsafe_allow_html=True)
                st.write("</ul>", unsafe_allow_html=True)
        else:
            st.warning("Warning: This image does not appear to be from soil mapping. Please upload an image of soil.")
