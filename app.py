import os
from flask import Flask, render_template, request

app = Flask(__name__)

# 問答集
questions_answers = {
    "蘋果": "apple",
    "apple": "蘋果",
    "香蕉": "banana",
    "banana": "香蕉",
    "貓": "cat",
    "cat": "貓",
    "狗": "dog",
    "dog": "狗",
    "書": "book",
    "book": "書",
    "桌子": "table",
    "table": "桌子",
    "椅子": "chair",
    "chair": "椅子",
    "房子": "house",
    "house": "房子",
    "汽車": "car",
    "car": "汽車",
    "學校": "school",
    "school": "學校",
    "老師": "teacher",
    "teacher": "老師",
    "學生": "student",
    "student": "學生",
    "咖啡": "coffee",
    "coffee": "咖啡",
    "茶": "tea",
    "tea": "茶",
    "醫生": "doctor",
    "doctor": "醫生",
    "護士": "nurse",
    "sad": "難過"
}

# --- 各個網頁路由設定 ---
@app.route('/')
def index():
    return render_template('index.html', QA=questions_answers)

@app.route('/competition')
def competition():
    return render_template('competition.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/leadership')
def leadership():
    return render_template('leadership.html')

@app.route('/club')
def club():
    return render_template('club.html')

@app.route('/electives')
def electives():
    return render_template('electives.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')

# --- 問答功能 ---
@app.route('/ask', methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        q = request.form.get('question', '').strip()
        a = questions_answers.get(q, "抱歉，我不知道這個詞的翻譯。")
        return render_template('ask.html', question=q, answer=a)
    
    return render_template('ask.html', question="", answer="")

# --- 主程式 ---
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
