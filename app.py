# 从flask包导入Flask类
# from flask import Flask

# 实例化这个类，创建一个程序对象app
# app = Flask(__name__)

# 视图函数：注册（给这个函数戴上一个装饰器的帽子）一个处理函数，这个函数是处理某个请求的处理函数（请求处理函数）
# 使用app.route()装饰器来为这个函数绑定对应的url，当用户在浏览器访问这个url的时候，就会触发这个函数，获得返回值，并把返回值显示到浏览器窗口
# /指的是根地址，只需要写出相对地址，主机地址和端口号都不需要写出，这里的/对应的就是主机后面的路径部分
# 完整的url就是http://localhost:5000/ 或是 http://127.0.0.1:5000 
# @app.route('/')
# def hello():
#     return '<h1>hello Totoro!<h1><img src="http://helloflask.com/totoro.gif">'

# 整个请求的处理过程
# 1.用户在浏览器地址栏访问这个地址，在这里即:http://localhost:5000/
# 2.服务器解析请求，发现请求url匹配的url规则是/,因此调用对应的处理函数hello()
# 3.获取hello()函数的返回值，处理后返回给客户端（浏览器）
# 4.浏览器接受响应，将其显示在窗口上

from flask import Flask,render_template
from flask import url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)

@app.route('/user/<name>')
def user_page(name):
    return f'User:{escape(name)}'

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='Daniel'))
    print(url_for('user_page',name='Peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return 'Test page'

name = 'Aimi'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]