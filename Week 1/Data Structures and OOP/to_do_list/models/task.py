# project_todo_app/models/task.py

class Task:
    def __init__(self, task_id, description, completed=False):
        """
        Initialize a task with an ID and description.
        """
        self.task_id = task_id          # Unique task ID (e.g., T001)
        self.description = description  # Task details
        self.completed = completed          # Status flag

    def mark_done(self):
        """
        Mark the task as completed.
        """
        self.completed = True

    def to_string(self):
        """
        Return a readable string version of the task.
        """
        status = "✅ Done" if self.completed else "❌ Not Done"
        return f"[{self.task_id}] {self.description} - {status}"
    
    def to_dict(self):
        """
        Converts the task object to a dictionary.
        Useful for serialization or JSON conversion.
        """
        return {
            "task_id" : self.task_id,
            "description" : self.description,
            "completed" : self.completed
        }
    
    @staticmethod
    def from_dict(data):
        """
        Create a task object from the JSON format.
        Useful for deserialization or JSON to Object.
        """
        return Task(
            task_id=data["task_id"],
            description=data["description"],
            completed=data["completed"]
        )