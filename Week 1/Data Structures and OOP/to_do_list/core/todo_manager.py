# project_todo_app/core/todo_manager.py

import json
import os
from models.task import Task

class TodoManager:
    def __init__(self, file_path='tasks.json'):
        """
        Initializes an empty task list.
        """
        self.tasks = []
        self.file_path = file_path  # Path to save tasks, if needed
        self.load_from_file()  # Load existing tasks from file if needed

    def add_task(self, task_id, description):
        """
        Adds a new task if the ID is unique.
        Returns True if added, False if duplicate.
        """
        if self.get_task(task_id):
            return False  # Duplicate ID

        task = Task(task_id, description)
        self.tasks.append(task)
        return True

    def get_task(self, task_id):
        """
        Finds a task by ID. Returns the Task object or None.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def list_tasks(self):
        """
        Returns a list of all tasks.
        """
        return self.tasks

    def mark_task_done(self, task_id):
        """
        Marks a task as done if found.
        Returns True if updated, False otherwise.
        """
        task = self.get_task(task_id)
        if task:
            task.mark_done()
            return True
        return False

    def delete_task(self, task_id):
        """
        Deletes a task by ID.
        Returns True if deleted, False otherwise.
        """
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def save_to_file(self):
        """
        Saves the current task list to a file.
        This method can be implemented to save tasks in a specific format.
        """
        with open(self.file_path, 'w') as f:
            data = [task.to_dict() for task in self.tasks]
            json.dump(data,f, indent=4)

    def load_from_file(self):
        """
        Loads tasks from a file if it exists.
        This method can be implemented to load tasks in a specific format.
        """
        if not os.path.exists(self.file_path):
            return False  # No file to load from
        
        # If the file exists, read and parse the tasks
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task) for task in data]

        except Exception as e:
            print(f"Error loading tasks from file: {e}")