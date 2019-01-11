from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '안녕하세요!!!!'

@app.route("/dictionary/<string:word>")
def dictionary(word):
    word_dict = {'apple':'사과', 'banana':'바나나', 'orange':'오렌지', 'grape':'포도'}
    return render_template('dict.html', word = word, word_dict = word_dict)
 
