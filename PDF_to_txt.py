import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="배경제거기", page_icon="🖼️", layout="centered")

# ---- Header ----
st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: 10px;'>🖼️ 이미지 배경 제거기</h1>
    <p style='text-align: center; color: gray; font-size: 16px;'>
        AI가 자동으로 배경을 투명하게 만들어줍니다.
    </p>
    """,
    unsafe_allow_html=True,
)

# ---- Upload Box ----
uploaded_file = st.file_uploader(
    "이미지를 업로드하세요",
    type=["jpg", "jpeg", "png"],
    help="JPG / PNG 파일 업로드 가능",
)

if uploaded_file:
    image = Image.open(uploaded_file)

    with st.container():
        st.markdown("### 📌 업로드한 이미지")
        st.image(image, use_column_width=True)

    if st.button("✨ 배경 제거하기"):
        with st.spinner("배경 제거 중입니다... ⏳"):
            result = remove(image)

        st.markdown("### 🎉 배경 제거 완료!")
        st.image(result, use_column_width=True)

        # Save result to buffer
        buf = io.BytesIO()
        result.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="📥 결과 이미지 다운로드 (PNG)",
            data=byte_im,
            file_name="removed_background.png",
            mime="image/png",
        )

else:
    st.info("좌측 또는 상단에서 이미지 파일을 업로드하세요!")

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: gray; font-size: 14px;'>
        Made with ❤️ using Streamlit + rembg
    </p>
    """,
    unsafe_allow_html=True,
)
