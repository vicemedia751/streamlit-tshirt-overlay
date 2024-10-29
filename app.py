import streamlit as st
from PIL import Image

def main():
    st.title("T-shirt Overlay App")

    person_image = st.file_uploader("Upload Person Image", type=["jpg", "png"])
    tshirt_image = st.file_uploader("Upload T-shirt Image", type=["jpg", "png"])
    color = st.color_picker("Select T-shirt Color")

    if person_image and tshirt_image:
        # Image overlay logic goes here
        st.image(person_image, caption="Person Image")
        st.image(tshirt_image, caption="T-shirt Image")
        st.write(f"T-shirt Color: {color}")

if __name__ == "__main__":
    main()
