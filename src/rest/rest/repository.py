# Abstraction: This class handles ONLY database interactions
class TodoRepository:
    def __init__(self, db_collection):
        self.collection = db_collection

    def get_all_todos(self):
        todos = []
        cursor = self.collection.find()
        for document in cursor:
            document['_id'] = str(document['_id'])
            todos.append(document)
        return todos

    def create_todo(self, description):
        result = self.collection.insert_one({
            "description": description
        })
        return {
            "_id": str(result.inserted_id),
            "description": description
        }