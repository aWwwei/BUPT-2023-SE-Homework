from flask import Flask
from views.auth import auth_blueprint


app = Flask(__name__)
app.register_blueprint(auth_blueprint)

# 注册蓝图
app.register_blueprint(auth_blueprint)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'




if __name__ == '__main__':
    app.run(host='localhost', port=11451)
