import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(
    page_title="배경제거기",
    page_icon="🖼️",
    layout="centered"
)

# ---- Title ----
st.markdown(
    """
    <h1 style='text-align:center;'>🖼️ 배경 제거기</h1>
    <p style='text-align:center; color:#666;'>AI가 자동으로 사진의 배경을 제거합니다.</p>
    """,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "이미지를 업로드하세요 (jpg/png)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    # Load image
    image = Image.open(uploaded_file)

    st.subheader("📌 업로드한 이미지")
    st.image(image, use_column_width=True)

    if st.button("✨ 배경 제거하기"):
        with st.spinner("배경 제거 중입니다... 잠시만 기다려주세요."):
            result = remove(image)  # rembg lightweight 모드 → opencv 필요없음

        st.subheader("🎉 결과 이미지")
        st.image(result, use_column_width=True)

        # Download output
        buf = io.BytesIO()
        result.save(buf, format="PNG")
        byte_img = buf.getvalue()

        st.download_button(
            label="📥 결과 이미지 다운로드 (PNG)",
            data=byte_img,
            file_name="removed_background.png",
            mime="image/png"
        )
else:
    st.info("이미지를 업로드하면 바로 배경 제거가 가능합니다.")
