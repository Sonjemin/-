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


st.title("🎯 자기소개서 기반 예상 면접 질문 생성기")

st.write("자기소개서 내용을 입력하면, 예상 질문을 도출해 드립니다.")

# 사용자 자기소개서 입력
user_input = st.text_area("📄 자기소개서 내용을 입력하세요", height=300,
                          placeholder="예: 저는 대학 시절 봉사 동아리에서 리더 역할을 맡아...")

# 버튼 클릭 시 예상 질문 생성
if st.button("🧠 예상 질문 생성하기"):
    if not user_input.strip():
        st.warning("자기소개서 내용을 입력해주세요.")
    else:
        with st.spinner("AI가 예상 질문을 생성 중입니다..."):

            prompt = f"""다음 자기소개서 내용을 읽고 면접에서 나올 법한 구체적이고 날카로운 질문을 5~7개 작성해 주세요.
각 질문은 한 줄로 작성해 주세요.

[자기소개서 내용]
{user_input}

[예상 질문]
"""

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6
            )

            questions = response['choices'][0]['message']['content']

        st.subheader("💬 예상 면접 질문")
        st.write(questions)

