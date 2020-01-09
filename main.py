# @Time    : 2020/1/9 13:27
# @Author  : 帅气的陈小陌
# @Email   : 13784197113@163.com
# File     : main.py
# Software : PyCharm
from flask import Flask, request, render_template

app = Flask(__name__)

# 先用字典储存测试，日后移交数据库
user_pwd = {}


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        # 获取前端传来的值
        username = request.form.get('username')
        password = request.form.get('password')
        if username in user_pwd and password == user_pwd[username]:
            return render_template('index.html')
        else:
            return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        print(password, password2)

        if password == password2:
            user_pwd[username] = password
            return render_template('login.html')
        else:
            return render_template('register.html')


@app.route('/')
def index():
    return render_template('index.html')


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()


