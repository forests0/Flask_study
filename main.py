from flask import Flask  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Respiource):
    def get(self):
        return {"hello": "world!"}


@api.route('/hello/<string:name>')
class Hello(Resource):
    def get(self, name):
        return {"message": "Welcome, %s!" % name}

@api.route('/hello/<string:name>')
class Hello(Resource):
    def get(self, name):
        return {"message" : "Welcome, %s!" % name}



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)