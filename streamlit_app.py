import streamlit as st
import numpy as np
import cv2
from  PIL import Image, ImageEnhance

#Header
st.set_page_config(page_title="10119179-10116361")
st.header("Aplikasi Edit Gambar Online")
st.subheader("Upload Gambar dan Edit secara Real-Time!!!")

#Sidebar
st.sidebar.markdown('<p class="font">Aplikasi Edit Gambar</p>', unsafe_allow_html=True)
with st.sidebar.expander("Tentang Aplikasi"):
     st.write("""Aplikasi Simpel Mudah dan Cepat digunakan untuk mengedit gambar dalam format JPG,PNG dan JPEG yang memanfaatkan library openCV, Streamlit dan Numpy.\n10116361 Reka Saepul Anwar
     """)

#Upload Gambar
uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])

#Sebelum dan Sesudah
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns( [0.5, 0.5])
    with col1:
        st.markdown('<p style="text-align: center;">Sebelum</p>',unsafe_allow_html=True)
        st.image(image,width=300)  

    with col2:
        st.markdown('<p style="text-align: center;">Sesudah</p>',unsafe_allow_html=True)
        filter = st.sidebar.radio('Edit Gambar dengan filter:', ['Original','Black and White', 'Pencil Sketch', 'Blur Effect']) 
        if filter == 'Gray Image':
                converted_img = np.array(image.convert('RGB'))
                gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
                st.image(gray_scale, width=300)
        elif filter == 'Black and White':
                converted_img = np.array(image.convert('RGB'))
                gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
                slider = st.sidebar.slider('Adjust the intensity', 1, 255, 127, step=1)
                (thresh, blackAndWhiteImage) = cv2.threshold(gray_scale, slider, 255, cv2.THRESH_BINARY)
                st.image(blackAndWhiteImage, width=300)
        elif filter == 'Pencil Sketch':
                converted_img = np.array(image.convert('RGB')) 
                gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
                inv_gray = 255 - gray_scale
                slider = st.sidebar.slider('Adjust the intensity', 25, 255, 125, step=2)
                blur_image = cv2.GaussianBlur(inv_gray, (slider,slider), 0, 0)
                sketch = cv2.divide(gray_scale, 255 - blur_image, scale=256)
                st.image(sketch, width=300) 
        elif filter == 'Blur Effect':
                converted_img = np.array(image.convert('RGB'))
                slider = st.sidebar.slider('Atur intensitas', 5, 81, 33, step=2)
                converted_img = cv2.cvtColor(converted_img, cv2.COLOR_RGB2BGR)
                blur_image = cv2.GaussianBlur(converted_img, (slider,slider), 0, 0)
                st.image(blur_image, channels='BGR', width=300) 
        else: 
                st.image(image, width=300)
