# 🌾 CropWise

**Know your soil, Grow right crop.**

CropWise is a deep learning-based web application that allows users to upload an image of soil and receive instant predictions about the soil type and recommended crops that grow best in it. Built using Convolutional Neural Networks (CNNs) for image classification and Streamlit for a user-friendly frontend, CropWise empowers farmers, gardeners, and agricultural enthusiasts with smart soil insights.

---

## 🚀 Features

- 🖼️ Upload soil images for analysis
- 🔍 Predict soil type using a trained CNN model
- 🌱 Get crop recommendations tailored to the detected soil type
- 💻 Interactive, responsive web interface built with Streamlit
- 📊 Trained on a curated dataset of soil images
- ⚡ Fast and lightweight – runs locally with minimal setup

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend / Model:** Python, TensorFlow/Keras (CNN)
- **Environment Management:** `venv` (Virtual Environment)

---

## 🔧 Installation

Follow these steps to set up CropWise on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cropwise.git
cd cropwise
```
### 2. Create a Virtual Environment

```bash
python -m venv env
```
### 3.  Activate Virtual Environment
- On **Windows**
```bash
env\Scripts\activate
```
- On **macOs/Linux**
```bash
source venv/bin/activate
```
### 4. Install Dependencies

```bash
pip install -r requirements.txt
```
### 5. Run the Streamlit App

```bash
streamlit run app.py
```
## 💻 Output
<video width="640" height="360" controls>
  <source src="CropWise-Working.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>