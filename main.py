import requests
import streamlit as st
api_key = "3PTFdcg8Ty5fffcD3dguLi6QcHiF4V6HRdXdCEhd"
url = "https://api.nasa.gov/planetary/apod?api_key="+api_key


response = requests.get(url)
data = response.json()
image_url = data['url']
print(type(data))

image_filepath = "img.jpg"
img_response = requests.get(image_url)
with open(image_filepath, "wb") as f:
    f.write(img_response.content)

st.header(data['title'])
st.image(image_filepath)
st.write(data['explanation'])