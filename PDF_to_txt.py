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
    st.subheader("업로드한 이미지")
    st.image(image, use_column_width=True)

    # 배경 제거 버튼
    if st.button("배경 제거하기"):
        with st.spinner("배경을 제거하는 중입니다... ⏳"):
            # rembg 처리
            result = remove(image)

            # 결과물 메모리에 저장
            buf = io.BytesIO()
            result.save(buf, format="PNG")
            byte_im = buf.getvalue()

        st.subheader("배경 제거 결과")
        st.image(result, use_column_width=True)

        # 다운로드 버튼
        st.download_button(
            label="배경 제거 이미지 다운로드",
            data=byte_im,
            file_name="removed_background.png",
            mime="image/png"
        )
