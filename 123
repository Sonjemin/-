from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI API 키 설정
openai.api_key = "YOUR_OPENAI_API_KEY"

# 자기소개서 생성 함수
def generate_self_intro(name, major, job_role, experience, strength):
    prompt = f"""
    아래 정보를 바탕으로 한국어로 자기소개서를 작성해줘.
    이름: {name}
    전공: {major}
    지원 직무: {job_role}
    관련 경험: {experience}
    강점 및 성격: {strength}
    
    자기소개서: 
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",  # 또는 gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "너는 뛰어난 취업 컨설턴트야."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )
    
    return response['choices'][0]['message']['content'].strip()

# API 엔드포인트
@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    name = data.get("name")
    major = data.get("major")
    job_role = data.get("job_role")
    experience = data.get("experience")
    strength = data.get("strength")

    result = generate_self_intro(name, major, job_role, experience, strength)
    return jsonify({"self_introduction": result})

if __name__ == '__main__':
    app.run(debug=True)
