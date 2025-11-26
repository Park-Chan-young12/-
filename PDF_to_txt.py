import streamlit as st
import torch
from PIL import Image
import io

st.set_page_config(page_title="사람·사물 구별기", page_icon="🧠")

st.title("🧠 사람 / 사물 자동 구별기 (YOLOv5 기반)")

@st.cache_resource
def load_model():
    return torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)

model = load_model()

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg","jpeg","png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.subheader("📌 업로드한 이미지")
    st.image(img, use_column_width=True)

    if st.button("사람·사물 판별하기"):
        with st.spinner("분석 중..."):
            results = model(img)

        # 결과 이미지 생성
        result_img = results.render()[0]
        result_pil = Image.fromarray(result_img)

        # 사람/사물 카운트
        df = results.pandas().xyxy[0]
        person_count = (df["name"] == "person").sum()
        object_count = len(df) - person_count

        st.subheader("🧾 분석 결과")
        st.write(f"👤 **사람 감지 수:** {person_count}")
        st.write(f"📦 **사물 감지 수:** {object_count}")

        st.image(result_pil, use_column_width=True)

        # 다운로드
        buf = io.BytesIO()
        result_pil.save(buf, format="PNG")
        st.download_button(
            label="📥 결과 이미지 다운로드",
            data=buf.getvalue(),
            file_name="detected.png",
            mime="image/png",
        )
