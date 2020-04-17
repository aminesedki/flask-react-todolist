import sqlite3



class TaskModel():

    def __init__(self, name, text):
        self.name = name
        self.text = text
    def json_format(self):
        return {'name': self.name, 'text': self.text}
    
    def delete(self, name): # DELET TASK AND RETURN MESSAGE 
        db_connection = sqlite3.connect('data.db')
        cursor = db_connection.cursor()

        query = "DELETE FROM tasks WHERE name=?"
        cursor.execute(query, (name,))

        db_connection.commit()
        db_connection.close()

        return {"message": f"Task named {name} successfully deleted."}

    @classmethod
    def find_by_name(cls, name): # RETURN A TASK THAT CAN BE NONE OR ALREADY EXISTE
        db_connection = sqlite3.connect('data.db')
        cursor = db_connection.cursor()

        query = "SELECT * FROM tasks WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        if row:    
            task = cls(*row)
        else:
            task = None
        db_connection.close()

        return task

    
    @classmethod
    def get_all(cls):
        db_connection = sqlite3.connect('data.db')
        cursor = db_connection.cursor()

        query = "SELECT * FROM tasks"
        result = cursor.execute(query)
        tasks = []
        
        for row in result:  
            tasks.append({'name': row[0], 'text': row[1]})

        db_connection.close()

        return tasks

    @classmethod
    def insert(cls, task): # RETURN
        db_connection = sqlite3.connect('data.db')
        cursor = db_connection.cursor()

        query = "INSERT INTO tasks VALUES( ?, ?)"
        cursor.execute(query, (task['name'], task['text']))

        db_connection.commit()
        db_connection.close()
    
    @classmethod
    def update_task(cls, task): 
        pass

    @staticmethod
    def create_tasks_table():
    
        db_connection = sqlite3.connect('data.db')
        cursor = db_connection.cursor()

        create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                        name TEXT UNIQUE NOT NULL,
                        text TEXT
                    )"""
        cursor.execute(create_tasks_table)

        db_connection.commit()
        db_connection.close()