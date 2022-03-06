from flask import Flask,request 
from flask_restful import Resource, Api

#initialize the app and called flask 
app = Flask(__name__)

#initialize the api from flask_restful and put "app" as the argument
api=Api(app)

#create a dictionary to store the data , you can think of a dict as json-like
todos={}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


#define the resources
#create a class called Hello,world and pass the "Resource" from flask_restful
class HelloWorld(Resource):
    def get(self):
        return {'Welcome to': 'Flask RESTful API'}
api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple,'/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)