import os
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from resources.task import Task, TasksList
app = Flask(__name__)
api = Api(app)

db_path = path = os.getcwd()




api.add_resource(Task, '/task/<string:name>')
api.add_resource(TasksList, '/tasks')

if __name__ == '__main__':
    from models.task import TaskModel
    TaskModel.create_tasks_table()
    app.run(port=5000, debug=True)