import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Background Remover", page_icon="📷")

st.title("📷 이미지 배경 제거기 (Powered by rembg)")

uploaded_file = st.file_uploader("이미지를 업로드하세요 (jpg, png 등)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # 원본 이미지 표시
    image = Image.open(uploaded_file)
    st.subheader("업로드한 PDF 파일")
