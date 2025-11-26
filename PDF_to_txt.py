import streamlit as st
from ultralytics import YOLO
from PIL import Image
import io

st.set_page_config(page_title="사람·사물 구별기", page_icon="🧠")

st.title("🧠 사람 / 사물 자동 구별기 (YOLO 기반)")

# 모델 로드 (YOLOv8n: 가벼운 모델)
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg","jpeg","png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.subheader("📌 업로드한 이미지")
    st.image(img, use_column_width=True)

    if st.button("사람·사물 판별하기"):
        with st.spinner("AI가 이미지를 분석하고 있습니다…"):
            results = model.predict(img)

        result_img = results[0].plot()   # 감지된 결과 그리기
        result_pil = Image.fromarray(result_img)

        # 사람/사물 분류
        names = model.names
        person_count = 0
        object_count = 0

        for box in results[0].boxes:
            cls = int(box.cls[0])
            label = names[cls]
            if label == "person":
                person_count += 1
            else:
                object_count += 1

        st.subheader("🧾 분석 결과")
        st.write(f"👤 **사람 감지 수:** {person_count}")
        st.write(f"📦 **사물 감지 수:** {object_count}")

        st.subheader("🔍 감지 결과 이미지")
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
