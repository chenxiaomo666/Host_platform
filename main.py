# @Time    : 2020/1/9 13:27
# @Author  : 帅气的陈小陌
# @Email   : 13784197113@163.com
# File     : main.py
# Software : PyCharm
from database import app, db, User
from flask import request, render_template


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        # 获取前端传来的值
        username = request.form.get('username')
        password = request.form.get('password')
        u = User.query.filter_by(username=username).first()
        if u.password == password:
            return render_template('countentPage.html')
        else:
            # 前端提示密码输入错误
            return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        print(username, password, password2)

        if password == password2:
            u = User.query.filter_by(username=username).all()
            if not u:   # 代表当前注册的用户名不存在，可以注册
                user_new = User(username, password)
                db.session.add(user_new)
                db.session.commit()
                return render_template('login.html')
            else:
                return "该用户名已存在"
        else:
            # 这里应前端提示两次密码输入不一致
            return render_template('register.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


