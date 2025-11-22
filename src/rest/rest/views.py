from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
from pymongo import MongoClient


from .repository import TodoRepository 


mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db = MongoClient(mongo_uri)['test_db']


todo_repo = TodoRepository(db.todos)

class TodoListView(APIView):
    
    def get(self, request):
        try:
            
            todos = todo_repo.get_all_todos()
            return Response(todos, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            return Response({"error": "Fetch failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            data = request.data
            if 'description' not in data or not data['description'].strip():
                return Response({"error": "Description required"}, status=status.HTTP_400_BAD_REQUEST)

           
            new_todo = todo_repo.create_todo(data['description'])
            
            return Response(new_todo, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            return Response({"error": "Creation failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)