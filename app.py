from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' %name


@app.route('/test')
def test_url_for():
    #下面是一些调用示例
    print(url_for('hello'))
    print(url_for('user_page', name='shui'))
    print(url_for('user_page', name='da'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'
