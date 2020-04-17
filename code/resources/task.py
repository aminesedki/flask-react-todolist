from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from models.task import TaskModel

class Task(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
                        'text',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, name):
        
        task = TaskModel.find_by_name(name)
        if task is not None:
            
            return task.json_format(), 200 
        
        return {'message': f"The task named {name} doesn't existe"}, 404
    
    def post(self, name):
        
        if TaskModel.find_by_name(name) is not None:
            return {'message': f"Task named {name} already existe."}
        
        data = Task.parser.parse_args()
        task = {'name': name, 'text': data['text']}
        TaskModel.insrt(task)
        return task, 201
    
    def put(self, name):
        pass 
    
    def delete(self, name):
        pass 
    
        

    
class TasksList(Resource):
    def get(self):

        return TaskModel.get_all()