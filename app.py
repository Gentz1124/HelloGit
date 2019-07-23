# flaskのインポート
from flask import Flask, render_template

# アプリオブジェクトの作成
app = Flask(__name__)

# ルーティング
@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/hive')
def hive():
    return render_template('index.html')

# 変数を渡すURL
@app.route('/var')
def var():
    message = "こんにちは"
    return render_template('var.html', message=message)

# For文を利用するURL
@app.route('/greeting')
def greeting():
    message_list = ["おはよう", "こんにちは", "こんばんは"]
    return render_template('greeting.html', message_list=message_list)

if __name__ == "__main__":
    app.run(debug=True)
