import streamlit as st
import pandas as pd
from PIL import Image

st.title("File Uploading")

# 1. Image
st.subheader("1. Uploading an Image")
img_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if img_file is not None:
    file_details = {"FileName": img_file.name,'FileType':img_file.type, "FileSize":img_file.size}
    st.write(file_details)
    st.image(Image.open(img_file))
    
    
# 2. Audio
st.subheader('1. Uploading an Audio')
Audio_file = st.file_uploader('Upload Audio', type=['mp3', 'wav'])
if Audio_file is not None:
    file_details = {"FileName": Audio_file.name,'FileType':Audio_file.type, "FileSize":Audio_file.size}
    st.write(file_details)
    st.audio(Audio_file)
    
    
# 3. Video
st.subheader('1. Uploading an Video')
Video_file = st.file_uploader('Upload Video', type=['mp4', 'mov'])
if Video_file is not None:
    file_details = {"FileName": Video_file.name,'FileType':Video_file.type, "FileSize":Video_file.size}
    st.write(file_details)
    st.video(Video_file)
