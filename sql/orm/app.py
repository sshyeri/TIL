# pip install flask_sqlalchemy
# pip install flask_migrate

from flask import Flask, render_template, url_for, request, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, User
import os



app = Flask(__name__)

# flask app 에 sqlalchemy 관련 설정, 
# 'SQLALCHEMY_DATABASE_URI'는 고정값,  'sqlite:///db_flask.sqlite3'는 달라도 됨.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3' 
# True가 기본값, True일 경우 sqlalchemy 데이터베이스 객체 수정 및 신호방출 등을 추적.
# ---> 과도한 메모리를 사용.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlalchemy 초기화
# db = SQLAlchemy(app)
db.init_app(app)

migrate = Migrate(app, db)


@app.route('/')
#뷰 함수
def index():
    # url_for('index') =======>>>'/' 뷰함수를 가져가서 url을 리턴
    # return redeirect_for('index')
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/users/create')
def create():
    username = request.args.get('username')
    email = request.args.get('email')
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
    
@app.route('/users/delete/<int:id>')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
    
@app.route('/users/edit/<int:id>')
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)
    
@app.route('/users/update/<int:id>')
def update(id):
    user = User.query.get(id)
    username = request.args.get('username')
    email = request.args.get('email')
    
    user.username = username
    user.email = email
    db.session.commit()
    return redirect(url_for('index'))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)