# 从flask包导入Flask类
from flask import Flask

# 实例化这个类，创建一个程序对象app
app = Flask(__name__)

# 视图函数：注册（给这个函数戴上一个装饰器的帽子）一个处理函数，这个函数是处理某个请求的处理函数（请求处理函数）
# 使用app.route()装饰器来为这个函数绑定对应的url，当用户在浏览器访问这个url的时候，就会触发这个函数，获得返回值，并把返回值显示到浏览器窗口
# /指的是根地址，只需要写出相对地址，主机地址和端口号都不需要写出，这里的/对应的就是主机后面的路径部分
# 完整的url就是http://localhost:5000/ 或是 http://127.0.0.1:5000 
@app.route('/')
def hello():
    return '<h1>hello Totoro!<h1><img src="http://helloflask.com/totoro.gif">'

# 整个请求的处理过程
# 1.用户在浏览器地址栏访问这个地址，在这里即:http://localhost:5000/
# 2.服务器解析请求，发现请求url匹配的url规则是/,因此调用对应的处理函数hello()
# 3.获取hello()函数的返回值，处理后返回给客户端（浏览器）
# 4.浏览器接受响应，将其显示在窗口上
