import streamlit as st
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

st.title("✍️ AI 자기소개서 생성기")

name = st.text_input("이름")
major = st.text_input("전공")
job_role = st.text_input("지원 직무")
experience = st.text_area("관련 경험")
strength = st.text_area("강점 및 성격")

if st.button("자기소개서 생성"):
    prompt = f"""
    아래 정보를 바탕으로 한국어로 자기소개서를 작성해줘.
    이름: {name}
    전공: {major}
    지원 직무: {job_role}
    관련 경험: {experience}
    강점 및 성격: {strength}

    자기소개서:
    """
    
    with st.spinner("AI가 자기소개서를 작성 중입니다..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "너는 훌륭한 취업 자소서 코치야."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )
        result = response['choices'][0]['message']['content'].strip()
        st.success("완성된 자기소개서:")
        st.text_area("자기소개서 결과", result, height=300)
